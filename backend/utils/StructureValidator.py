from antlr4 import *
import sqlite3


class StructureValidator:
    @staticmethod
    def validate_table_names(tree, parser):
        table_names = StructureValidator.find_table_names(tree, parser)

        with sqlite3.connect("database/sample_database.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            existing_tables = {row[0].lower() for row in cursor.fetchall()}

        missing = [name for name in table_names.keys() if name.lower() not in existing_tables]
        unique_aliases = len(set(table_names.values())) == len(table_names)
        error = None
        if len(missing) > 0:
            error = f"Some of used tables does not exist in the database: "
            for table in missing:
                error += f"{table} | "
        elif not unique_aliases:
            error = f"Aliases for tables must be unique!"

        return {
            "error": error,
            "used_tables": table_names
        }

    @staticmethod
    def validate_column_names(tree, parser, used_tables):
        column_names = StructureValidator.find_column_names(tree, parser)

        with sqlite3.connect("database/sample_database.db") as conn:
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
        for col, alias in column_names.items():
            col_lower = col.lower()
            if alias is None:
                found_in = [table for table, cols in table_to_columns.items() if col_lower in cols]
            else:
                found_in = [table for table, t_alias in used_tables.items()
                            if alias == t_alias and col_lower in table_to_columns[table]]
            column_status[col] = found_in

        missing = [col for col, tables in column_status.items() if not tables]
        error = None
        if len(missing) > 0:
            error = f"Some of used columns does not exist in tables: "
            for col in missing:
                if column_names[col] is None:
                    error += f"{col} | "
                else:
                    tab = [table for table, alias in used_tables.items() if alias == column_names[col]]
                    if len(tab) > 0:
                        error += f"{col} in table {tab[0]} | "
                    else:
                        error += f"{col} | "

        return {
            "error": error,
            "column_table_map": column_status
        }

    @staticmethod
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
        return result

    @staticmethod
    def find_column_names(tree, parser):
        result = {}

        def traverse(node):
            if isinstance(node, ParserRuleContext):
                rule_name = parser.ruleNames[node.getRuleIndex()]
                if rule_name == "columnName":
                    splitted = node.getText().split('.')
                    result[splitted[-1]] = splitted[0] if len(splitted) == 2 else None
            for i in range(node.getChildCount()):
                traverse(node.getChild(i))

        traverse(tree)
        return result
