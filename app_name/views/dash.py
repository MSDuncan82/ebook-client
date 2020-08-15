
from app_name import app, templates
from fastapi import Request

@app.get("/")
async def index(request: Request):
    """Home page"""

    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/board")
async def board(request: Request):
    """Embedded dashboard"""

    return templates.TemplateResponse("dash.html", {"request": request})