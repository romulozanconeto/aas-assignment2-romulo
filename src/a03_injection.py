def get_user_by_id(user_id, mock_cursor):
    """
    Retrieves a user from the database by ID.
    VULNERABILITY: String concatenation allows SQL injection.
    """
    # Build query by directly inserting user_id into string (unsafe)
    query = f"SELECT * FROM users WHERE id = {user_id}"
    mock_cursor.execute(query)     # Execute raw query
    return mock_cursor.fetchall()  # Return all results