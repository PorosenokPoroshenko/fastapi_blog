from fastapi import APIRouter, Path, Depends 
from sqlalchemy.orm import Session
from typing import Annotated

from src.posts import models, crud, schemas
from src.database import SessionLocal

router = APIRouter(
    prefix="/posts",
    tags=["Posts"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Post])
def read_posts(skip: int = 0, limit:int = 100, db: Session = Depends(get_db)):
    posts = crud.get_posts(db, skip, limit) 
    return posts

@router.get("/latest", response_model=schemas.Post)
def get_latest_post(db: Session = Depends(get_db)):
    latest_post = crud.get_latest_post(db=db)
    return latest_post

@router.get("/{post_id}", response_model=schemas.Post)
def get_post_by_id(post_id: Annotated[int, Path(ge=1)], db: Session = Depends(get_db)):
    post = crud.get_post(db, post_id)
    return post 

@router.post("/create_post", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db, post)