# Interpreter zapytań SQL dla PostgreSQL

## Dane studenta(-ów)

- **Imię i nazwisko:** Jan Banasik, Patrick Bajorski  
- **E-mail:** jbanasik@student.agh.edu.pl, pbajorski@student.agh.edu.pl 

## Założenia programu

### Ogólne cele programu

Celem projektu jest stworzenie interpretera zapytań SQL zgodnych ze składnią PostgreSQL. Program umożliwia analizę składniową zapytań i generuje ich strukturę w postaci drzewa parsowania. Pozwala to na lepsze zrozumienie składni SQL oraz może być podstawą do dalszego przetwarzania zapytań, np. optymalizacji, interpretacji, czy budowy silnika zapytań.

### Rodzaj translatora

**Interpreter** – projekt nie kompiluje kodu SQL do innego języka, ale analizuje i interpretuje jego składnię w czasie rzeczywistym.

### Planowany wynik działania programu

Interpreter zapytań SQL dla składni PostgreSQL, który:

- przyjmuje zapytanie SQL jako wejście,
- analizuje jego składnię za pomocą parsera stworzonego na podstawie gramatyki ANTLR,
- generuje i wyświetla drzewo parsowania.

### Planowany język implementacji

- **Python 3**

## Skaner i parser

### Sposób realizacji

Projekt wykorzystuje **ANTLR 4** – generator skanerów i parserów. Gramatyka języka SQL (PostgreSQL) została zdefiniowana w pliku `.g4`, z którego ANTLR generuje odpowiednie klasy parsera i leksera w Pythonie.

## Opis tokenów

Tokeny definiowane są w pliku gramatyki ANTLR `PostgreSQL.g4`. Przykładowe tokeny to:

- `SELECT`, `FROM`, `WHERE`, `JOIN`, `GROUP BY`, `HAVING`
- `IDENTIFIER`, `NUMBER`, `STRING`
- `=`, `>`, `<`, `>=`, `<=`, `<>`
- `+`, `-`, `*`, `/`

Tokeny są zgodne z typową składnią SQL i odpowiadają słowom kluczowym, operatorom oraz identyfikatorom.

## Gramatyka formatu

Gramatyka jest napisana w notacji ANTLR i obejmuje składnię PostgreSQL, np.:

```antlr
selectStatement
    : SELECT columnList FROM tableList (whereClause)? (groupByClause)? (havingClause)?
    ;

columnList
    : column (',' column)*
    ;

tableList
    : tableName (joinClause)?
    ;
```

(pełna gramatyka znajduje się w pliku `PostgreSQL.g4`)

## Informacje o użytych narzędziach

- **ANTLR 4.13.0** – do generowania parsera i leksera
- **Python 3.x** – do implementacji logiki programu
- **antlr4-python3-runtime** – biblioteka uruchomieniowa dla wygenerowanego parsera
- **Oficjalna gramatyka PostgreSQL dla ANTLR** (dostosowana do potrzeb projektu)

## Instrukcja obsługi

1. Zainstaluj zależności:
   ```bash
   pip install antlr4-python3-runtime
   ```

2. Pobierz ANTLR:
   ```bash
   wget https://www.antlr.org/download/antlr-4.13.0-complete.jar
   ```

3. Wygeneruj parser:
   ```bash
   java -jar antlr-4.13.0-complete.jar -Dlanguage=Python3 PostgreSQL.g4
   ```

4. Uruchom parser:
   ```bash
   python test_postgresql_parser.py
   ```

## Przykład użycia

**Wejście:**

```sql
SELECT id, age, name, surname
FROM users;
```

**Wynik:**

```
Parsed SQL:

    SELECT id, age, name, surname
    FROM users;
    

Parse Tree:
statement
  selectStatement
    SELECT
    columnList
      column
        columnName
          id
      ,
      column
        columnName
          age
      ,
      column
        columnName
          name
      ,
      column
        columnName
          surname
    FROM
    tableList
      tableName
        users
    semicolon
      ;
```
