from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ACIAN")

def hello() -> str:
    return "Hello from ACIAN"

mcp.add_tool(hello)