import os
import sqlite3
import pandas as pd

from antlr4 import *
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from antlr4.error.ErrorListener import ErrorListener
from AntlrFiles.PostgreSQLLexer import PostgreSQLLexer
from AntlrFiles.PostgreSQLParser import PostgreSQLParser
from validateTables import validateTableNames
from validateColumns import validateColumnNames


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Query(BaseModel):
    query: str


class MyErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Line {line}:{column} - {msg}")


def prepare_database():
    names = [
        "categories.csv", "customers.csv", "employee_territories.csv",
        "employees.csv", "orders.csv", "orders_details.csv",
        "products.csv", "regions.csv", "shippers.csv",
        "suppliers.csv", "territories.csv"
    ]
    for name in names:
        path = os.path.join("resources", name)
        if os.path.exists(path):
            df = pd.read_csv(path, sep=",")
            try:
                with sqlite3.connect("sample_database.db") as conn:
                    df.to_sql(name[:-4], conn, if_exists="fail", index=False)
            except ValueError:
                print(f"Table '{name[:-4]}' already exists.")
        else:
            print(f"File {name} not found.")


def format_tree(tree, parser, indent=0):
    if tree.getChildCount() == 0:
        return "  " * indent + tree.getText() + "\n"
    result = "  " * indent + parser.ruleNames[tree.getRuleIndex()] + "\n"
    for i in range(tree.getChildCount()):
        result += format_tree(tree.getChild(i), parser, indent + 1)
    return result


def parse_sql(sql):
    input_stream = InputStream(sql)
    lexer = PostgreSQLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PostgreSQLParser(stream)

    error_listener = MyErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.statements()
    success = not error_listener.errors
    return tree, parser, success, error_listener.errors


def execute_sql_query(query: str):
    conn = sqlite3.connect("sample_database.db")
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description] if cursor.description else []
        return {"result": [dict(zip(columns, row)) for row in rows]}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conn.commit()
        conn.close()


@app.post("/execute")
def execute(query: Query):

    prepare_database()

    tree, parser, success, errors = parse_sql(query.query)


    if not success:
        return {"error": "Błąd składni zapytania SQL", "details": errors}

    foundErrorsInTableNames = validateTableNames(tree, parser)
    if not foundErrorsInTableNames['all_exist']:
        return {"error": "Nie ma takiej tabeli w bazie",
                "Missing tables": foundErrorsInTableNames['missing_tables']}

    foundErrorsInColumnsNames = validateColumnNames(tree, parser, foundErrorsInTableNames['used_tables'])
    if not foundErrorsInColumnsNames["all_exist"]:
        return {"error": "Nie ma takiej kolumny w bazie",
                "Missing columns": foundErrorsInColumnsNames['missing_columns']}

    return execute_sql_query(query.query)


def execute_test(query: str):
    prepare_database()

    tree, parser, success, errors = parse_sql(query)

    if not success:
        return {"error": "Błąd składni zapytania SQL", "details": errors}

    foundErrorsInTableNames = validateTableNames(tree, parser)
    if not foundErrorsInTableNames['all_exist']:
        return {"error": "Nie ma takiej tabeli w bazie",
                "Missing tables": foundErrorsInTableNames['missing_tables']}

    foundErrorsInColumnsNames = validateColumnNames(tree, parser, foundErrorsInTableNames['used_tables'])
    if not foundErrorsInColumnsNames["all_exist"]:
        return {"error": "Nie ma takiej kolumny w bazie", "Missing columns": foundErrorsInColumnsNames['missing_columns']}
    return execute_sql_query(query)


