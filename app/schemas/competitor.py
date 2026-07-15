from pydantic import BaseModel


class CompetitorCreate(BaseModel):
    company_name: str
    website: str
    industry: str


class CompetitorResponse(BaseModel):
    id: int
    company_name: str
    website: str
    industry: str

    class Config:
        from_attributes = True