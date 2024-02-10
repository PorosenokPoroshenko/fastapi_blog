from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

import uvicorn

from posts.router import router as posts_router

app = FastAPI()
app.include_router(posts_router)
templates = Jinja2Templates(directory="templates")


def on_startup():
    pass

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request}) 


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)