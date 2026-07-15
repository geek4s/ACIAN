from fastapi import APIRouter, Depends, Security, HTTPException
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.session import get_db

from app.models.user import User
from app.models.competitor import Competitor
from app.models.user_competitor import UserCompetitor
from app.services.audit_service import log_action

from app.schemas.competitor import (
    CompetitorCreate,
    CompetitorUpdate,
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
        log_action(
          db=db,
          user_id=current_user.id,
          action="CREATE",
          table_name="competitors",
          record_id=existing_competitor.id,
          new_data={
              "company_name": existing_competitor.company_name,
              "website": existing_competitor.website,
              "industry": existing_competitor.industry,
              }
        )

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
@router.put("/{competitor_id}", response_model=CompetitorResponse)
def update_competitor(
    competitor_id: int,
    competitor: CompetitorUpdate,
    db: Session = Depends(get_db),
    current_user: User = Security(get_current_user),
):

    existing = (
        db.query(Competitor)
        .filter(Competitor.id == competitor_id)
        .first()
    )

    if existing is None:
        return {"error": "Competitor not found"}

    old_data = {
        "company_name": existing.company_name,
        "website": existing.website,
        "industry": existing.industry,
    }

    existing.company_name = competitor.company_name
    existing.website = competitor.website
    existing.industry = competitor.industry

    db.commit()
    db.refresh(existing)

    log_action(
        db=db,
        user_id=current_user.id,
        action="UPDATE",
        table_name="competitors",
        record_id=existing.id,
        old_data=old_data,
        new_data={
            "company_name": existing.company_name,
            "website": existing.website,
            "industry": existing.industry,
        }
    )

    return existing
@router.delete("/{competitor_id}")
def delete_competitor(
    competitor_id: int,
    db: Session = Depends(get_db),
    current_user: User = Security(get_current_user),
):

    competitor = (
        db.query(Competitor)
        .filter(Competitor.id == competitor_id)
        .first()
    )

    if competitor is None:
        return {"error": "Competitor not found"}

    old_data = {
        "company_name": competitor.company_name,
        "website": competitor.website,
        "industry": competitor.industry,
    }

    log_action(
        db=db,
        user_id=current_user.id,
        action="DELETE",
        table_name="competitors",
        record_id=competitor.id,
        old_data=old_data,
    )

    db.delete(competitor)
    db.commit()

    return {
        "message": "Competitor deleted successfully"
    }