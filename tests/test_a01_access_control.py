import pytest
from src.a01_access_control import get_document

# Mock user class for testing access control
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

# Test: admin can access any document
def test_admin_access_any_document():
    user = User("anyone", "admin")
    content = get_document("doc1", user)
    assert "Alice's secret document" in content

# Test: document owner can access own document
def test_owner_access_own_document():
    user = User("alice", "user")
    content = get_document("doc1", user)
    assert "Alice's secret document" in content

# Test: unauthorized user (wrong role) gets denied
def test_unauthorized_user():
    user = User("charlie", "user")
    result = get_document("doc1", user)
    assert result == "Access denied"

# Test: requesting non-existent document returns not found
def test_nonexistent_document():
    user = User("alice", "user")
    result = get_document("doc999", user)
    assert result == "Document not found"

# Test: role manipulation (malicious user as admin) grants access
def test_admin_access_via_role_manipulation():
    malicious_user = User("charlie", "admin")
    content = get_document("doc1", malicious_user)
    assert "Alice's secret document" in content