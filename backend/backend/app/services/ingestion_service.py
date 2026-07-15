from sqlalchemy.orm import Session

from app.services.snapshot_service import create_snapshot
from app.embeddings.chunker import TextChunker
from app.embeddings.embedder import Embedder
from app.embeddings.vector_store import VectorStore


def ingest_competitor(
    competitor_id: int,
    db: Session
):

    # 1. Create Snapshot
    snapshot = create_snapshot(
        competitor_id=competitor_id,
        db=db
    )

    # 2. Chunk the page
    chunks = TextChunker.chunk(
        snapshot.page_content
    )

    # 3. Store embeddings
    store = VectorStore()

    for index, chunk in enumerate(chunks):

        embedding = Embedder.embed(chunk)

        store.add_document(
            document_id=f"{snapshot.id}_{index}",
            text=chunk,
            embedding=embedding,
            metadata={
                "snapshot_id": snapshot.id,
                "competitor_id": competitor_id
            }
        )

    return {
        "snapshot_id": snapshot.id,
        "chunks": len(chunks),
        "status": "completed"
    }