from sqlalchemy.orm import Session

from app.models.competitor import Competitor
from app.models.snapshot import Snapshot
from app.scrapers.website_scraper import WebsiteScraper


def create_snapshot(
    competitor_id: int,
    db: Session
):

    competitor = (
        db.query(Competitor)
        .filter(Competitor.id == competitor_id)
        .first()
    )

    if competitor is None:
        raise Exception("Competitor not found")

    scraped = WebsiteScraper.scrape(
        competitor.website
    )

    snapshot = Snapshot(
        competitor_id=competitor.id,
        page_title=scraped["title"],
        raw_html=scraped["html"],
        page_content=scraped["text"]
    )

    db.add(snapshot)
    db.commit()
    db.refresh(snapshot)

    return snapshot