from app.embeddings.embedder import Embedder

vector = Embedder.embed(
    "OpenAI develops artificial intelligence."
)

print("Vector Length:", len(vector))
print()
print(vector[:10])