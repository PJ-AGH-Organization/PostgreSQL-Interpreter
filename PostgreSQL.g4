grammar PostgreSQL;


statement: selectStatement | insertStatement | updateStatement | deleteStatement;

selectStatement: 'SELECT' columnList 'FROM' tableList whereClause? groupByClause? havingClause? orderByClause?;
insertStatement: 'INSERT' 'INTO' tableName '(' columnList ')' 'VALUES' '(' valueList ')';
updateStatement: 'UPDATE' tableName 'SET' assignmentList whereClause?;
deleteStatement: 'DELETE' 'FROM' tableName whereClause?;

whereClause: 'WHERE' condition;
groupByClause: 'GROUP BY' columnList;
havingClause: 'HAVING' condition;
orderByClause: 'ORDER BY' columnList;

columnList: column (',' column)*;
column: columnName | aggregateFunction | windowFunction;
valueList: value (',' value)*;
assignmentList: assignment (',' assignment)*;
assignment: columnName '=' value;
condition: expression comparisonOperator expression;
expression: columnName | value | aggregateFunction;

tableList: tableName (joinClause)*;
joinClause: joinType 'JOIN' tableName 'ON' condition;
joinType: 'INNER' | 'LEFT' | 'RIGHT' | 'FULL' | 'CROSS';

aggregateFunction: ('COUNT' | 'SUM' | 'AVG' | 'MIN' | 'MAX') '(' columnName ')';
windowFunction: ('ROW_NUMBER' | 'RANK' | 'DENSE_RANK' | 'NTILE' | 'LEAD' | 'LAG') '(' ')' 'OVER' '(' partitionByClause? orderByClause? ')';
partitionByClause: 'PARTITION BY' columnList;


tableName: IDENTIFIER;
columnName: IDENTIFIER ('.' IDENTIFIER)?;
value: STRING | NUMBER;
comparisonOperator: '=' | '!=' | '<' | '<=' | '>' | '>=';

IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
STRING: '\'' .*? '\'';
NUMBER: [0-9]+;
WS: [ \t\r\n]+ -> skip;
