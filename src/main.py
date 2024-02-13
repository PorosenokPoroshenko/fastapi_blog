from fastapi import FastAPI, Request, Depends
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager

import uvicorn
from datetime import datetime

from .posts.router import router as posts_api_router
from .handlers import router as pages_router
from .database import Base, engine
from .posts.models import Post


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)

    with Session(engine) as session:
        example_post = Post(title="Example post", content="lorem ipsum")
        session.add(example_post)
        session.commit()

    yield

    Base.metadata.drop_all(engine)


app = FastAPI(lifespan=lifespan)
app.include_router(posts_api_router)
app.include_router(pages_router)
app.mount("/static", StaticFiles(directory="static"), name="static")


if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True)
