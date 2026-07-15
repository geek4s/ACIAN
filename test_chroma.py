from app.embeddings.vector_store import VectorStore

store = VectorStore()

results = store.collection.get()

print("Number of documents:", len(results["ids"]))

print("\nMetadata:")
for metadata in results["metadatas"]:
    print(metadata)