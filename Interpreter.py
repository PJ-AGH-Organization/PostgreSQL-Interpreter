from PostgreSQLVisitor import PostgreSQLVisitor
from PostgreSQLParser import PostgreSQLParser


class Interpreter(PostgreSQLVisitor):
    def visitSelectStatement(self, ctx: PostgreSQLParser.SelectStatementContext):
        columns = ctx.columnList().getText()
        table = ctx.tableList().getText()

        return {
            "type": "SELECT",
            "columns": columns,
            "table": table
        }
