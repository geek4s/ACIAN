from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database.database import Base


class Competitor(Base):
    __tablename__ = "competitors"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    company_name = Column(String(255), nullable=False)

    website = Column(String(255), nullable=False)

    industry = Column(String(100), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship(
        "User",
        back_populates="competitors"
    )
    snapshots = relationship(
    "Snapshot",
    back_populates="competitor",
    cascade="all, delete-orphan"
    )