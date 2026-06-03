import pytest
import base64
import pickle
from unittest.mock import patch
from src.a08_deserialization import load_user_preferences

# Test: empty string returns empty dict
def test_empty_string():
    result = load_user_preferences("")
    assert result == {}

# Test: valid base64-encoded pickled dict is deserialized correctly
def test_valid_base64_pickle_dict():
    data = {"theme": "dark"}
    pickled = pickle.dumps(data)
    b64 = base64.b64encode(pickled).decode()
    with patch('pickle.loads') as mock_loads:
        mock_loads.return_value = data
        result = load_user_preferences(b64)
        mock_loads.assert_called_once_with(pickled)
        assert result == data

# Test: valid base64-encoded pickled list is also accepted
def test_valid_base64_pickle_list():
    data = [1, 2, 3]
    pickled = pickle.dumps(data)
    b64 = base64.b64encode(pickled).decode()
    with patch('pickle.loads') as mock_loads:
        mock_loads.return_value = data
        result = load_user_preferences(b64)
        mock_loads.assert_called_once_with(pickled)
        assert result == data

# Test: malformed base64 string raises exception
def test_malformed_base64():
    with pytest.raises(Exception):
        load_user_preferences("Invalid pickle")

# Test: valid base64 but invalid pickle content (e.g., random bytes) raises exception
def test_invalid_pickle_data():
    # Valid base64 but invalid pickle content (e.g., random bytes)
    b64 = base64.b64encode(b"Not a pickle").decode()
    # Original code does not catch pickle.UnpicklingError
    with pytest.raises(Exception):
        load_user_preferences(b64)