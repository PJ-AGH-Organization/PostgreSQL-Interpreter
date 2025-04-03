# PostgreSQL Parser w ANTLR i Pythonie

## Opis

Ten projekt zawiera parser zapytań SQL dla PostgreSQL, zrealizowany za pomocą ANTLR 4 i Pythona. Parser umożliwia analizę składniową zapytań SQL, takich jak `SELECT`, `INSERT`, `UPDATE`, `DELETE` oraz obsługę zaawansowanych funkcji, takich jak `JOIN`, `GROUP BY`, `HAVING` i funkcje okna.

Projekt generuje drzewo parsowania zapytania SQL i wyświetla je w czytelnej formie.

## Wymagania

- Python 3.x
- ANTLR 4.x
- PostgreSQL Grammar w ANTLR

## Instalacja

### Krok 1: Instalacja zależności

Aby uruchomić projekt, musisz zainstalować odpowiednie zależności:

1. **Zainstaluj bibliotekę ANTLR dla Pythona:**

   ```bash
   pip install antlr4-python3-runtime
   ```

2. **Pobierz ANTLR jar:**

   W terminalu wykonaj polecenie, aby pobrać plik JAR ANTLR:

   ```bash
   wget https://www.antlr.org/download/antlr-4.13.0-complete.jar
   ```

### Krok 2: Generowanie parsera

1. Stwórz plik gramatyki `PostgreSQL.g4` (lub użyj dostarczonego pliku).
   
2. Uruchom ANTLR, aby wygenerować pliki w Pythonie:

   ```bash
   java -jar antlr-4.13.0-complete.jar -Dlanguage=Python3 PostgreSQL.g4
   ```

3. To polecenie wygeneruje pliki:
   - `PostgreSQLLexer.py`
   - `PostgreSQLParser.py`
   - `PostgreSQLListener.py` (opcjonalnie)

### Krok 3: Uruchomienie parsera w Pythonie

Wykorzystaj plik `test_postgresql_parser.py` (zawierający kod testowy) do analizy zapytania SQL:

```bash
python test_postgresql_parser.py
```

### Krok 4: Uruchomienie analizy

Po uruchomieniu skryptu, program przetworzy zapytanie SQL i wyświetli drzewo parsowania w czytelnej formie.

## Przykład użycia

**Zapytanie SQL:**

```sql
SELECT COUNT(id), name
FROM users
INNER JOIN orders ON users.id = orders.user_id
GROUP BY name
HAVING COUNT(id) > 5
```

**Wyjście programu:**

```
Parsed SQL:
SELECT COUNT(id), name
FROM users
INNER JOIN orders ON users.id = orders.user_id
GROUP BY name
HAVING COUNT(id) > 5

Parse Tree:
statement
  selectStatement
    columnList
      column
        aggregateFunction
          COUNT
          columnName
            id
      column
        columnName
          name
    tableList
      tableName
        users
      joinClause
        joinType
          INNER
        tableName
          orders
        condition
          expression
            columnName
              users.id
          comparisonOperator
            '='
          expression
            columnName
              orders.user_id
    groupByClause
      GROUP BY
      columnList
        column
          columnName
            name
    havingClause
      HAVING
      condition
        expression
          aggregateFunction
            COUNT
            columnName
              id
        comparisonOperator
          '>'
        expression
          value
            5
```
