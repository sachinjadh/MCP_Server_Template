from mcp.server.fastmcp import FastMCP
from loaders.tool_loader import load_tools
from loaders.resource_loader import load_resources

mcp = FastMCP("reusable-python-server")

load_tools(mcp)
load_resources(mcp)

if __name__ == "__main__":
    mcp.run()
