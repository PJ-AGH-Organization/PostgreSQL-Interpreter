grammar PostgreSQL;

statements
    : (statement SEMICOLON)+ EOF
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
    : SELECT columnList FROM tableList whereClause? groupByClause? havingClause? limitClause?
    ;

insertStatement
    : INSERT INTO tableName '(' columnList ')' VALUES '(' valueList ')'
    ;

updateStatement
    : UPDATE tableName SET assignmentList whereClause?
    ;

deleteStatement
    : DELETE FROM tableName whereClause?
    ;

createTableStatement
    : CREATE TABLE tableName '(' columnDef (',' columnDef)* (',' tableConstraint)* ')'
    ;

alterTableStatement
    : ALTER TABLE tableName alterAction
    ;

alterAction
    : ADD columnDef
    | ADD tableConstraint
    | DROP COLUMN columnName
    | ALTER COLUMN columnName alterColumnAction
    ;

alterColumnAction
    : SET DEFAULT value
    | DROP DEFAULT
    | SET NOT NULL
    | DROP NOT NULL
    ;

dropTableStatement
    : DROP TABLE tableName
    ;

columnDef
    : columnName dataType columnConstraint*
    ;

tableConstraint
    : PRIMARY KEY '(' columnName (',' columnName)* ')'
    | UNIQUE '(' columnName (',' columnName)* ')'
    | FOREIGN KEY '(' columnName ')' REFERENCES tableName '(' columnName ')'
    ;

columnConstraint
    : PRIMARY KEY
    | NOT NULL
    | UNIQUE
    | DEFAULT value
    ;

dataType
    : INT
    | INTEGER
    | TEXT
    | VARCHAR '(' NUMBER ')'
    | BOOLEAN
    | DATE
    | FLOAT
    ;

whereClause: WHERE condition;
groupByClause: GROUP BY columnList;
havingClause: HAVING condition;
limitClause: LIMIT NUMBER;

columnList
    : STAR
    | column (',' column)*
    ;

column
    : (columnName
    | aggregateFunction
    | countFunction) (AS? columnAliasName)?
    ;

valueList: value (',' value)*;
assignmentList: assignment (',' assignment)*;
assignment: columnName '=' value;
condition: expression comparisonOperator expression;
expression: columnName | value | aggregateFunction;

tableList: tableWithAlias (joinClause)*;

tableWithAlias: tableName (AS? tableAliasName)?;

joinClause: joinType? JOIN tableWithAlias joinCondition;

joinType: INNER | LEFT | RIGHT;

joinCondition
    : ON '(' condition ')'
    | USING '(' columnName (',' columnName)* ')'
    ;

aggregateFunction: (SUM | AVG | MIN | MAX) '(' columnName ')';

countFunction: COUNT '(' (columnName | STAR) ')';

tableName: IDENTIFIER;
tableAliasName: IDENTIFIER;
columnAliasName: IDENTIFIER;
columnName: IDENTIFIER ('.' IDENTIFIER)?;
value: STRING | NUMBER | TRUE | FALSE | NULL;
comparisonOperator: '=' | '!=' | '<' | '<=' | '>' | '>=';

SEMICOLON: ';';
STAR: '*';
SELECT: [sS][eE][lL][eE][cC][tT];
FROM: [fF][rR][oO][mM];
JOIN: [jJ][oO][iI][nN];
ON: [oO][nN];
USING: [uU][sS][iI][nN][gG];
WHERE: [wW][hH][eE][rR][eE];
GROUP: [gG][rR][oO][uU][pP];
BY: [bB][yY];
HAVING: [hH][aA][vV][iI][nN][gG];
ORDER: [oO][rR][dD][eE][rR];
LIMIT: [lL][iI][mM][iI][tT];
INSERT: [iI][nN][sS][eE][rR][tT];
INTO: [iI][nN][tT][oO];
VALUES: [vV][aA][lL][uU][eE][sS];
UPDATE: [uU][pP][dD][aA][tT][eE];
SET: [sS][eE][tT];
DELETE: [dD][eE][lL][eE][tT][eE];
CREATE: [cC][rR][eE][aA][tT][eE];
TABLE: [tT][aA][bB][lL][eE];
ALTER: [aA][lL][tT][eE][rR];
ADD: [aA][dD][dD];
DROP: [dD][rR][oO][pP];
COLUMN: [cC][oO][lL][uU][mM][nN];
NOT: [nN][oO][tT];
NULL: [nN][uU][lL][lL];
PRIMARY: [pP][rR][iI][mM][aA][rR][yY];
KEY: [kK][eE][yY];
UNIQUE: [uU][nN][iI][qQ][uU][eE];
FOREIGN: [fF][oO][rR][eE][iI][gG][nN];
REFERENCES: [rR][eE][fF][eE][rR][eE][nN][cC][eE][sS];
DEFAULT: [dD][eE][fF][aA][uU][lL][tT];
INT: [iI][nN][tT];
INTEGER: [iI][nN][tT][eE][gG][eE][rR];
TEXT: [tT][eE][xX][tT];
VARCHAR: [vV][aA][rR][cC][hH][aA][rR];
BOOLEAN: [bB][oO][oO][lL][eE][aA][nN];
DATE: [dD][aA][tT][eE];
FLOAT: [fF][lL][oO][aA][tT];
TRUE: [tT][rR][uU][eE];
FALSE: [fF][aA][lL][sS][eE];
COUNT: [cC][oO][uU][nN][tT];
SUM: [sS][uU][mM];
AVG: [aA][vV][gG];
MIN: [mM][iI][nN];
MAX: [mM][aA][xX];
INNER: [iI][nN][nN][eE][rR];
LEFT: [lL][eE][fF][tT];
RIGHT: [rR][iI][gG][hH][tT];
FULL: [fF][uU][lL][lL];
CROSS: [cC][rR][oO][sS][sS];
AS: [aA][sS];

IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
STRING: '\'' ( ~('\'' | '\\') | '\\' . )* '\'';
NUMBER: [0-9]+ ('.' [0-9]+)?;
WS: [ \t\r\n]+ -> skip;
