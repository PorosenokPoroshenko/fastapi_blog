from fastapi import FastAPI, Request, Depends
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from contextlib import asynccontextmanager

import uvicorn
from datetime import datetime

from src.posts.router import router as posts_router
from src.database import Base, engine 
from src.posts.models import Post




Base.metadata.create_all(bind=engine)

with Session(engine) as session:
    example_post = Post(title="Example post", content="lorem ipsum", date = datetime.now())
    session.add(example_post)
    session.commit()



app = FastAPI()
app.include_router(posts_router)
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request}) 


if __name__ == '__main__':
    uvicorn.run("src.main:app", reload=True)