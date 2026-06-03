import hashlib

def store_password(password):
    """
    Stores a password hash.
    VULNERABILITY: Uses MD5 without salt.
    """
    # Encode password to bytes, compute MD5 hash, return as hex string
    hashed = hashlib.md5(password.encode()).hexdigest()
    return hashed