from src.database import Base
from sqlalchemy import Column, Integer, String, Text, DateTime

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String(256), nullable=False)
    content = Column(Text)
    date = Column(DateTime)
