from antlr4 import *
import sqlite3

def find_table_names(tree, parser):
    result = []

    def traverse(node):
        if isinstance(node, ParserRuleContext):
            rule_name = parser.ruleNames[node.getRuleIndex()]
            if rule_name == "tableName":
                result.append(node.getText())
        for i in range(node.getChildCount()):
            traverse(node.getChild(i))

    traverse(tree)
    return result

def validateTableNames(tree, parser):
    table_names = find_table_names(tree, parser)
    existing_tables = []

    with sqlite3.connect("sample_database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        existing_tables = {row[0].lower() for row in cursor.fetchall()}

    missing = [name for name in table_names if name.lower() not in existing_tables]

    return {
        "all_exist": len(missing) == 0,
        "missing_tables": missing,
        "used_tables": table_names
    }
