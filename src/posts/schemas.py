#TODO 
# create post
# read post
# update post
# delete post
# 

from pydantic import BaseModel
from pydantic.types import datetime

class PostBase(BaseModel):
    title: str
    content: str
    date: datetime

class Post(PostBase):
    id: int
    
    class Config:
        orm_mode = True

class PostCreate(PostBase):
    pass
    
