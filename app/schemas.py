from pydantic import BaseModel

class PasswordCreate(BaseModel):
    username: str
    service: str
    password: str

class PasswordResponse(BaseModel):
    username: str
    service: str

    class Config:
        orm_mode = True
