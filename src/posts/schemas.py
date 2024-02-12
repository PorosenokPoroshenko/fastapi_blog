from pydantic import BaseModel
from pydantic.types import datetime

class PostBase(BaseModel):
    title: str
    content: str

class Post(PostBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True

class PostCreate(PostBase):
    pass
    
