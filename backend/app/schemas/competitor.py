from pydantic import BaseModel
from datetime import datetime

class CompetitorCreate(BaseModel):
    company_name: str
    website: str
    industry: str


class CompetitorResponse(BaseModel):
    id: int
    company_name: str
    website: str
    industry: str
    last_scraped: datetime | None
    created_at: datetime

    class Config:
        from_attributes = True

class CompetitorUpdate(BaseModel):
    company_name: str
    website: str
    industry: str