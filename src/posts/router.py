from fastapi import APIRouter, Path 
from typing import Annotated


posts = [{"id": 5, "title": "KEKS", "content":"1 2 3 4 455 6"},
         {"id": 6, "title": "KEKS2", "content":"1 2 3 4 455 6"},
         ]

router = APIRouter(
    prefix="/posts",
    tags=["Posts"],
)

@router.get("/")
def get_posts():
    return posts

@router.get("/latest")
def get_latest_post():
    return {"id":0, "title": "KEKS0", "content":"1231"}

@router.get("/{post_id}")
def get_post_by_id(post_id: Annotated[int, Path(ge=1)]):
    return {"id":post_id}