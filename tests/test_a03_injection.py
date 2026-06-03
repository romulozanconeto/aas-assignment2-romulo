import pytest
from src.a03_injection import get_user_by_id

# Mock database cursor to capture and inspect raw SQL queries
class MockCursor:
    def __init__(self):
        self.last_query = None

    def execute(self, query):
        self.last_query = query

    def fetchall(self):
        return []

# Test: numeric ID produces safe WHERE clause with literal value
def test_valid_user_id():
    cursor = MockCursor()
    get_user_by_id(1, cursor)
    assert "WHERE id = 1" in cursor.last_query

# Test: malicious string with OR 1=1 bypasses logic if unsanitized
def test_sql_injection_bypass():
    cursor = MockCursor()
    malicious_id = "1 OR 1=1"
    get_user_by_id(malicious_id, cursor)
    assert malicious_id in cursor.last_query

# Test: more dangerous injection attempting to drop table
def test_sql_injection_drop_table():
    cursor = MockCursor()
    malicious_id = "1; DROP TABLE users; --"
    get_user_by_id(malicious_id, cursor)
    assert "DROP TABLE" in cursor.last_query