from pydantic import BaseModel
from typing import List, Optional


class NewsItem(BaseModel):
    icon: str
    description: str


class UserCreate(BaseModel):
    name: str
    account_number: str
    news: Optional[List[NewsItem]] = None


class UserResponse(BaseModel):
    id: int
    name: str
    account_number: str
    news: Optional[List[NewsItem]] = None

    class Config:
        from_attributes = True