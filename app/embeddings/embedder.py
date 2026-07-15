from sentence_transformers import SentenceTransformer


class Embedder:

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    @classmethod
    def embed(cls, text: str):

        embedding = cls.model.encode(text)

        return embedding.tolist()