from app.graph.workflow import graph


def test_comparison_agent():

    result = graph.invoke(
        {
            "competitor_id": 4
        }
    )
    print("\nComparison Output:\n")
    print(result["comparison"])
    assert "comparison" in result
    assert isinstance(result["comparison"], str)
    assert len(result["comparison"]) > 0

    """assert (
        "Comparison Summary" in result["comparison"]
        or "No previous snapshot available." in result["comparison"]
    )"""