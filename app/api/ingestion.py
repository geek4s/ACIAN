# ingestion.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.services.ingestion_service import ingest_competitor

router = APIRouter(
    prefix="/ingest",
    tags=["Ingestion"]
)


@router.post("/{competitor_id}")
def ingest(
    competitor_id: int,
    db: Session = Depends(get_db)
):

    return ingest_competitor(
        competitor_id,
        db
    )