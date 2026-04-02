from pydantic import BaseModel, EmailStr
from datetime import datetime

# USER
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str


# CLIENTE
class ClienteCreate(BaseModel):
    nome: str
    email: EmailStr
    telefone: str | None = None


class ClienteResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr
    telefone: str | None = None
    created_at: datetime

    class Config:
        from_attributes = True

        