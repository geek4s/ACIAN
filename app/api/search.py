from fastapi import APIRouter
from app.mcp.tools import search_documents

router = APIRouter()

@router.get("/search")
def search(query: str, n_results: int = 3):
    return search_documents(query, n_results)