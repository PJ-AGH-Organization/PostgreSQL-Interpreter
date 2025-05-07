import sqlite3
from antlr4 import *
from fastapi_utils.cbv import cbv
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from utils.Query import Query
from utils.MyErrorListener import MyErrorListener
from utils.StructureValidator import StructureValidator
from database.DatabaseInitializer import prepare_database
from AntlrFiles.PostgreSQLLexer import PostgreSQLLexer
from AntlrFiles.PostgreSQLParser import PostgreSQLParser

router = APIRouter()


@cbv(router)
class SQLInterpreter:
    def format_tree(self, tree, parser, indent=0):
        if tree.getChildCount() == 0:
            return "  " * indent + tree.getText() + "\n"
        result = "  " * indent + parser.ruleNames[tree.getRuleIndex()] + "\n"
        for i in range(tree.getChildCount()):
            result += self.format_tree(tree.getChild(i), parser, indent + 1)
        return result

    def parse_sql(self, query):
        input_stream = InputStream(query)
        lexer = PostgreSQLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = PostgreSQLParser(stream)

        error_listener = MyErrorListener()
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)

        tree = parser.statements()
        success = not error_listener.errors
        return tree, parser, success, error_listener.errors

    def execute_sql_query(self, query: str):
        conn = sqlite3.connect("database/sample_database.db")
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description] if cursor.description else []
            return [dict(zip(columns, row)) for row in rows], True
        except Exception as e:
            return str(e), False
        finally:
            conn.commit()
            conn.close()

    @router.post("/execute")
    def execute(self, query: Query):
        if query.query == "":
            return

        tree, parser, success, errors = self.parse_sql(query.query)

        if not success:
            return {"error": "Błąd składni zapytania SQL",
                    "details": errors}

        queries = query.query.split(";")
        queries = queries[:-1]
        result_dict = {}

        for counter, curr_query in enumerate(queries):
            key = f"query {counter + 1}"
            result_dict[key] = {}
            stmt = tree.statement(counter)
            if parser.ruleNames[stmt.getChild(0).getRuleIndex()] == "createTableStatement":
                self.execute_sql_query(curr_query)
                continue

            if (parser.ruleNames[stmt.getChild(0).getRuleIndex()] == "alterTableStatement" and
                    stmt.getChild(0).getChild(3).getChild(0).getText() == "ADD"):
                self.execute_sql_query(curr_query)
                continue

            tables_validation_result = StructureValidator.validate_table_names(stmt, parser)
            if tables_validation_result["error"] is not None:
                result_dict[key]["error"] = tables_validation_result["error"]
                return result_dict

            columns_validation_result = StructureValidator.validate_column_names(stmt, parser,
                                                                                 tables_validation_result[
                                                                                     'used_tables'])
            if columns_validation_result["error"] is not None:
                result_dict[key]["error"] = columns_validation_result["error"]
                return result_dict

            res, checker = self.execute_sql_query(curr_query)
            if checker:
                result_dict[key]["result"] = res
            else:
                result_dict[key]["error"] = res

        return result_dict


app = FastAPI(lifespan=prepare_database)
app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
