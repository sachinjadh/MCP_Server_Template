import os
import json

def load_resources(mcp):
    resources_dir = os.path.join(os.path.dirname(__file__), "..", "resources")

    for file in os.listdir(resources_dir):
        if file.endswith(".json"):
            path = os.path.join(resources_dir, file)
            with open(path, "r") as f:
                data = json.load(f)

            mcp.register_resource(
                name=file.replace(".json", ""),
                data=data
            )
