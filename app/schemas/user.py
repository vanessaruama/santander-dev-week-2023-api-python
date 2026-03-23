from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    account_number: str


class UserResponse(BaseModel):
    id: int
    name: str
    account_number: str

    class Config:
        from_attributes = True
