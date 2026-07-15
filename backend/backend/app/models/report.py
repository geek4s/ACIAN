from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database.database import Base


class Report(Base):
    __tablename__ = "reports"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True)

    # User who owns this report
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    # Report Information
    title = Column(String(255), nullable=False)

    summary = Column(Text, nullable=False)

    report_url = Column(String(500), nullable=True)

    # Timestamp
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    # Relationship
    user = relationship(
        "User",
        back_populates="reports"
    )