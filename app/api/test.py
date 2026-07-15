from fastapi import APIRouter

from app.graph.workflow import graph

router = APIRouter(
    prefix="/test",
    tags=["Testing"]
)

@router.post("/retrieval/{competitor_id}")
def test_retrieval(competitor_id: int):

    result = graph.invoke(
        {
            "competitor_id": competitor_id
        }
    )

    return result