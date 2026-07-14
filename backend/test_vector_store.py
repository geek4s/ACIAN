from app.embeddings.embedder import Embedder
from app.embeddings.vector_store import VectorStore

store = VectorStore()

text = "OpenAI develops AI systems."

embedding = Embedder.embed(text)

store.add_document(
    document_id=1,
    text=text,
    embedding=embedding,
    metadata={
        "company": "OpenAI"
    }
)

query = Embedder.embed(
    "Artificial Intelligence"
)

results = store.search(query)

print(results)