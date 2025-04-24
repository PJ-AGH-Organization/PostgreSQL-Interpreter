import sqlite3
from antlr4 import *
from AntlrFiles.PostgreSQLLexer import PostgreSQLLexer
from AntlrFiles.PostgreSQLParser import PostgreSQLParser
import os
import pandas as pd
from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []  # Przechowuj błędy w liście

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = f"Line {line}:{column} - {msg}"
        self.errors.append(error_msg)  # Dodaj błąd do listy





def format_tree(tree, parser, indent=0):
    if tree.getChildCount() == 0:
        return "  " * indent + tree.getText() + "\n"
    result = "  " * indent + parser.ruleNames[tree.getRuleIndex()] + "\n"
    for i in range(tree.getChildCount()):
        result += format_tree(tree.getChild(i), parser, indent + 1)
    return result


def parse_sql(sql):

    successFlag = True
    input_stream = InputStream(sql)
    lexer = PostgreSQLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PostgreSQLParser(stream)

    error_listener = MyErrorListener()
    parser.removeErrorListeners()  # Usuń domyślny listener
    parser.addErrorListener(error_listener)  # Dodaj nasz listener

    tree = parser.statements()

    if error_listener.errors:
        successFlag = False
        print("Znaleziono błędy:")
        for error in error_listener.errors:
            print(error)
    else:
        print("Parsowanie zakończone sukcesem.")


    formatted_tree = format_tree(tree, parser)
    print("\nParsed SQL:\n" + sql)
    print("\nParse Tree:\n" + formatted_tree)
    return tree, parser, successFlag

def prepare_database():

    names = ["categories.csv", "customers.csv", "employee_territories.csv",
             "employees.csv", "orders.csv", "orders_details.csv",
             "products.csv", "regions.csv", "shippers.csv", "suppliers.csv", "territories.csv"]

    for name in names:
        categoriesDf = pd.read_csv(os.path.join("resources", f"{name}"), sep=",")

        try:

            with sqlite3.connect("sample_database.db") as conn:
                categoriesDf.to_sql(name[:-4], conn, if_exists="fail", index=False)
        except ValueError as e:
            print(f"Column already exists!!!!!")


def execute_sql_query(query):
    conn = sqlite3.connect("sample_database.db")
    cursor = conn.cursor()

    for subquery in query.split(";")[:-1]:
        ans = cursor.execute(subquery.strip() + ";")
        yield ans.fetchall()


def main():
    prepare_database()
    query = ("SELECT * FROM suppliers;"
             "chuhjuuj;"
             "SELECT * FROM suppliers;"
             )


    tree, parser, successFlag = parse_sql(query)

    if not successFlag:
        return

    res = list(execute_sql_query(query))

    for sub_result in res:
        print(sub_result)
        print("-------------------------------")


if __name__ == "__main__":
    main()

