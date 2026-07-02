📘 README
🧩 Overview
This project is a reusable Python MCP server template.
It lets you create MCP servers quickly by adding small tool files without modifying the main server code.

The server automatically loads all tools and resources, making it easy to extend and reuse.

📁 Project Structure
Code
mcp_server/
  server.py
  requirements.txt
  loaders/
    tool_loader.py
    resource_loader.py
  tools/
    ping.py
    math_add.py
  resources/
    config.json
⚙️ How It Works
server.py starts the MCP server.

The tool loader scans the /tools folder and auto‑registers any function decorated with @tool().

The resource loader loads any .json file from /resources.

You only add new tools by creating new Python files in /tools.

🚀 Getting Started
Install dependencies
Code
pip install -r requirements.txt
Run the server
Code
mcp dev server.py
Add a new tool
Create a file inside /tools, for example:

Code
tools/get_user.py
python
from mcp.server.fastmcp import tool

@tool()
def get_user(user_id: str):
    return {"user_id": user_id, "role": "admin"}
The server will automatically detect it.

⭐ Benefits of This Template
Easy to reuse — copy the folder to create a new MCP server.

No boilerplate — server core never changes.

Auto‑loading tools — drop a file, tool is ready.

Fast development — perfect for quick prototypes.

Clean structure — tools, resources, and loaders are separated.

Scalable — supports many tools without complexity.
