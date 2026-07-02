# 🤖 Python MCP Server Template

A reusable, plug-and-play template for building [Model Context Protocol (MCP)](https://modelcontextprotocol.io) servers in Python.
Drop in a new tool file and the server picks it up automatically — no boilerplate, no rewiring.

---

## 📘 Overview

This template lets you spin up MCP servers quickly by adding small, self-contained tool files — without ever touching the core server code.
The server auto-discovers and registers all tools and resources at startup, making it trivial to extend and reuse across projects.

---

## 📁 Project Structure

```
mcp_server/
├── server.py                  # MCP server entrypoint
├── requirements.txt
├── loaders/
│   ├── tool_loader.py         # Auto-scans /tools and registers @tool() functions
│   └── resource_loader.py     # Auto-loads .json files from /resources
├── tools/
│   ├── ping.py                # Example tool — health check
│   └── math_add.py            # Example tool — addition
└── resources/
    └── config.json            # Example resource — server config
```

---

## ⚙️ How It Works

1. `server.py` starts the MCP server
2. `tool_loader.py` scans the `/tools` folder and auto-registers any function decorated with `@tool()`
3. `resource_loader.py` loads every `.json` file found in `/resources`
4. To add new functionality — just drop a new `.py` file in `/tools`. That's it.

---

## 🚀 Getting Started

**1. Clone the repo**
```bash
git clone https://github.com/your-username/mcp-server-template.git
cd mcp-server-template
```

**2. Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the server**
```bash
mcp dev server.py
```

---

## 🧩 Adding a New Tool

Create a new `.py` file inside `/tools`:

```python
# tools/get_user.py

from mcp.server.fastmcp import tool

@tool()
def get_user(user_id: str) -> dict:
    """Returns user details for a given user ID."""
    return {"user_id": user_id, "role": "admin"}
```

The server detects and registers it automatically on next startup. No changes needed anywhere else.

---

## 📦 Example Tools Included

| File | Function | Description |
|---|---|---|
| `tools/ping.py` | `ping()` | Health check — returns `pong` |
| `tools/math_add.py` | `math_add(a, b)` | Adds two numbers |

---

## ⭐ Why Use This Template

| Feature | Benefit |
|---|---|
| **Auto-loading tools** | Drop a file in `/tools` — it's live |
| **No boilerplate** | Server core never needs to change |
| **Clean separation** | Tools, resources, and loaders are fully decoupled |
| **Easy to reuse** | Copy the folder to start a new MCP server instantly |
| **Fast prototyping** | Go from idea to working tool in under a minute |
| **Scalable** | Add dozens of tools with zero added complexity |

---

## 🛠️ Requirements

- Python 3.10+
- `mcp` Python SDK — see `requirements.txt`

---

## 📄 License

MIT — free to use, modify, and distribute.
