import psycopg2
from antlr4 import *
from AntlrFiles.PostgreSQLLexer import PostgreSQLLexer
from AntlrFiles.PostgreSQLParser import PostgreSQLParser


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
    tree = parser.statement()

    formatted_tree = format_tree(tree, parser)
    print("\nParsed SQL:\n" + sql)
    print("\nParse Tree:\n" + formatted_tree)
    return tree, parser


def execute_sql_query(query):
    try:

        connection = psycopg2.connect(
            host="db.ebeuhtgbpprwweegiasr.supabase.co",
            database="postgres",
            user="postgres",
            password="Kompilatory2025"
        )

        cursor = connection.cursor()

        tree, _ = parse_sql(query)

        cursor.execute(query)
        result = cursor.fetchall()

        print("\nQuery Results:")
        for row in result:
            print(row)

        cursor.close()
        connection.close()

    except Exception as error:
        print("Błąd połączenia z bazą danych:", error)


if __name__ == "__main__":
    sql_query = """
    SELECT id, age, name, surname
    FROM users;
    """
    execute_sql_query(sql_query)
