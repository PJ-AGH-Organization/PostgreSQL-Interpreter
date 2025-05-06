import pytest
from main import execute_test  # lub odpowiednia ścieżka do funkcji

valid_queries = [
    "SELECT COUNT(*) FROM suppliers;",
    "SELECT * FROM customers LIMIT 5;",
    "SELECT employeeid, lastname FROM employees WHERE employeeid < 10;",
    "SELECT orderid, orderdate FROM orders WHERE orderdate > '1997-01-01';",
    "SELECT productid, productname FROM products WHERE unitprice > 20;"
]

@pytest.mark.parametrize("query", valid_queries)
def test_valid_queries_without_errors(query):
    result = execute_test(query)
    assert "error" not in result, f"Query failed: {query}"
