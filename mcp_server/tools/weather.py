import requests
from mcp.server.fastmcp import tool

@tool()
def weather(city: str):
    r = requests.get(f"https://wttr.in/{city}?format=j1")
    return r.json()
