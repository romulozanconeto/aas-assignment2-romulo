import pytest
from src.a02_crypto import store_password

# Test that MD5 hash output length is always 32 hex characters
def test_md5_hash_length():
    result = store_password("test")
    assert len(result) == 32

# Test that same password produces identical hash (deterministic)
def test_md5_deterministic():
    r1 = store_password("password123")
    r2 = store_password("password123")
    assert r1 == r2

# Test vulnerability: no salt → identical passwords yield identical hashes
def test_no_salt_vulnerability():
    h1 = store_password("secret")
    h2 = store_password("secret")
    assert h1 == h2

# Test edge case: empty password still returns 32-character hash
def test_empty_password():
    result = store_password("")
    assert len(result) == 32