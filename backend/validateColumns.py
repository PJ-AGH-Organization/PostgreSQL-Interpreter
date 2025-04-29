import sqlite3
from antlr4 import *

def find_column_names(tree, parser):
    result = []

    def traverse(node):
        if isinstance(node, ParserRuleContext):
            rule_name = parser.ruleNames[node.getRuleIndex()]
            if rule_name == "columnName":
                result.append(node.getText())
        for i in range(node.getChildCount()):
            traverse(node.getChild(i))

    traverse(tree)
    return result

def validateColumnNames(tree, parser, used_tables):
    column_names = find_column_names(tree, parser)

    with sqlite3.connect("sample_database.db") as conn:
        cursor = conn.cursor()
        table_to_columns = {}

        for table in used_tables:
            try:
                cursor.execute(f"PRAGMA table_info({table})")
                cols = [row[1].lower() for row in cursor.fetchall()]
                table_to_columns[table] = cols
            except sqlite3.OperationalError:
                table_to_columns[table] = []

    column_status = {}
    for col in column_names:
        col_lower = col.lower()
        found_in = [table for table, cols in table_to_columns.items() if col_lower in cols]
        column_status[col] = found_in

    missing = [col for col, tables in column_status.items() if not tables]

    return {
        "all_exist": len(missing) == 0,
        "missing_columns": missing,
        "column_table_map": column_status
    }


