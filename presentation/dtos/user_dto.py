from pydantic import BaseModel, EmailStr

class UserDTO(BaseModel):
    id: int | None
    name: str
    email: EmailStr
    is_active: bool | None
