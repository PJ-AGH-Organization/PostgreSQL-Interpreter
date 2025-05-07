# Generated from PostgreSQL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PostgreSQLParser import PostgreSQLParser
else:
    from PostgreSQLParser import PostgreSQLParser

# This class defines a complete listener for a parse tree produced by PostgreSQLParser.
class PostgreSQLListener(ParseTreeListener):

    # Enter a parse tree produced by PostgreSQLParser#statements.
    def enterStatements(self, ctx:PostgreSQLParser.StatementsContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#statements.
    def exitStatements(self, ctx:PostgreSQLParser.StatementsContext):
        pass


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


    # Enter a parse tree produced by PostgreSQLParser#createTableStatement.
    def enterCreateTableStatement(self, ctx:PostgreSQLParser.CreateTableStatementContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#createTableStatement.
    def exitCreateTableStatement(self, ctx:PostgreSQLParser.CreateTableStatementContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alterTableStatement.
    def enterAlterTableStatement(self, ctx:PostgreSQLParser.AlterTableStatementContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alterTableStatement.
    def exitAlterTableStatement(self, ctx:PostgreSQLParser.AlterTableStatementContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alterAction.
    def enterAlterAction(self, ctx:PostgreSQLParser.AlterActionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alterAction.
    def exitAlterAction(self, ctx:PostgreSQLParser.AlterActionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#alterColumnAction.
    def enterAlterColumnAction(self, ctx:PostgreSQLParser.AlterColumnActionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#alterColumnAction.
    def exitAlterColumnAction(self, ctx:PostgreSQLParser.AlterColumnActionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#dropTableStatement.
    def enterDropTableStatement(self, ctx:PostgreSQLParser.DropTableStatementContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#dropTableStatement.
    def exitDropTableStatement(self, ctx:PostgreSQLParser.DropTableStatementContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#columnDef.
    def enterColumnDef(self, ctx:PostgreSQLParser.ColumnDefContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#columnDef.
    def exitColumnDef(self, ctx:PostgreSQLParser.ColumnDefContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#tableConstraint.
    def enterTableConstraint(self, ctx:PostgreSQLParser.TableConstraintContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#tableConstraint.
    def exitTableConstraint(self, ctx:PostgreSQLParser.TableConstraintContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#columnConstraint.
    def enterColumnConstraint(self, ctx:PostgreSQLParser.ColumnConstraintContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#columnConstraint.
    def exitColumnConstraint(self, ctx:PostgreSQLParser.ColumnConstraintContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#dataType.
    def enterDataType(self, ctx:PostgreSQLParser.DataTypeContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#dataType.
    def exitDataType(self, ctx:PostgreSQLParser.DataTypeContext):
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


    # Enter a parse tree produced by PostgreSQLParser#limitClause.
    def enterLimitClause(self, ctx:PostgreSQLParser.LimitClauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#limitClause.
    def exitLimitClause(self, ctx:PostgreSQLParser.LimitClauseContext):
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


    # Enter a parse tree produced by PostgreSQLParser#columnExpression.
    def enterColumnExpression(self, ctx:PostgreSQLParser.ColumnExpressionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#columnExpression.
    def exitColumnExpression(self, ctx:PostgreSQLParser.ColumnExpressionContext):
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


    # Enter a parse tree produced by PostgreSQLParser#standardCondition.
    def enterStandardCondition(self, ctx:PostgreSQLParser.StandardConditionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#standardCondition.
    def exitStandardCondition(self, ctx:PostgreSQLParser.StandardConditionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#havingCondition.
    def enterHavingCondition(self, ctx:PostgreSQLParser.HavingConditionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#havingCondition.
    def exitHavingCondition(self, ctx:PostgreSQLParser.HavingConditionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#whereExpression.
    def enterWhereExpression(self, ctx:PostgreSQLParser.WhereExpressionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#whereExpression.
    def exitWhereExpression(self, ctx:PostgreSQLParser.WhereExpressionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#havingExpression.
    def enterHavingExpression(self, ctx:PostgreSQLParser.HavingExpressionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#havingExpression.
    def exitHavingExpression(self, ctx:PostgreSQLParser.HavingExpressionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#tableList.
    def enterTableList(self, ctx:PostgreSQLParser.TableListContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#tableList.
    def exitTableList(self, ctx:PostgreSQLParser.TableListContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#tableWithAlias.
    def enterTableWithAlias(self, ctx:PostgreSQLParser.TableWithAliasContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#tableWithAlias.
    def exitTableWithAlias(self, ctx:PostgreSQLParser.TableWithAliasContext):
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


    # Enter a parse tree produced by PostgreSQLParser#joinCondition.
    def enterJoinCondition(self, ctx:PostgreSQLParser.JoinConditionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#joinCondition.
    def exitJoinCondition(self, ctx:PostgreSQLParser.JoinConditionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#aggregateFunction.
    def enterAggregateFunction(self, ctx:PostgreSQLParser.AggregateFunctionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#aggregateFunction.
    def exitAggregateFunction(self, ctx:PostgreSQLParser.AggregateFunctionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#countFunction.
    def enterCountFunction(self, ctx:PostgreSQLParser.CountFunctionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#countFunction.
    def exitCountFunction(self, ctx:PostgreSQLParser.CountFunctionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#tableName.
    def enterTableName(self, ctx:PostgreSQLParser.TableNameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#tableName.
    def exitTableName(self, ctx:PostgreSQLParser.TableNameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#tableAliasName.
    def enterTableAliasName(self, ctx:PostgreSQLParser.TableAliasNameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#tableAliasName.
    def exitTableAliasName(self, ctx:PostgreSQLParser.TableAliasNameContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#columnAliasName.
    def enterColumnAliasName(self, ctx:PostgreSQLParser.ColumnAliasNameContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#columnAliasName.
    def exitColumnAliasName(self, ctx:PostgreSQLParser.ColumnAliasNameContext):
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


    # Enter a parse tree produced by PostgreSQLParser#mathOperator.
    def enterMathOperator(self, ctx:PostgreSQLParser.MathOperatorContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#mathOperator.
    def exitMathOperator(self, ctx:PostgreSQLParser.MathOperatorContext):
        pass



del PostgreSQLParser