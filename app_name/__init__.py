from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.wsgi import WSGIMiddleware
from dash_app import app_dash
# Now create your regular FASTAPI application

app = FastAPI()

app.mount("/static", StaticFiles(directory="./app_name/static"), name="static")
templates = Jinja2Templates(directory="./app_name/templates")

app.mount("/dash", WSGIMiddleware(app_dash.server))
from app_name.views import main, tasks, dash