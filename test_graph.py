from app.graph.workflow import graph

result = graph.invoke(
    {
        "competitor_id": 4
    }
)

print(result)