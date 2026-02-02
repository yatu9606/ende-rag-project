from sentence_transformers import SentenceTransformer

TOP_K = 3

def semantic_search(vector_store, query):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_embedding = model.encode([query])[0].tolist()

    results = vector_store.search(
        query_vector=query_embedding,
        top_k=TOP_K
    )

    print("\nTop Results:\n")
    for i, res in enumerate(results, 1):
        print(f"{i}. {res['metadata']['text']}")
