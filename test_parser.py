from antlr4 import *
from PostgreSQLLexer import PostgreSQLLexer
from PostgreSQLParser import PostgreSQLParser
from antlr4.tree.Trees import Trees

def main():
    # Przykładowe zapytanie SQL
    sql_query = "SELECT name, age FROM users;"

    # Tworzymy strumień wejściowy
    input_stream = InputStream(sql_query)

    # Tworzymy leksykera
    lexer = PostgreSQLLexer(input_stream)

    # Tworzymy strumień tokenów
    token_stream = CommonTokenStream(lexer)

    # Tworzymy parser
    parser = PostgreSQLParser(token_stream)

    # Parsowanie zapytania SQL i uzyskiwanie drzewa składniowego
    tree = parser.statement()  # 'statement' to reguła startowa w Twojej gramatyce

    # Drukowanie drzewa składniowego
    print("Drzewo składniowe:")
    print(Trees.toStringTree(tree, None, parser))  # wyświetlenie drzewa składniowego w formie tekstowej


if __name__ == "__main__":
    main()
