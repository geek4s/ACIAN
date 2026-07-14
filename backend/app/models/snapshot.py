# backend/app/models/snapshot.py

from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database.database import Base


class Snapshot(Base):
    __tablename__ = "snapshots"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True)

    # Foreign Key
    competitor_id = Column(
        Integer,
        ForeignKey("competitors.id"),
        nullable=False
    )

    # Scraped Data
    page_title = Column(Text, nullable=True)

    raw_html = Column(Text, nullable=True)

    page_content = Column(Text, nullable=True)

    pricing = Column(Text, nullable=True)

    features = Column(Text, nullable=True)

    # Timestamp
    snapshot_date = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    # Relationship
    competitor = relationship(
        "Competitor",
        back_populates="snapshots"
    )