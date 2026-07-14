# backend/app/api/competitors.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.auth.dependencies import get_current_user
from app.models.user import User
from app.database.session import get_db
from fastapi import Security
from app.models.competitor import Competitor
from app.schemas.competitor import (
    CompetitorCreate,
    CompetitorResponse,
)

router = APIRouter(
    prefix="/competitors",
    tags=["Competitors"]
)


@router.post("/", response_model=CompetitorResponse)
def add_competitor(
    competitor: CompetitorCreate,
    db: Session = Depends(get_db),
    current_user: User = Security(get_current_user),
):
    new_competitor = Competitor(
        user_id=current_user.id,
        company_name=competitor.company_name,
        website=competitor.website,
        industry=competitor.industry,
    )

    db.add(new_competitor)
    db.commit()
    db.refresh(new_competitor)

    return new_competitor