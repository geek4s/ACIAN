# app/mcp/tools.py

from sqlalchemy.orm import Session

from app.mcp.server import mcp
from app.database.session import SessionLocal
from app.models.competitor import Competitor
from app.services.ingestion_service import ingest_competitor
from app.embeddings.embedder import Embedder
from app.embeddings.vector_store import VectorStore

@mcp.tool()
def list_competitors():
    """
    Returns all competitors.
    """

    db: Session = SessionLocal()

    competitors = db.query(Competitor).all()

    result = []

    for competitor in competitors:
        result.append(
            {
                "id": competitor.id,
                "company_name": competitor.company_name,
                "website": competitor.website,
                "industry": competitor.industry,
                "tracked_users": len(competitor.tracked_users),
            }
        )

    db.close()

    return result


@mcp.tool()
def get_competitor(competitor_id: int):
    """
    Returns one competitor.
    """

    db: Session = SessionLocal()

    competitor = (
        db.query(Competitor)
        .filter(Competitor.id == competitor_id)
        .first()
    )

    db.close()

    if competitor is None:
        return {"error": "Competitor not found"}

    return {
        "id": competitor.id,
        "company_name": competitor.company_name,
        "website": competitor.website,
        "industry": competitor.industry,
        "tracked_users": len(competitor.tracked_users),
    }

@mcp.tool()
def ingest_competitor_tool(competitor_id: int):
    """
    Ingest a competitor by scraping its website,
    creating a snapshot, chunking the content,
    generating embeddings, and storing them in ChromaDB.
    """

    db: Session = SessionLocal()

    try:
        result = ingest_competitor(
            competitor_id=competitor_id,
            db=db
        )

        return result

    finally:
        db.close()

@mcp.tool()
def search_documents(
    query: str,
    n_results: int = 3
):
    """
    Search competitor documents using semantic search.
    """

    vector_store = VectorStore()

    query_embedding = Embedder.embed(query)

    results = vector_store.search(
        query_embedding=query_embedding,
        n_results=n_results
    )

    formatted_results = []

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    for document, metadata, distance in zip(
        documents,
        metadatas,
        distances
    ):

        formatted_results.append({
            "document": document[:300] + "...",
            "competitor_id": metadata["competitor_id"],
            "snapshot_id": metadata["snapshot_id"],
            "distance": distance
        })

    return formatted_results