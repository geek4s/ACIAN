from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database.database import Base


class Sentiment(Base):
    __tablename__ = "sentiment"

    id = Column(Integer, primary_key=True, index=True)

    competitor_id = Column(Integer, ForeignKey("competitors.id"))

    positive = Column(Float)

    negative = Column(Float)

    neutral = Column(Float)

    overall_score = Column(Float)

    date = Column(DateTime(timezone=True), server_default=func.now())

    competitor = relationship("Competitor")