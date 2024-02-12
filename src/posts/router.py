from fastapi import APIRouter, Path, Depends, Form
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from typing import Annotated

from src.posts import schemas, service
from src.database import get_db

router = APIRouter(
    prefix="/api/posts",
    tags=["Posts API"],
)


@router.get("/", response_model=list[schemas.Post])
def get_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = service.get_posts(db, skip, limit)
    return posts


@router.get("/latest", response_model=schemas.Post)
def get_latest_post(db: Session = Depends(get_db)):
    latest_post = service.get_latest_post(db=db)
    return latest_post


@router.get("/{post_id}", response_model=schemas.Post)
def get_post_by_id(post_id: Annotated[int, Path(ge=1)], db: Session = Depends(get_db)):
    post = service.get_post(db, post_id)
    return post


@router.post("/", response_model=schemas.Post)
def create_post(
    title: Annotated[str, Form()],
    content: Annotated[str, Form()],
    db: Session = Depends(get_db),
):
    post = schemas.PostCreate(title=title, content=content)
    return service.create_post(db, post)
