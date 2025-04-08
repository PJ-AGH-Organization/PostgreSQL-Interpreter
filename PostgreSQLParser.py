# Generated from PostgreSQL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,39,190,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,1,0,1,0,1,0,3,0,
        55,8,0,1,1,1,1,1,1,1,1,1,1,3,1,62,8,1,1,1,3,1,65,8,1,1,1,3,1,68,
        8,1,1,1,3,1,71,8,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,3,3,92,8,3,1,3,1,3,1,4,1,4,1,4,1,4,
        3,4,100,8,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,
        1,8,1,9,1,9,1,9,5,9,119,8,9,10,9,12,9,122,9,9,1,10,1,10,3,10,126,
        8,10,1,11,1,11,1,11,5,11,131,8,11,10,11,12,11,134,9,11,1,12,1,12,
        1,12,5,12,139,8,12,10,12,12,12,142,9,12,1,13,1,13,1,13,1,13,1,14,
        1,14,1,14,1,14,1,15,1,15,1,15,3,15,155,8,15,1,16,1,16,5,16,159,8,
        16,10,16,12,16,162,9,16,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,
        1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,22,3,22,
        184,8,22,1,23,1,23,1,24,1,24,1,24,0,0,25,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,0,4,1,0,19,23,1,0,24,
        28,1,0,37,38,2,0,16,16,31,35,181,0,54,1,0,0,0,2,56,1,0,0,0,4,74,
        1,0,0,0,6,86,1,0,0,0,8,95,1,0,0,0,10,103,1,0,0,0,12,106,1,0,0,0,
        14,109,1,0,0,0,16,112,1,0,0,0,18,115,1,0,0,0,20,125,1,0,0,0,22,127,
        1,0,0,0,24,135,1,0,0,0,26,143,1,0,0,0,28,147,1,0,0,0,30,154,1,0,
        0,0,32,156,1,0,0,0,34,163,1,0,0,0,36,169,1,0,0,0,38,171,1,0,0,0,
        40,176,1,0,0,0,42,178,1,0,0,0,44,180,1,0,0,0,46,185,1,0,0,0,48,187,
        1,0,0,0,50,55,3,2,1,0,51,55,3,4,2,0,52,55,3,6,3,0,53,55,3,8,4,0,
        54,50,1,0,0,0,54,51,1,0,0,0,54,52,1,0,0,0,54,53,1,0,0,0,55,1,1,0,
        0,0,56,57,5,1,0,0,57,58,3,18,9,0,58,59,5,2,0,0,59,61,3,32,16,0,60,
        62,3,10,5,0,61,60,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,65,3,12,
        6,0,64,63,1,0,0,0,64,65,1,0,0,0,65,67,1,0,0,0,66,68,3,14,7,0,67,
        66,1,0,0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,71,3,16,8,0,70,69,1,0,
        0,0,70,71,1,0,0,0,71,72,1,0,0,0,72,73,3,40,20,0,73,3,1,0,0,0,74,
        75,5,3,0,0,75,76,5,4,0,0,76,77,3,42,21,0,77,78,5,5,0,0,78,79,3,18,
        9,0,79,80,5,6,0,0,80,81,5,7,0,0,81,82,5,5,0,0,82,83,3,22,11,0,83,
        84,5,6,0,0,84,85,3,40,20,0,85,5,1,0,0,0,86,87,5,8,0,0,87,88,3,42,
        21,0,88,89,5,9,0,0,89,91,3,24,12,0,90,92,3,10,5,0,91,90,1,0,0,0,
        91,92,1,0,0,0,92,93,1,0,0,0,93,94,3,40,20,0,94,7,1,0,0,0,95,96,5,
        10,0,0,96,97,5,2,0,0,97,99,3,42,21,0,98,100,3,10,5,0,99,98,1,0,0,
        0,99,100,1,0,0,0,100,101,1,0,0,0,101,102,3,40,20,0,102,9,1,0,0,0,
        103,104,5,11,0,0,104,105,3,28,14,0,105,11,1,0,0,0,106,107,5,12,0,
        0,107,108,3,18,9,0,108,13,1,0,0,0,109,110,5,13,0,0,110,111,3,28,
        14,0,111,15,1,0,0,0,112,113,5,14,0,0,113,114,3,18,9,0,114,17,1,0,
        0,0,115,120,3,20,10,0,116,117,5,15,0,0,117,119,3,20,10,0,118,116,
        1,0,0,0,119,122,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,19,1,
        0,0,0,122,120,1,0,0,0,123,126,3,44,22,0,124,126,3,38,19,0,125,123,
        1,0,0,0,125,124,1,0,0,0,126,21,1,0,0,0,127,132,3,46,23,0,128,129,
        5,15,0,0,129,131,3,46,23,0,130,128,1,0,0,0,131,134,1,0,0,0,132,130,
        1,0,0,0,132,133,1,0,0,0,133,23,1,0,0,0,134,132,1,0,0,0,135,140,3,
        26,13,0,136,137,5,15,0,0,137,139,3,26,13,0,138,136,1,0,0,0,139,142,
        1,0,0,0,140,138,1,0,0,0,140,141,1,0,0,0,141,25,1,0,0,0,142,140,1,
        0,0,0,143,144,3,44,22,0,144,145,5,16,0,0,145,146,3,46,23,0,146,27,
        1,0,0,0,147,148,3,30,15,0,148,149,3,48,24,0,149,150,3,30,15,0,150,
        29,1,0,0,0,151,155,3,44,22,0,152,155,3,46,23,0,153,155,3,38,19,0,
        154,151,1,0,0,0,154,152,1,0,0,0,154,153,1,0,0,0,155,31,1,0,0,0,156,
        160,3,42,21,0,157,159,3,34,17,0,158,157,1,0,0,0,159,162,1,0,0,0,
        160,158,1,0,0,0,160,161,1,0,0,0,161,33,1,0,0,0,162,160,1,0,0,0,163,
        164,3,36,18,0,164,165,5,17,0,0,165,166,3,42,21,0,166,167,5,18,0,
        0,167,168,3,28,14,0,168,35,1,0,0,0,169,170,7,0,0,0,170,37,1,0,0,
        0,171,172,7,1,0,0,172,173,5,5,0,0,173,174,3,44,22,0,174,175,5,6,
        0,0,175,39,1,0,0,0,176,177,5,29,0,0,177,41,1,0,0,0,178,179,5,36,
        0,0,179,43,1,0,0,0,180,183,5,36,0,0,181,182,5,30,0,0,182,184,5,36,
        0,0,183,181,1,0,0,0,183,184,1,0,0,0,184,45,1,0,0,0,185,186,7,2,0,
        0,186,47,1,0,0,0,187,188,7,3,0,0,188,49,1,0,0,0,14,54,61,64,67,70,
        91,99,120,125,132,140,154,160,183
    ]

class PostgreSQLParser ( Parser ):

    grammarFileName = "PostgreSQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'SELECT'", "'FROM'", "'INSERT'", "'INTO'", 
                     "'('", "')'", "'VALUES'", "'UPDATE'", "'SET'", "'DELETE'", 
                     "'WHERE'", "'GROUP BY'", "'HAVING'", "'ORDER BY'", 
                     "','", "'='", "'JOIN'", "'ON'", "'INNER'", "'LEFT'", 
                     "'RIGHT'", "'FULL'", "'CROSS'", "'COUNT'", "'SUM'", 
                     "'AVG'", "'MIN'", "'MAX'", "';'", "'.'", "'!='", "'<'", 
                     "'<='", "'>'", "'>='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "IDENTIFIER", "STRING", "NUMBER", "WS" ]

    RULE_statement = 0
    RULE_selectStatement = 1
    RULE_insertStatement = 2
    RULE_updateStatement = 3
    RULE_deleteStatement = 4
    RULE_whereClause = 5
    RULE_groupByClause = 6
    RULE_havingClause = 7
    RULE_orderByClause = 8
    RULE_columnList = 9
    RULE_column = 10
    RULE_valueList = 11
    RULE_assignmentList = 12
    RULE_assignment = 13
    RULE_condition = 14
    RULE_expression = 15
    RULE_tableList = 16
    RULE_joinClause = 17
    RULE_joinType = 18
    RULE_aggregateFunction = 19
    RULE_semicolon = 20
    RULE_tableName = 21
    RULE_columnName = 22
    RULE_value = 23
    RULE_comparisonOperator = 24

    ruleNames =  [ "statement", "selectStatement", "insertStatement", "updateStatement", 
                   "deleteStatement", "whereClause", "groupByClause", "havingClause", 
                   "orderByClause", "columnList", "column", "valueList", 
                   "assignmentList", "assignment", "condition", "expression", 
                   "tableList", "joinClause", "joinType", "aggregateFunction", 
                   "semicolon", "tableName", "columnName", "value", "comparisonOperator" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    IDENTIFIER=36
    STRING=37
    NUMBER=38
    WS=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def selectStatement(self):
            return self.getTypedRuleContext(PostgreSQLParser.SelectStatementContext,0)


        def insertStatement(self):
            return self.getTypedRuleContext(PostgreSQLParser.InsertStatementContext,0)


        def updateStatement(self):
            return self.getTypedRuleContext(PostgreSQLParser.UpdateStatementContext,0)


        def deleteStatement(self):
            return self.getTypedRuleContext(PostgreSQLParser.DeleteStatementContext,0)


        def getRuleIndex(self):
            return PostgreSQLParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = PostgreSQLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_statement)
        try:
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.selectStatement()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.insertStatement()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.updateStatement()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 53
                self.deleteStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnList(self):
            return self.getTypedRuleContext(PostgreSQLParser.ColumnListContext,0)


        def tableList(self):
            return self.getTypedRuleContext(PostgreSQLParser.TableListContext,0)


        def semicolon(self):
            return self.getTypedRuleContext(PostgreSQLParser.SemicolonContext,0)


        def whereClause(self):
            return self.getTypedRuleContext(PostgreSQLParser.WhereClauseContext,0)


        def groupByClause(self):
            return self.getTypedRuleContext(PostgreSQLParser.GroupByClauseContext,0)


        def havingClause(self):
            return self.getTypedRuleContext(PostgreSQLParser.HavingClauseContext,0)


        def orderByClause(self):
            return self.getTypedRuleContext(PostgreSQLParser.OrderByClauseContext,0)


        def getRuleIndex(self):
            return PostgreSQLParser.RULE_selectStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectStatement" ):
                listener.enterSelectStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectStatement" ):
                listener.exitSelectStatement(self)




    def selectStatement(self):

        localctx = PostgreSQLParser.SelectStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_selectStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(PostgreSQLParser.T__0)
            self.state = 57
            self.columnList()
            self.state = 58
            self.match(PostgreSQLParser.T__1)
            self.state = 59
            self.tableList()
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 60
                self.whereClause()


            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 63
                self.groupByClause()


            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 66
                self.havingClause()


            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 69
                self.orderByClause()


            self.state = 72
            self.semicolon()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InsertStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tableName(self):
            return self.getTypedRuleContext(PostgreSQLParser.TableNameContext,0)


        def columnList(self):
            return self.getTypedRuleContext(PostgreSQLParser.ColumnListContext,0)


        def valueList(self):
            return self.getTypedRuleContext(PostgreSQLParser.ValueListContext,0)


        def semicolon(self):
            return self.getTypedRuleContext(PostgreSQLParser.SemicolonContext,0)


        def getRuleIndex(self):
            return PostgreSQLParser.RULE_insertStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsertStatement" ):
                listener.enterInsertStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsertStatement" ):
                listener.exitInsertStatement(self)




    def insertStatement(self):

        localctx = PostgreSQLParser.InsertStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_insertStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(PostgreSQLParser.T__2)
            self.state = 75
            self.match(PostgreSQLParser.T__3)
            self.state = 76
            self.tableName()
            self.state = 77
            self.match(PostgreSQLParser.T__4)
            self.state = 78
            self.columnList()
            self.state = 79
            self.match(PostgreSQLParser.T__5)
            self.state = 80
            self.match(PostgreSQLParser.T__6)
            self.state = 81
            self.match(PostgreSQLParser.T__4)
            self.state = 82
            self.valueList()
            self.state = 83
            self.match(PostgreSQLParser.T__5)
            self.state = 84
            self.semicolon()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tableName(self):
            return self.getTypedRuleContext(PostgreSQLParser.TableNameContext,0)


        def assignmentList(self):
            return self.getTypedRuleContext(PostgreSQLParser.AssignmentListContext,0)


        def semicolon(self):
            return self.getTypedRuleContext(PostgreSQLParser.SemicolonContext,0)


        def whereClause(self):
            return self.getTypedRuleContext(PostgreSQLParser.WhereClauseContext,0)


        def getRuleIndex(self):
            return PostgreSQLParser.RULE_updateStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpdateStatement" ):
                listener.enterUpdateStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpdateStatement" ):
                listener.exitUpdateStatement(self)




    def updateStatement(self):

        localctx = PostgreSQLParser.UpdateStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_updateStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(PostgreSQLParser.T__7)
            self.state = 87
            self.tableName()
            self.state = 88
            self.match(PostgreSQLParser.T__8)
            self.state = 89
            self.assignmentList()
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 90
                self.whereClause()


            self.state = 93
            self.semicolon()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeleteStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tableName(self):
            return self.getTypedRuleContext(PostgreSQLParser.TableNameContext,0)


        def semicolon(self):
            return self.getTypedRuleContext(PostgreSQLParser.SemicolonContext,0)


        def whereClause(self):
            return self.getTypedRuleContext(PostgreSQLParser.WhereClauseContext,0)


        def getRuleIndex(self):
            return PostgreSQLParser.RULE_deleteStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeleteStatement" ):
                listener.enterDeleteStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeleteStatement" ):
                listener.exitDeleteStatement(self)




    def deleteStatement(self):

        localctx = PostgreSQLParser.DeleteStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_deleteStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(PostgreSQLParser.T__9)
            self.state = 96
            self.match(PostgreSQLParser.T__1)
            self.state = 97
            self.tableName()
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 98
                self.whereClause()


            self.state = 101
            self.semicolon()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhereClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(PostgreSQLParser.ConditionContext,0)


        def getRuleIndex(self):
            return PostgreSQLParser.RULE_whereClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhereClause" ):
                listener.enterWhereClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhereClause" ):
                listener.exitWhereClause(self)




    def whereClause(self):

        localctx = PostgreSQLParser.WhereClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_whereClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(PostgreSQLParser.T__10)
            self.state = 104
            self.condition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GroupByClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnList(self):
            return self.getTypedRuleContext(PostgreSQLParser.ColumnListContext,0)


        def getRuleIndex(self):
            return PostgreSQLParser.RULE_groupByClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroupByClause" ):
                listener.enterGroupByClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroupByClause" ):
                listener.exitGroupByClause(self)




    def groupByClause(self):

        localctx = PostgreSQLParser.GroupByClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_groupByClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(PostgreSQLParser.T__11)
            self.state = 107
            self.columnList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HavingClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(PostgreSQLParser.ConditionContext,0)


        def getRuleIndex(self):
            return PostgreSQLParser.RULE_havingClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHavingClause" ):
                listener.enterHavingClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHavingClause" ):
                listener.exitHavingClause(self)




    def havingClause(self):

        localctx = PostgreSQLParser.HavingClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_havingClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(PostgreSQLParser.T__12)
            self.state = 110
            self.condition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderByClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnList(self):
            return self.getTypedRuleContext(PostgreSQLParser.ColumnListContext,0)


        def getRuleIndex(self):
            return PostgreSQLParser.RULE_orderByClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrderByClause" ):
                listener.enterOrderByClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrderByClause" ):
                listener.exitOrderByClause(self)




    def orderByClause(self):

        localctx = PostgreSQLParser.OrderByClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_orderByClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(PostgreSQLParser.T__13)
            self.state = 113
            self.columnList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PostgreSQLParser.ColumnContext)
            else:
                return self.getTypedRuleContext(PostgreSQLParser.ColumnContext,i)


        def getRuleIndex(self):
            return PostgreSQLParser.RULE_columnList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnList" ):
                listener.enterColumnList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnList" ):
                listener.exitColumnList(self)




    def columnList(self):

        localctx = PostgreSQLParser.ColumnListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_columnList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.column()
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 116
                self.match(PostgreSQLParser.T__14)
                self.state = 117
                self.column()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnName(self):
            return self.getTypedRuleContext(PostgreSQLParser.ColumnNameContext,0)


        def aggregateFunction(self):
            return self.getTypedRuleContext(PostgreSQLParser.AggregateFunctionContext,0)


        def getRuleIndex(self):
            return PostgreSQLParser.RULE_column

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn" ):
                listener.enterColumn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn" ):
                listener.exitColumn(self)




    def column(self):

        localctx = PostgreSQLParser.ColumnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_column)
        try:
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.columnName()
                pass
            elif token in [24, 25, 26, 27, 28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.aggregateFunction()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PostgreSQLParser.ValueContext)
            else:
                return self.getTypedRuleContext(PostgreSQLParser.ValueContext,i)


        def getRuleIndex(self):
            return PostgreSQLParser.RULE_valueList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValueList" ):
                listener.enterValueList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValueList" ):
                listener.exitValueList(self)




    def valueList(self):

        localctx = PostgreSQLParser.ValueListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_valueList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.value()
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 128
                self.match(PostgreSQLParser.T__14)
                self.state = 129
                self.value()
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PostgreSQLParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(PostgreSQLParser.AssignmentContext,i)


        def getRuleIndex(self):
            return PostgreSQLParser.RULE_assignmentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentList" ):
                listener.enterAssignmentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentList" ):
                listener.exitAssignmentList(self)




    def assignmentList(self):

        localctx = PostgreSQLParser.AssignmentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_assignmentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.assignment()
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 136
                self.match(PostgreSQLParser.T__14)
                self.state = 137
                self.assignment()
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnName(self):
            return self.getTypedRuleContext(PostgreSQLParser.ColumnNameContext,0)


        def value(self):
            return self.getTypedRuleContext(PostgreSQLParser.ValueContext,0)


        def getRuleIndex(self):
            return PostgreSQLParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = PostgreSQLParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.columnName()
            self.state = 144
            self.match(PostgreSQLParser.T__15)
            self.state = 145
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PostgreSQLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PostgreSQLParser.ExpressionContext,i)


        def comparisonOperator(self):
            return self.getTypedRuleContext(PostgreSQLParser.ComparisonOperatorContext,0)


        def getRuleIndex(self):
            return PostgreSQLParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = PostgreSQLParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.expression()
            self.state = 148
            self.comparisonOperator()
            self.state = 149
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnName(self):
            return self.getTypedRuleContext(PostgreSQLParser.ColumnNameContext,0)


        def value(self):
            return self.getTypedRuleContext(PostgreSQLParser.ValueContext,0)


        def aggregateFunction(self):
            return self.getTypedRuleContext(PostgreSQLParser.AggregateFunctionContext,0)


        def getRuleIndex(self):
            return PostgreSQLParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = PostgreSQLParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expression)
        try:
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.columnName()
                pass
            elif token in [37, 38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.value()
                pass
            elif token in [24, 25, 26, 27, 28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 153
                self.aggregateFunction()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tableName(self):
            return self.getTypedRuleContext(PostgreSQLParser.TableNameContext,0)


        def joinClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PostgreSQLParser.JoinClauseContext)
            else:
                return self.getTypedRuleContext(PostgreSQLParser.JoinClauseContext,i)


        def getRuleIndex(self):
            return PostgreSQLParser.RULE_tableList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableList" ):
                listener.enterTableList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableList" ):
                listener.exitTableList(self)




    def tableList(self):

        localctx = PostgreSQLParser.TableListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_tableList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.tableName()
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16252928) != 0):
                self.state = 157
                self.joinClause()
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JoinClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def joinType(self):
            return self.getTypedRuleContext(PostgreSQLParser.JoinTypeContext,0)


        def tableName(self):
            return self.getTypedRuleContext(PostgreSQLParser.TableNameContext,0)


        def condition(self):
            return self.getTypedRuleContext(PostgreSQLParser.ConditionContext,0)


        def getRuleIndex(self):
            return PostgreSQLParser.RULE_joinClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoinClause" ):
                listener.enterJoinClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoinClause" ):
                listener.exitJoinClause(self)




    def joinClause(self):

        localctx = PostgreSQLParser.JoinClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_joinClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.joinType()
            self.state = 164
            self.match(PostgreSQLParser.T__16)
            self.state = 165
            self.tableName()
            self.state = 166
            self.match(PostgreSQLParser.T__17)
            self.state = 167
            self.condition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JoinTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PostgreSQLParser.RULE_joinType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoinType" ):
                listener.enterJoinType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoinType" ):
                listener.exitJoinType(self)




    def joinType(self):

        localctx = PostgreSQLParser.JoinTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_joinType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16252928) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregateFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnName(self):
            return self.getTypedRuleContext(PostgreSQLParser.ColumnNameContext,0)


        def getRuleIndex(self):
            return PostgreSQLParser.RULE_aggregateFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregateFunction" ):
                listener.enterAggregateFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregateFunction" ):
                listener.exitAggregateFunction(self)




    def aggregateFunction(self):

        localctx = PostgreSQLParser.AggregateFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_aggregateFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 520093696) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 172
            self.match(PostgreSQLParser.T__4)
            self.state = 173
            self.columnName()
            self.state = 174
            self.match(PostgreSQLParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SemicolonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PostgreSQLParser.RULE_semicolon

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSemicolon" ):
                listener.enterSemicolon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSemicolon" ):
                listener.exitSemicolon(self)




    def semicolon(self):

        localctx = PostgreSQLParser.SemicolonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_semicolon)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(PostgreSQLParser.T__28)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PostgreSQLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return PostgreSQLParser.RULE_tableName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableName" ):
                listener.enterTableName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableName" ):
                listener.exitTableName(self)




    def tableName(self):

        localctx = PostgreSQLParser.TableNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_tableName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(PostgreSQLParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(PostgreSQLParser.IDENTIFIER)
            else:
                return self.getToken(PostgreSQLParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return PostgreSQLParser.RULE_columnName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnName" ):
                listener.enterColumnName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnName" ):
                listener.exitColumnName(self)




    def columnName(self):

        localctx = PostgreSQLParser.ColumnNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_columnName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(PostgreSQLParser.IDENTIFIER)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 181
                self.match(PostgreSQLParser.T__29)
                self.state = 182
                self.match(PostgreSQLParser.IDENTIFIER)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(PostgreSQLParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(PostgreSQLParser.NUMBER, 0)

        def getRuleIndex(self):
            return PostgreSQLParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = PostgreSQLParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            _la = self._input.LA(1)
            if not(_la==37 or _la==38):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PostgreSQLParser.RULE_comparisonOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOperator" ):
                listener.enterComparisonOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOperator" ):
                listener.exitComparisonOperator(self)




    def comparisonOperator(self):

        localctx = PostgreSQLParser.ComparisonOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_comparisonOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66572058624) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





