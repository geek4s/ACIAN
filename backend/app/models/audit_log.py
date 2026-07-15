from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    JSON,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database.database import Base


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    # User who performed the action
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    # CREATE / UPDATE / DELETE / LOGIN / INGEST ...
    action = Column(
        String(50),
        nullable=False
    )

    # Table affected
    table_name = Column(
        String(100),
        nullable=False
    )

    # ID of the affected record
    record_id = Column(
        Integer,
        nullable=False
    )

    # Entire row before the update/delete
    old_data = Column(
        JSON,
        nullable=True
    )

    # Entire row after create/update
    new_data = Column(
        JSON,
        nullable=True
    )

    timestamp = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    user = relationship(
        "User"
    )