from antlr4 import *
from antlr4.tree.Trees import Trees
from PostgreSQLLexer import PostgreSQLLexer
from PostgreSQLParser import PostgreSQLParser
import sys


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


if __name__ == "__main__":
    sql_query = """
    SELECT COUNT(id), name
    FROM users
    INNER JOIN orders ON users.id = orders.user_id
    GROUP BY name
    HAVING COUNT(id) > 5
    """
    parse_sql(sql_query)