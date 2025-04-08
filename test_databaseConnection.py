import psycopg2
from antlr4 import *
from PostgreSQLLexer import PostgreSQLLexer
from PostgreSQLParser import PostgreSQLParser


# Funkcja formatowania drzewa składniowego
def format_tree(tree, parser, indent=0):
    if tree.getChildCount() == 0:
        return "  " * indent + tree.getText() + "\n"
    result = "  " * indent + parser.ruleNames[tree.getRuleIndex()] + "\n"
    for i in range(tree.getChildCount()):
        result += format_tree(tree.getChild(i), parser, indent + 1)
    return result


# Funkcja do analizy zapytania SQL
def parse_sql(sql):
    input_stream = InputStream(sql)
    lexer = PostgreSQLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PostgreSQLParser(stream)
    tree = parser.statement()

    formatted_tree = format_tree(tree, parser)
    print("\nParsed SQL:\n" + sql)
    print("\nParse Tree:\n" + formatted_tree)
    return tree


# Funkcja do wykonania zapytania SQL na bazie danych PostgreSQL
def execute_sql_query(query):
    try:
        # Połączenie z bazą danych PostgreSQL
        connection = psycopg2.connect(
            host="localhost",  # Zmienna hosta
            database="postgres",  # Zmienna bazy danych
            user="postgres",  # Zmienna użytkownika
            password="Jan12345*"  # Zmienna hasła
        )

        cursor = connection.cursor()

        # Przeanalizowanie zapytania
        tree = parse_sql(query)

        # Wykonanie zapytania na bazie danych
        cursor.execute(query)
        result = cursor.fetchall()

        print("\nQuery Results:")
        for row in result:
            print(row)

        # Zamknięcie połączenia
        cursor.close()
        connection.close()

    except Exception as error:
        print("Błąd połączenia z bazą danych:", error)


# Przykład zapytania SQL do testowania
if __name__ == "__main__":
    sql_query = """
    SELECT id_badania, nazwa
    FROM badania;
    """
    execute_sql_query(sql_query)
