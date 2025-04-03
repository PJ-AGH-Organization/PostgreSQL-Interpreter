# Generated from PostgreSQL.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .PostgreSQLParser import PostgreSQLParser
else:
    from PostgreSQLParser import PostgreSQLParser

# This class defines a complete listener for a parse tree produced by PostgreSQLParser.
class PostgreSQLListener(ParseTreeListener):

    # Enter a parse tree produced by PostgreSQLParser#statement.
    def enterStatement(self, ctx:PostgreSQLParser.StatementContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#statement.
    def exitStatement(self, ctx:PostgreSQLParser.StatementContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#selectStatement.
    def enterSelectStatement(self, ctx:PostgreSQLParser.SelectStatementContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#selectStatement.
    def exitSelectStatement(self, ctx:PostgreSQLParser.SelectStatementContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#insertStatement.
    def enterInsertStatement(self, ctx:PostgreSQLParser.InsertStatementContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#insertStatement.
    def exitInsertStatement(self, ctx:PostgreSQLParser.InsertStatementContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#updateStatement.
    def enterUpdateStatement(self, ctx:PostgreSQLParser.UpdateStatementContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#updateStatement.
    def exitUpdateStatement(self, ctx:PostgreSQLParser.UpdateStatementContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#deleteStatement.
    def enterDeleteStatement(self, ctx:PostgreSQLParser.DeleteStatementContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#deleteStatement.
    def exitDeleteStatement(self, ctx:PostgreSQLParser.DeleteStatementContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#whereClause.
    def enterWhereClause(self, ctx:PostgreSQLParser.WhereClauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#whereClause.
    def exitWhereClause(self, ctx:PostgreSQLParser.WhereClauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#groupByClause.
    def enterGroupByClause(self, ctx:PostgreSQLParser.GroupByClauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#groupByClause.
    def exitGroupByClause(self, ctx:PostgreSQLParser.GroupByClauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#havingClause.
    def enterHavingClause(self, ctx:PostgreSQLParser.HavingClauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#havingClause.
    def exitHavingClause(self, ctx:PostgreSQLParser.HavingClauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#orderByClause.
    def enterOrderByClause(self, ctx:PostgreSQLParser.OrderByClauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#orderByClause.
    def exitOrderByClause(self, ctx:PostgreSQLParser.OrderByClauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#columnList.
    def enterColumnList(self, ctx:PostgreSQLParser.ColumnListContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#columnList.
    def exitColumnList(self, ctx:PostgreSQLParser.ColumnListContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#column.
    def enterColumn(self, ctx:PostgreSQLParser.ColumnContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#column.
    def exitColumn(self, ctx:PostgreSQLParser.ColumnContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#valueList.
    def enterValueList(self, ctx:PostgreSQLParser.ValueListContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#valueList.
    def exitValueList(self, ctx:PostgreSQLParser.ValueListContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#assignmentList.
    def enterAssignmentList(self, ctx:PostgreSQLParser.AssignmentListContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#assignmentList.
    def exitAssignmentList(self, ctx:PostgreSQLParser.AssignmentListContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#assignment.
    def enterAssignment(self, ctx:PostgreSQLParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#assignment.
    def exitAssignment(self, ctx:PostgreSQLParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#condition.
    def enterCondition(self, ctx:PostgreSQLParser.ConditionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#condition.
    def exitCondition(self, ctx:PostgreSQLParser.ConditionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#expression.
    def enterExpression(self, ctx:PostgreSQLParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#expression.
    def exitExpression(self, ctx:PostgreSQLParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#tableList.
    def enterTableList(self, ctx:PostgreSQLParser.TableListContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#tableList.
    def exitTableList(self, ctx:PostgreSQLParser.TableListContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#joinClause.
    def enterJoinClause(self, ctx:PostgreSQLParser.JoinClauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#joinClause.
    def exitJoinClause(self, ctx:PostgreSQLParser.JoinClauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#joinType.
    def enterJoinType(self, ctx:PostgreSQLParser.JoinTypeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#joinType.
    def exitJoinType(self, ctx:PostgreSQLParser.JoinTypeContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#aggregateFunction.
    def enterAggregateFunction(self, ctx:PostgreSQLParser.AggregateFunctionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#aggregateFunction.
    def exitAggregateFunction(self, ctx:PostgreSQLParser.AggregateFunctionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#windowFunction.
    def enterWindowFunction(self, ctx:PostgreSQLParser.WindowFunctionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#windowFunction.
    def exitWindowFunction(self, ctx:PostgreSQLParser.WindowFunctionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#partitionByClause.
    def enterPartitionByClause(self, ctx:PostgreSQLParser.PartitionByClauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#partitionByClause.
    def exitPartitionByClause(self, ctx:PostgreSQLParser.PartitionByClauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#tableName.
    def enterTableName(self, ctx:PostgreSQLParser.TableNameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#tableName.
    def exitTableName(self, ctx:PostgreSQLParser.TableNameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#columnName.
    def enterColumnName(self, ctx:PostgreSQLParser.ColumnNameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#columnName.
    def exitColumnName(self, ctx:PostgreSQLParser.ColumnNameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#value.
    def enterValue(self, ctx:PostgreSQLParser.ValueContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#value.
    def exitValue(self, ctx:PostgreSQLParser.ValueContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:PostgreSQLParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:PostgreSQLParser.ComparisonOperatorContext):
        pass



del PostgreSQLParser