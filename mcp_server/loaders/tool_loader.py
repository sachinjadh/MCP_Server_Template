import os
import importlib

def load_tools(mcp):
    tools_dir = os.path.join(os.path.dirname(__file__), "..", "tools")

    for file in os.listdir(tools_dir):
        if file.endswith(".py") and not file.startswith("__"):
            module_name = f"tools.{file[:-3]}"
            module = importlib.import_module(module_name)

            for attr in dir(module):
                obj = getattr(module, attr)
                if hasattr(obj, "_mcp_tool"):
                    mcp.register_tool(obj)
