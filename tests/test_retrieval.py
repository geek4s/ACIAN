from app.graph.workflow import graph


def test_retrieval_returns_documents():
    result = graph.invoke(
        {
            "competitor_id": 3
        }
    )

    assert "documents" in result
    assert len(result["documents"]) > 0


def test_retrieval_document_type():
    result = graph.invoke(
        {
            "competitor_id": 3
        }
    )

    for document in result["documents"]:
        assert isinstance(document, str)


def test_invalid_competitor():
    result = graph.invoke(
        {
            "competitor_id": 9999
        }
    )

    assert result["documents"] == []