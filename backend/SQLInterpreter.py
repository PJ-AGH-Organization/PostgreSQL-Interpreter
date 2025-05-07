import os
import sqlite3
import pandas as pd
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
    #Aktualnie obecne tylko w celach testowych - potem się wyjebie, bo jest to używane w DatabaseInitializer
    # def prepare_database(self):
    #     names = [
    #         "categories.csv", "customers.csv", "employee_territories.csv",
    #         "employees.csv", "orders.csv", "orders_details.csv",
    #         "products.csv", "regions.csv", "shippers.csv",
    #         "suppliers.csv", "territories.csv"
    #     ]
    #     for name in names:
    #         path = os.path.join("resources", name)
    #         if os.path.exists(path):
    #             df = pd.read_csv(path, sep=",")
    #             try:
    #                 with sqlite3.connect("database/sample_database.db") as conn:
    #                     df.to_sql(name[:-4], conn, if_exists="fail", index=False)
    #             except ValueError:
    #                 print(f"Table '{name[:-4]}' already exists.")
    #         else:
    #             print(f"File {name} not found.")

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

            tables_validation_result = StructureValidator.validate_table_names(tree.statement(counter), parser)
            if tables_validation_result["error"] is not None:
                result_dict[key]["error"] = tables_validation_result["error"]
                return result_dict

            columns_validation_result = StructureValidator.validate_column_names(tree.statement(counter), parser,
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

    # def execute_test(self, query: str):
    #     tree, parser, success, errors = self.parse_sql(query)
    #
    #     print(self.format_tree(tree, parser))
    #
    #     if not success:
    #         return {"error": "Błąd składni zapytania SQL", "details": errors}
    #
    #     queries = query.split(";")
    #     queries = queries[:-1]
    #     result_dict = {}
    #
    #     for counter, curr_query in enumerate(queries):
    #         key = f"query {counter+1}"
    #         result_dict[key] = {}
    #
    #         tables_validation_result = StructureValidator.validate_table_names(tree.statement(counter), parser)
    #         if tables_validation_result["error"] is not None:
    #             result_dict[key]["error"] = tables_validation_result["error"]
    #             return result_dict
    #
    #         columns_validation_result = StructureValidator.validate_column_names(tree.statement(counter), parser, tables_validation_result['used_tables'])
    #         if columns_validation_result["error"] is not None:
    #             result_dict[key]["error"] = columns_validation_result["error"]
    #             return result_dict
    #
    #         res, checker = self.execute_sql_query(curr_query)
    #         if checker:
    #             result_dict[key]["result"] = res
    #         else:
    #             result_dict[key]["error"] = res
    #
    #     return result_dict


# if __name__ == "__main__":
#     sql = SQLInterpreter()
#     sql.prepare_database()
#     print(sql.execute_test("SELECT COUNT(*) AS liczba FROM suppliers s JOIN customers c USING (city) WHERE s.supplierid > 10;"
#                            "SELECT s.supplierid FROM suppliers s;"))


app = FastAPI(lifespan=prepare_database)
app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
