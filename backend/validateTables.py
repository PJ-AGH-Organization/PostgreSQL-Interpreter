from antlr4 import *
import sqlite3

def find_table_names(tree, parser):
    stack = []
    result = {}

    def traverse(node):
        if isinstance(node, ParserRuleContext):
            rule_name = parser.ruleNames[node.getRuleIndex()]
            if rule_name == "tableName":
                stack.append(node.getText())
            elif rule_name == "aliasName":
                result[stack.pop()] = node.getText()
        for i in range(node.getChildCount()):
            traverse(node.getChild(i))

    while len(stack) > 0:
        result[stack.pop()] = None

    traverse(tree)
    print(f"{result=}")
    return result

def validateTableNames(tree, parser):
    table_names = find_table_names(tree, parser)
    existing_tables = []

    with sqlite3.connect("sample_database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        existing_tables = {row[0].lower() for row in cursor.fetchall()}

    missing = [name for name in table_names.keys() if name.lower() not in existing_tables]
    print(f"{missing=}")

    return {
        "all_exist": len(missing) == 0,
        "missing_tables": missing,
        "used_tables": table_names
    }
