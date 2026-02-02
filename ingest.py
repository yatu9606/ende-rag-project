import os
from sentence_transformers import SentenceTransformer

DATA_FILE = "data/documents.txt"

def ingest(vector_store):
    print("Loading embedding model...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError("documents.txt not found")

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        documents = [line.strip() for line in f if line.strip()]

    embeddings = model.encode(documents, show_progress_bar=True)

    for i, (doc, emb) in enumerate(zip(documents, embeddings)):
        vector_store.add(
            id=str(i),
            vector=emb.tolist(),
            metadata={"text": doc}
        )

    print(f"Ingested {len(documents)} documents into Endee")
