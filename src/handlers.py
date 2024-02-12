from src.posts import router as api
from fastapi import APIRouter, Request, Path, Depends, Form
from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from sqlalchemy.orm import Session
from src.database import get_db

router = APIRouter(tags=["www"])

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/posts", response_class=HTMLResponse)
def read_posts(request: Request, db: Session = Depends(get_db)):
    posts = api.get_posts(db=db)
    context = dict(request=request, posts=posts)
    return templates.TemplateResponse("posts.html", context)


@router.get("/posts/{post_id}", response_class=HTMLResponse)
def read_post(
    request: Request, post_id: Annotated[int, Path(ge=1)], db: Session = Depends(get_db)
):
    post = api.get_post_by_id(post_id, db)
    context = dict(request=request, post=post)
    return templates.TemplateResponse("post.html", context)


@router.get("/create_post", response_class=HTMLResponse)
def read_create_post(request: Request):
    context = dict(request=request)
    return templates.TemplateResponse("create_post.html", context)


@router.post("/create_post", response_class=HTMLResponse)
def read_create_post(
    request: Request,
    title: Annotated[str, Form()],
    content: Annotated[str, Form()],
    db: Session = Depends(get_db),
):
    new_post = api.create_post(title, content, db)
    context = dict(request=request, message="Post successfully created")
    return templates.TemplateResponse("create_post.html", context)
