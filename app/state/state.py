from typing import TypedDict


class CompetitorState(TypedDict):

    competitor_id: int

    documents: list

    comparison: str

    sentiment: str

    report: str