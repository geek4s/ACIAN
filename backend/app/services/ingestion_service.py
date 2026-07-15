from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone

from app.models.competitor import Competitor

from app.services.snapshot_service import create_snapshot
from app.embeddings.chunker import TextChunker
from app.embeddings.embedder import Embedder
from app.embeddings.vector_store import VectorStore


def ingest_competitor(
    competitor_id: int,
    db: Session
):

    competitor = (
        db.query(Competitor)
        .filter(Competitor.id == competitor_id)
        .first()
    )

    if competitor is None:
        return {
            "status": "error",
            "message": "Competitor not found."
        }

    # -----------------------------
    # Cache Check
    # -----------------------------
    if competitor.last_scraped is not None:

        age = datetime.now(timezone.utc) - competitor.last_scraped

        if age < timedelta(days=7):

            return {
                "status": "cached",
                "message": "Competitor was scraped recently.",
                "last_scraped": competitor.last_scraped,
            }

    # -----------------------------
    # Create Snapshot
    # -----------------------------
    snapshot = create_snapshot(
        competitor_id=competitor_id,
        db=db
    )

    # -----------------------------
    # Chunk Page
    # -----------------------------
    chunks = TextChunker.chunk(
        snapshot.page_content
    )

    # -----------------------------
    # Store Embeddings
    # -----------------------------
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

    # -----------------------------
    # Update scrape time
    # -----------------------------
    competitor.last_scraped = datetime.now(timezone.utc)

    db.commit()

    return {
        "snapshot_id": snapshot.id,
        "chunks": len(chunks),
        "status": "completed"
    }
