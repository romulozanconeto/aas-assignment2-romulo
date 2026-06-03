import pickle
import base64

def load_user_preferences(data_b64):
    """
    Loads user preferences from a base64-encoded string.
    VULNERABILITY: pickle.loads on untrusted data allows RCE.
    """
    if not data_b64:		               # Handle empty input
        return {}
    decoded = base64.b64decode(data_b64)   # Decode from base64 to bytes
    prefs = pickle.loads(decoded)          # Deserialize (unsafe on untrusted data)
    return prefs