from app.embeddings.embedder import Embedder
from app.embeddings.vector_store import VectorStore


def retrieval_agent(state):

    competitor_id = state["competitor_id"]

    vector_store = VectorStore()

    query_embedding = Embedder.embed("company overview")

    results = vector_store.search(
        query_embedding=query_embedding,
        n_results=5,
        competitor_id=competitor_id
    )

    state["documents"] = results["documents"][0]

    return state