from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

posts = [
    {"id": 1, "title": "First Post", "content": "This is the first post."},
    {"id": 2, "title": "Second Post", "content": "This is the second post."},
]

@app.get("/")
@app.get("/posts")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {
        "request": request,
        "posts": posts,
        "title": "Home"
    })

@app.get("/posts/{post_id}", response_class=HTMLResponse)
async def get_post(post_id: int):
    return f"<h1>Post {post_id}</h1>"