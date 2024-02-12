from fastapi import FastAPI, Request, Depends
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager

import uvicorn
from datetime import datetime

from src.posts.router import router as posts_api_router
from src.handlers import router as pages_router
from src.database import Base, engine
from src.posts.models import Post


Base.metadata.create_all(bind=engine)

with Session(engine) as session:
    example_post = Post(
        title="Example post", content="lorem ipsum", date=datetime.now()
    )
    session.add(example_post)
    session.commit()

app = FastAPI()
app.include_router(posts_api_router)
app.include_router(pages_router)
app.mount("/static", StaticFiles(directory="static"), name="static")


if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True)
