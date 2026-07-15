from app.mcp.tools import (
    list_competitors,
    get_competitor,
)
from app.mcp.tools import (
    list_competitors,
    get_competitor,
    ingest_competitor_tool,
)
from app.mcp.tools import (
    list_competitors,
    get_competitor,
    ingest_competitor_tool,
    search_documents,
)

print("------ ALL COMPETITORS ------")
print(list_competitors())
print()

print("------ COMPETITOR  ------")
print(get_competitor(1))
print()

print("------ INGEST COMPETITOR ------")
print(ingest_competitor_tool(1))

print()
print("------ SEARCH DOCUMENTS ------")
results = search_documents(
    "Apple"
)

print(results)