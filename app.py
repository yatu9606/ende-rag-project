from endee.vector_store import VectorStore
from ingest import ingest
from query import semantic_search

print("Starting Endee Semantic Search Demo")

# 🔥 ONE shared VectorStore
vector_store = VectorStore(
    collection_name="rag_demo",
    embedding_dim=384
)

# Ingest data
ingest(vector_store)

# Query loop
while True:
    q = input("\nEnter query (or type 'exit'): ")
    if q.lower() == "exit":
        break
    semantic_search(vector_store, q)
