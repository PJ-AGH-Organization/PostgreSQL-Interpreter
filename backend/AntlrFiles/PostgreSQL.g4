grammar PostgreSQL;

statements
    : (statement semicolon)* EOF
    ;

statement
    : selectStatement
    | insertStatement
    | updateStatement
    | deleteStatement
    | createTableStatement
    | alterTableStatement
    | dropTableStatement
    ;

selectStatement
    : 'SELECT' columnList 'FROM' tableList whereClause? groupByClause? havingClause? orderByClause?
    ;

insertStatement
    : 'INSERT' 'INTO' tableName '(' columnList ')' 'VALUES' '(' valueList ')'
    ;

updateStatement
    : 'UPDATE' tableName 'SET' assignmentList whereClause?
    ;

deleteStatement
    : 'DELETE' 'FROM' tableName whereClause?
    ;

createTableStatement
    : 'CREATE' 'TABLE' tableName '(' columnDef (',' columnDef)* (',' tableConstraint)* ')'
    ;

alterTableStatement
    : 'ALTER' 'TABLE' tableName alterAction
    ;

alterAction
    : 'ADD' columnDef
    | 'ADD' tableConstraint
    | 'DROP' 'COLUMN' columnName
    | 'ALTER' 'COLUMN' columnName alterColumnAction
    ;

alterColumnAction
    : 'SET' 'DEFAULT' value
    | 'DROP' 'DEFAULT'
    | 'SET' 'NOT' 'NULL'
    | 'DROP' 'NOT' 'NULL'
    ;

dropTableStatement
    : 'DROP' 'TABLE' tableName
    ;

columnDef
    : columnName dataType columnConstraint*
    ;

tableConstraint
    : 'PRIMARY' 'KEY' '(' columnName (',' columnName)* ')'
    | 'UNIQUE' '(' columnName (',' columnName)* ')'
    | 'FOREIGN' 'KEY' '(' columnName ')' 'REFERENCES' tableName '(' columnName ')'
    ;

columnConstraint
    : 'PRIMARY' 'KEY'
    | 'NOT' 'NULL'
    | 'UNIQUE'
    | 'DEFAULT' value
    ;

dataType
    : 'INT'
    | 'INTEGER'
    | 'TEXT'
    | 'VARCHAR' '(' NUMBER ')'
    | 'BOOLEAN'
    | 'DATE'
    | 'FLOAT'
    ;

whereClause: 'WHERE' condition;
groupByClause: 'GROUP BY' columnList;
havingClause: 'HAVING' condition;
orderByClause: 'ORDER BY' columnList;

columnList
    : STAR
    | column (',' column)*
    ;

column
    : columnName
    | aggregateFunction
    ;

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
value: STRING | NUMBER | 'TRUE' | 'FALSE' | 'NULL';
comparisonOperator: '=' | '!=' | '<' | '<=' | '>' | '>=';

IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
STRING: '\'' .*? '\'';
NUMBER: [0-9]+;
WS: [ \t\r\n]+ -> skip;
STAR: '*';
