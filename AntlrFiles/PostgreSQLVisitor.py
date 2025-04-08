# Generated from PostgreSQL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PostgreSQLParser import PostgreSQLParser
else:
    from PostgreSQLParser import PostgreSQLParser

# This class defines a complete generic visitor for a parse tree produced by PostgreSQLParser.

class PostgreSQLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PostgreSQLParser#statement.
    def visitStatement(self, ctx:PostgreSQLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#selectStatement.
    def visitSelectStatement(self, ctx:PostgreSQLParser.SelectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#insertStatement.
    def visitInsertStatement(self, ctx:PostgreSQLParser.InsertStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#updateStatement.
    def visitUpdateStatement(self, ctx:PostgreSQLParser.UpdateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#deleteStatement.
    def visitDeleteStatement(self, ctx:PostgreSQLParser.DeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#whereClause.
    def visitWhereClause(self, ctx:PostgreSQLParser.WhereClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#groupByClause.
    def visitGroupByClause(self, ctx:PostgreSQLParser.GroupByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#havingClause.
    def visitHavingClause(self, ctx:PostgreSQLParser.HavingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#orderByClause.
    def visitOrderByClause(self, ctx:PostgreSQLParser.OrderByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#columnList.
    def visitColumnList(self, ctx:PostgreSQLParser.ColumnListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#column.
    def visitColumn(self, ctx:PostgreSQLParser.ColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#valueList.
    def visitValueList(self, ctx:PostgreSQLParser.ValueListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#assignmentList.
    def visitAssignmentList(self, ctx:PostgreSQLParser.AssignmentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#assignment.
    def visitAssignment(self, ctx:PostgreSQLParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#condition.
    def visitCondition(self, ctx:PostgreSQLParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#expression.
    def visitExpression(self, ctx:PostgreSQLParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#tableList.
    def visitTableList(self, ctx:PostgreSQLParser.TableListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#joinClause.
    def visitJoinClause(self, ctx:PostgreSQLParser.JoinClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#joinType.
    def visitJoinType(self, ctx:PostgreSQLParser.JoinTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#aggregateFunction.
    def visitAggregateFunction(self, ctx:PostgreSQLParser.AggregateFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#semicolon.
    def visitSemicolon(self, ctx:PostgreSQLParser.SemicolonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#tableName.
    def visitTableName(self, ctx:PostgreSQLParser.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#columnName.
    def visitColumnName(self, ctx:PostgreSQLParser.ColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#value.
    def visitValue(self, ctx:PostgreSQLParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:PostgreSQLParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)



del PostgreSQLParser