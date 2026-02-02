import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class VectorStore:
    """
    Python adapter representing Endee vector database behavior.
    This acts as an interface layer over Endee's vector storage concepts.
    """

    def __init__(self, collection_name: str, embedding_dim: int):
        self.collection_name = collection_name
        self.embedding_dim = embedding_dim
        self.vectors = []
        self.metadata = []

    def add(self, id: str, vector: list, metadata: dict):
        self.vectors.append(np.array(vector))
        self.metadata.append(metadata)

    def search(self, query_vector: list, top_k: int = 3):
        if not self.vectors:
            return []

        vectors = np.array(self.vectors)
        query = np.array(query_vector).reshape(1, -1)

        scores = cosine_similarity(query, vectors)[0]
        top_indices = scores.argsort()[::-1][:top_k]

        results = []
        for idx in top_indices:
            results.append({
                "score": float(scores[idx]),
                "metadata": self.metadata[idx]
            })

        return results
