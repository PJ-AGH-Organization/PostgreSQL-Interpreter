grammar PostgreSQL;

statement: selectStatement | insertStatement | updateStatement | deleteStatement;

selectStatement: 'SELECT' columnList 'FROM' tableList whereClause? groupByClause? havingClause? orderByClause? semicolon;
insertStatement: 'INSERT' 'INTO' tableName '(' columnList ')' 'VALUES' '(' valueList ')' semicolon;
updateStatement: 'UPDATE' tableName 'SET' assignmentList whereClause? semicolon;
deleteStatement: 'DELETE' 'FROM' tableName whereClause? semicolon;

whereClause: 'WHERE' condition;
groupByClause: 'GROUP BY' columnList;
havingClause: 'HAVING' condition;
orderByClause: 'ORDER BY' columnList;

columnList: column (',' column)*;
column: columnName | aggregateFunction;
valueList: value (',' value)*;
assignmentList: assignment (',' assignment)*;
assignment: columnName '=' value;
condition: expression comparisonOperator expression;
expression: columnName | value | aggregateFunction;

tableList: tableName (joinClause)*;
joinClause: joinType 'JOIN' tableName 'ON' condition;
joinType: 'INNER' | 'LEFT' | 'RIGHT' | 'FULL' | 'CROSS';

aggregateFunction: ('COUNT' | 'SUM' | 'AVG' | 'MIN' | 'MAX') '(' columnName ')';

semicolon: ';';

tableName: IDENTIFIER;
columnName: IDENTIFIER ('.' IDENTIFIER)?;
value: STRING | NUMBER;
comparisonOperator: '=' | '!=' | '<' | '<=' | '>' | '>=';

IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
STRING: '\'' .*? '\'';
NUMBER: [0-9]+;
WS: [ \t\r\n]+ -> skip;
