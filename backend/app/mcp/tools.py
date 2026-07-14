from app.mcp.server import mcp

@mcp.tool()
def hello() -> str:
    """Returns a hello message."""
    return "Hello from ACIAN!"