# backend/app/models/user_competitor.py

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    DateTime,
    UniqueConstraint
)

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database.database import Base


class UserCompetitor(Base):
    __tablename__ = "user_competitors"

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "competitor_id",
            name="uq_user_competitor"
        ),
    )

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    competitor_id = Column(
        Integer,
        ForeignKey("competitors.id"),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    # Relationships
    user = relationship(
        "User",
        back_populates="tracked_competitors"
    )

    competitor = relationship(
        "Competitor",
        back_populates="tracked_users"
    )