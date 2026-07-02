from mcp.server.fastmcp import tool
from contracts.user_contract import UserContract

@tool()
def get_user(user_id: str):
    user = UserContract(
        user_id=user_id,
        name="Sachin",
        role="admin"
    )
    return user.__dict__
