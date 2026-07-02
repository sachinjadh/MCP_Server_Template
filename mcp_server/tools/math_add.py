from mcp.server.fastmcp import tool

@tool()
def add(a: int, b: int) -> dict:
    return {"result": a + b}
