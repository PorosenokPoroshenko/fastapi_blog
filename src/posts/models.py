from ..database import Base
from sqlalchemy import Column, Integer, String, Text, DateTime, func
from datetime import datetime


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String(256), nullable=False)
    content = Column(Text)
    date = Column(
        DateTime,
        default=func.now(),
        server_default=func.now(),
        onupdate=func.current_timestamp(),
    )
