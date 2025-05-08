# PostgreSQL Interpreter

## Dane studenta(-ów):

*   Jan Banasik
*   Patrick Bajorski

## Dane kontaktowe:

*   jbanasik@student.agh.edu.pl
*   pbajorski@student.agh.edu.pl

## Założenia programu

**Ogólne cele programu:**

Głównym celem projektu jest stworzenie interpretera zapytań SQL, wzorowanego na składni stosowanej w systemie bazodanowym PostgreSQL. Program działa jako **serwis webowy (API REST)**, który przyjmuje zapytania SQL, przeprowadza ich analizę leksykalną i składniową przy użyciu generatora parserów ANTLR, dokonuje podstawowej walidacji struktury (istnienia tabel, kolumn), a następnie **deleguje wykonanie zapytania do silnika bazy danych SQLite**. Projekt skupia się na prawidłowym parsowaniu i zrozumieniu struktury zapytania, a także prezentacji drzewa parsowania, wykorzystując zewnętrzny silnik do faktycznej manipulacji danymi.

**Rodzaj translatora:**

Projekt implementuje **interpreter**, wykorzystujący **silnik bazy danych SQLite** jako backend wykonawczy.

**Wynik działania programu:**

Program działa jako serwis webowy oparty o framework FastAPI. Udostępnia endpoint HTTP POST, który przyjmuje tekst zapytania(ń) SQL (jedno lub wiele, oddzielonych średnikami). W odpowiedzi, serwis zwraca obiekt w formacie JSON, zawierający:

*   Dla każdego przetworzonego zapytania (lub ogólnie dla błędu składniowego):
    *   Sformatowane drzewo parsowania (parse tree), prezentujące strukturę składniową zapytania (dla każdego zapytania, jeśli parsowanie się powiodło).
    *   Wynik wykonania zapytania przez silnik SQLite (np. dane w formie listy obiektów dla `SELECT`, komunikat o sukcesie dla DDL/DML, lub komunikat o błędzie wykonania/walidacji struktury).
    *   Ewentualne błędy składniowe (wykryte przez parser ANTLR) lub błędy walidacji struktury (np. odwołanie do nieistniejącej tabeli/kolumny), które przerywają przetwarzanie dalszych zapytań w ramach tego samego żądania.

Dane bazodanowe, na których operuje interpreter, są inicjowane podczas startu aplikacji poprzez załadowanie danych z plików CSV z katalogu `resources/` do tymczasowej bazy danych SQLite w pliku `database/sample_database.db`.

**Język implementacji:**

Projekt jest implementowany w języku **Python 3**.

**Sposób realizacji skanera/parsera:**

Skaner (fazę leksykalną) i parser (fazę składniową) zrealizowano przy użyciu **generatora parserów ANTLR 4**. Gramatyka języka wejściowego (podzbioru SQL, wzorowanego na PostgreSQL) została zdefiniowana w pliku `PostgreSQL.g4`. ANTLR został użyty do wygenerowania kodu źródłowego w języku Python (pliki w `backend/AntlrFiles/`), odpowiedzialnego za analizę leksykalną i składniową.

## Opis tokenów

Poniżej przedstawiono reguły leksykalne definiujące tokeny rozpoznawane przez skaner, w notacji generatora ANTLR 4 (zawartość sekcji lexera z pliku `PostgreSQL.g4`):

```antlr
grammar PostgreSQL;

statements
    : (statement)+ EOF
    ;

statement
    : selectStatement SEMICOLON
    | insertStatement SEMICOLON
    | updateStatement SEMICOLON
    | deleteStatement SEMICOLON
    | createTableStatement SEMICOLON
    | alterTableStatement SEMICOLON
    | dropTableStatement SEMICOLON
    ;

selectStatement
    : SELECT columnList FROM tableList whereClause? groupByClause? havingClause? orderClause? limitClause?
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

whereClause
    : WHERE standardCondition
    ;

groupByClause
    : GROUP BY columnList
    ;

havingClause
    : HAVING havingCondition
    ;

limitClause
    : LIMIT NUMBER
    ;

orderClause
    : ORDER BY orderExpression (',' orderExpression)*
    ;

orderExpression
    : (NUMBER | columnName) sortingOperator?
    ;

sortingOperator
    : ASC
    | DESC
    ;

columnList
    : STAR
    | columnExpression (',' columnExpression)*
    ;

column
    : columnName
    | aggregateFunction
    | countFunction
    ;

columnExpression
    : (column | NUMBER) (mathOperator (column | NUMBER))* (AS? columnAliasName)?
    ;

valueList
    : value (',' value)*
    ;

assignmentList
    : assignment (',' assignment)*
    ;

assignment
    : columnName '=' value
    ;

standardCondition
    : whereExpression comparisonOperator whereExpression
    ;

havingCondition
    : havingExpression comparisonOperator havingExpression
    ;

whereExpression
    : columnName
    | value
    ;

havingExpression
    : columnName
    | value
    | aggregateFunction
    | countFunction
    ;

tableList
    : tableWithAlias (joinClause)*
    ;

tableWithAlias
    : tableName (AS? tableAliasName)?
    ;

joinClause
    : joinType? JOIN tableWithAlias joinCondition
    ;

joinType
    : INNER
    | LEFT
    | RIGHT
    ;

joinCondition
    : ON '(' standardCondition ')'
    | USING '(' columnName (',' columnName)* ')'
    ;

aggregateFunction
    : (SUM | AVG | MIN | MAX) '(' columnName (mathOperator columnName)* ')'
    ;

countFunction
    : COUNT '(' (columnName | STAR) ')'
    ;

tableName
    : IDENTIFIER
    ;

tableAliasName
    : IDENTIFIER
    ;

columnAliasName
    : STRING
    | IDENTIFIER
    ;

columnName
    : IDENTIFIER ('.' IDENTIFIER)?
    ;

value
    : STRING
    | NUMBER
    | TRUE
    | FALSE
    | NULL
    ;

comparisonOperator
    : '='
    | '!='
    | '<'
    | '<='
    | '>'
    | '>='
    ;

mathOperator
    : '+'
    | '-'
    | '*'
    | '/'
    ;

SEMICOLON
    : ';'
    ;

STAR
    : '*'
    ;

SELECT
    : [sS][eE][lL][eE][cC][tT]
    ;

FROM
    : [fF][rR][oO][mM]
    ;

JOIN
    : [jJ][oO][iI][nN]
    ;

ON
    : [oO][nN]
    ;

USING
    : [uU][sS][iI][nN][gG]
    ;

WHERE
    : [wW][hH][eE][rR][eE]
    ;

GROUP
    : [gG][rR][oO][uU][pP]
    ;

BY
    : [bB][yY]
    ;

HAVING
    : [hH][aA][vV][iI][nN][gG]
    ;

ORDER
    : [oO][rR][dD][eE][rR]
    ;

LIMIT
    : [lL][iI][mM][iI][tT]
    ;

INSERT
    : [iI][nN][sS][eE][rR][tT]
    ;

INTO
    : [iI][nN][tT][oO]
    ;

VALUES
    : [vV][aA][lL][uU][eE][sS]
    ;

UPDATE
    : [uU][pP][dD][aA][tT][eE]
    ;

SET
    : [sS][eE][tT]
    ;

DELETE
    : [dD][eE][lL][eE][tT][eE]
    ;

CREATE
    : [cC][rR][eE][aA][tT][eE]
    ;

TABLE
    : [tT][aA][bB][lL][eE]
    ;

ALTER
    : [aA][lL][tT][eE][rR]
    ;

ADD
    : [aA][dD][dD]
    ;

DROP
    : [dD][rR][oO][pP]
    ;

COLUMN
    : [cC][oO][lL][uU][mM][nN]
    ;

NOT
    : [nN][oO][tT]
    ;

NULL
    : [nN][uU][lL][lL]
    ;

PRIMARY
    : [pP][rR][iI][mM][aA][rR][yY]
    ;

KEY
    : [kK][eE][yY]
    ;

UNIQUE
    : [uU][nN][iI][qQ][uU][eE]
    ;

FOREIGN
    : [fF][oO][rR][eE][iI][gG][nN]
    ;

REFERENCES
    : [rR][eE][fF][eE][rR][eE][nN][cC][eE][sS]
    ;

DEFAULT
    : [dD][eE][fF][aA][uU][lL][tT]
    ;

INT
    : [iI][nN][tT]
    ;

INTEGER
    : [iI][nN][tT][eE][gG][eE][rR]
    ;

TEXT
    : [tT][eE][xX][tT]
    ;

VARCHAR
    : [vV][aA][rR][cC][hH][aA][rR]
    ;

BOOLEAN
    : [bB][oO][oO][lL][eE][aA][nN]
    ;

DATE
    : [dD][aA][tT][eE]
    ;

FLOAT
    : [fF][lL][oO][aA][tT]
    ;

TRUE
    : [tT][rR][uU][eE]
    ;

FALSE
    : [fF][aA][lL][sS][eE]
    ;

COUNT
    : [cC][oO][uU][nN][tT]
    ;

SUM
    : [sS][uU][mM]
    ;

AVG
    : [aA][vV][gG]
    ;

MIN
    : [mM][iI][nN]
    ;

MAX
    : [mM][aA][xX]
    ;

INNER
    : [iI][nN][nN][eE][rR]
    ;

LEFT
    : [lL][eE][fF][tT]
    ;

RIGHT
    : [rR][iI][gG][hH][tT]
    ;

FULL
    : [fF][uU][lL][lL]
    ;

CROSS
    : [cC][rR][oO][sS][sS]
    ;

ASC
    : [aA][sS][cC]
    ;

DESC
    : [dD][eE][sS][cC]
    ;

AS
    : [aA][sS]
    ;

IDENTIFIER
    : [a-zA-Z_][a-zA-Z_0-9]*
    ;

STRING
    : '\'' ( ~('\'' | '\\') | '\\' . )* '\''
    ;

NUMBER
    : [0-9]+ ('.' [0-9]+)?
    ;

WS
    : [ \t\r\n]+ -> skip
    ;

```

## Informacje o stosowanych generatorach skanerów/parserów, pakietach zewnętrznych

*   **Generator Skanera/Parsera:** ANTLR 4 (The ANTLR Parser Generator), wersja `~=4.13.2` (zgodnie z `requirements.txt`). Plik gramatyki (`PostgreSQL.g4`) znajduje się w katalogu `backend/AntlrFiles/`. Użyto targetu Python 3 do wygenerowania kodu parsowania (pliki takie jak `PostgreSQLLexer.py`, `PostgreSQLParser.py` w `backend/AntlrFiles/`).
*   **Narzędzia:** Do wygenerowania kodu parsera/skanera z pliku `.g4` użyto narzędzia `antlr4` (dostępnego po instalacji `antlr4-tools`).
*   **Pakiety zewnętrzne (zależności Python):**
    *   `antlr4-python3-runtime`: Biblioteka uruchomieniowa dla ANTLR w Pythonie.
    *   `antlr4-tools`: Narzędzia do generowania kodu z gramatyk ANTLR.
    *   `fastapi`: Framework do szybkiego tworzenia API webowych.
    *   `uvicorn`: Szybki serwer ASGI do uruchamiania aplikacji FastAPI.
    *   `pydantic`: Biblioteka do walidacji danych, często używana z FastAPI (widoczna w `requirements.txt`).
    *   `pytest`: Framework do pisania i uruchamiania testów (widoczny w `requirements.txt`, sugeruje istnienie testów jednostkowych/integracyjnych).
    *   `pandas`: Używany do wstępnego ładowania danych z plików CSV do bazy SQLite.
    *   `fastapi-utils`: Dodatkowe narzędzia dla FastAPI (np. `@cbv`).
    *   `typing-inspect`: Narzędzie do introspekcji typów (widoczne w `requirements.txt`).
    *   `sqlite3`: Standardowa biblioteka Pythona, używana jako silnik bazy danych do wykonywania zapytań.
*   **Zarządzanie zależnościami:** Pakiety są zarządzane przy użyciu `pip`. Wszystkie niezbędne zależności znajdują się w pliku `requirements.txt`.

## Krótka instrukcja obsługi

1.  **Upewnij się, że masz zainstalowany Python 3.x oraz narzędzie `pip`.**
2.  **Sklonuj repozytorium:**
    ```bash
    git clone https://github.com/PJ-AGH-Organization/PostgreSQL-Interpreter.git
    cd PostgreSQL-Interpreter
    ```
3.  **Zainstaluj zależności Python:**
    ```bash
    pip install -r requirements.txt
    ```
    To zainstaluje wszystkie wymagane pakiety, w tym runtime ANTLR oraz narzędzia do generowania parsera (`antlr4-tools`).
4.  **Wygeneruj kod parsera/skanera (jeśli nie jest już obecny w repozytorium lub wymaga odświeżenia):**
    *(Uwaga: Pliki wygenerowane przez ANTLR są często dołączane do repozytorium. Ten krok jest potrzebny tylko wtedy, gdy ich brakuje lub gramatyka została zmieniona.)*
    ```bash
    python -m antlr4 -Dlanguage=Python3 backend/AntlrFiles/PostgreSQL.g4 -visitor -listener -o backend/AntlrFiles
    ```
    To polecenie uruchomi generator ANTLR, używając zainstalowanego pakietu `antlr4-tools` (stąd `python -m antlr4`), wskaże język docelowy Python3, poda plik gramatyki (`backend/AntlrFiles/PostgreSQL.g4`), włączy generowanie Listenerów i Visitorów (`-visitor -listener`) oraz określi katalog wyjściowy na `backend/AntlrFiles`.
5.  **Uruchom aplikację FastAPI:**
    ```bash
    uvicorn SQLInterpreter:app --reload
    ```
    Aplikacja zostanie uruchomiona domyślnie na adresie `http://127.0.0.1:8000/`. Opcja `--reload` przydatna podczas developmentu, powoduje automatyczne przeładowanie serwera po zmianach w kodzie.
6.  **Inicjalizacja bazy danych:** Mechanizm `lifespan` w FastAPI (moduł `database/DatabaseInitializer.py`) automatycznie utworzy bazę `database/sample_database.db` i załaduje do niej dane z plików CSV z katalogu `resources/` podczas startu serwera.
7.  **Interakcja z API:** Korzystaj z klienta HTTP (np. `curl`, Postman, przeglądarka z dokumentacją Swagger UI) do wysyłania żądań POST na endpoint `/execute` lub wykonaj następujące komendy w katalogu głównym projektu:
    ```bash
    cd frontend
    npm install
    npm audit fix --force
    npm install react-syntax-highlighter
    npm audit fix --force
    npm run dev
    ```
i wejdź w link, który zostanie wyświetlony w terminalu.

## Przykład użycia

![view1](/views/View_1.png)

![view2](/views/View_2.png)

![view3](/views/View_3.png)

![view4](/views/View_4.png)


## Inne informacje

*   Architektura opiera się na trójwarstwowym podejściu: webowy interfejs API (FastAPI), warstwa parsowania i walidacji (ANTLR + Python) oraz warstwa przechowywania i wykonywania danych (SQLite).
*   Interpreter syntaktycznie obsługuje szeroki podzbiór składni PostgreSQL (zgodnie z gramatyką `PostgreSQL.g4`), w tym m.in.:
    *   Instrukcje DDL: `CREATE TABLE`, `ALTER TABLE` (`ADD COLUMN`, `DROP COLUMN`, `ALTER COLUMN` z `SET/DROP DEFAULT/NOT NULL`), `DROP TABLE`.
    *   Instrukcje DML: `SELECT` (z `*`, listą kolumn/wyrażeń, aliasami, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, `LIMIT`), `INSERT` (tylko składnia `VALUES`), `UPDATE`, `DELETE`.
    *   JOINy (`INNER`, `LEFT`, `RIGHT`).
    *   Podstawowe typy danych (`INT`, `INTEGER`, `TEXT`, `VARCHAR`, `BOOLEAN`, `DATE`, `FLOAT`).
    *   Podstawowe ograniczenia (`PRIMARY KEY`, `UNIQUE`, `FOREIGN KEY`, `NOT NULL`, `DEFAULT`).
    *   Funkcje agregujące (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`).
*   **Ważne ograniczenie:** Faktyczne wykonanie zapytań jest realizowane przez silnik **SQLite**. Mimo że interpreter parsuje bardziej złożoną składnię PostgreSQL, możliwość jej wykonania jest ograniczona przez kompatybilność SQLite ze składnią i funkcjonalnościami PostgreSQL. Mogą występować różnice w zachowaniu, obsłudze typów danych, czy braku wsparcia dla specyficznych funkcji PostgreSQL, które nie są dostępne w SQLite.
*   Walidacja semantyczna (sprawdzanie istnienia tabel i kolumn, podstawowa zgodność typów) jest częściowo realizowana w kodzie Python (`utils/StructureValidator.py`) przed przekazaniem zapytania do SQLite. Bardziej zaawansowana walidacja jest realizowana przez sam silnik SQLite.
*   Baza danych (`database/sample_database.db`) jest tworzona i ładowana od nowa z plików CSV przy każdym uruchomieniu aplikacji (dzięki mechanizmowi `lifespan`).
