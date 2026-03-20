from embedder import Embedder
from data import documents
from vector_store import VectorStore

class RAGSystem:
    def __init__(self):
        self.embedder=Embedder()

        self.doc_embeddings=self.embedder.encode(documents)

        dimension=len(self.doc_embeddings[0])
        self.vector_store=VectorStore(dimension)

        self.vector_store.add(self.doc_embeddings)

    def retrieve(self,query):
        query_embedding=self.embedder.encode([query])
        indices=self.vector_store.search(query_embedding)
        results=[documents[i] for i in indices[0]]
        return results