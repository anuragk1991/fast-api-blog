from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
	{
		"id": 1,
		"title": "First Post",
		"content": "A test post whith some description",
		"author": "Anurag",
		"date_posted": "June 5th, 2026"
	},
	{
		"id": 2,
		"title": "Another Post",
		"content": "A slightly different post from large body of ponds",
		"author": "Amit",
		"date_posted": "June 15th, 2026"
	}

]
@app.get("/posts", include_in_schema=False)
@app.get("/", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Home"})


@app.get("/api/posts")
def get_posts():
	return posts