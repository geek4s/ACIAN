from fastapi import APIRouter, Depends, Security, HTTPException
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.session import get_db

from app.models.user import User
from app.models.competitor import Competitor
from app.models.user_competitor import UserCompetitor

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

    # Check if competitor already exists globally
    existing_competitor = (
        db.query(Competitor)
        .filter(Competitor.website == competitor.website)
        .first()
    )

    if existing_competitor is None:

        existing_competitor = Competitor(
            company_name=competitor.company_name,
            website=competitor.website,
            industry=competitor.industry,
        )

        db.add(existing_competitor)
        db.commit()
        db.refresh(existing_competitor)

    # Check if THIS user is already tracking it
    existing_link = (
        db.query(UserCompetitor)
        .filter(
            UserCompetitor.user_id == current_user.id,
            UserCompetitor.competitor_id == existing_competitor.id,
        )
        .first()
    )

    if existing_link:
        raise HTTPException(
            status_code=400,
            detail="You are already tracking this competitor."
        )

    # Create tracking relationship
    tracking = UserCompetitor(
        user_id=current_user.id,
        competitor_id=existing_competitor.id,
    )

    db.add(tracking)
    db.commit()

    return existing_competitor