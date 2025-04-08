from dataclasses import dataclass
from datetime import datetime

@dataclass
class UserEntity:
    id: int
    name: str
    email: str
    created_at: datetime
    is_active: bool
