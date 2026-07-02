from dataclasses import dataclass

@dataclass
class UserContract:
    user_id: str
    name: str
    role: str
