import chromadb


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="competitor_snapshots"
        )

    def add_document(
        self,
        document_id,
        text,
        embedding,
        metadata
    ):

        self.collection.add(
            ids=[str(document_id)],
            documents=[text],
            embeddings=[embedding],
            metadatas=[metadata]
        )

    def search(
        self,
        query_embedding,
        n_results=3
    ):

        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )