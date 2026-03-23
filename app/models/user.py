from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSON
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    account_number = Column(String, nullable=False)
    news = Column(JSON, nullable=True)