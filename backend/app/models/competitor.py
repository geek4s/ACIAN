# backend/app/models/competitor.py

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    UniqueConstraint,
)

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database.database import Base


class Competitor(Base):
    __tablename__ = "competitors"

    __table_args__ = (
        UniqueConstraint(
            "website",
            name="uq_website"
        ),
    )

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    company_name = Column(
        String(255),
        nullable=False
    )

    website = Column(
        String(255),
        nullable=False
    )

    industry = Column(
        String(100),
        nullable=False
    )

    # Used to determine when the website should be scraped again
    last_scraped = Column(
        DateTime(timezone=True),
        nullable=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    # Many users can track one competitor
    tracked_users = relationship(
        "UserCompetitor",
        back_populates="competitor",
        cascade="all, delete-orphan"
    )

    # One competitor has many snapshots
    snapshots = relationship(
        "Snapshot",
        back_populates="competitor",
        cascade="all, delete-orphan"
    )