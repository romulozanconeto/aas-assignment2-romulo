# Document model with owner and content
class Document:
    def __init__(self, owner, content):
        self.owner = owner
        self.content = content

# In-memory document storage
documents = {
    "doc1": Document("alice", "Alice's secret document"),
    "doc2": Document("bob", "Bob's public document"),
    "doc3": Document("admin", "Sensitive admin data")
}

def get_document(doc_id, user):
    """
    Retrieves a document if the user is authorized.
    VULNERABILITY: Assumes user.role is trustworthy.
    """
    doc = documents.get(doc_id)          # Fetch document by ID
    if doc is None:                      # Handle missing document
        return "Document not found"
    if user.role == "admin":             # Admin bypasses ownership check
        return doc.content
    if doc.owner == user.username:       # Owner can access own document
        return doc.content
    return "Access denied"               # Unauthorized access