from mcp.server.fastmcp import tool

@tool()
def ping() -> dict:
    return {"status": "ok", "message": "pong"}
