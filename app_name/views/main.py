from app_name import app, templates
from fastapi import Request

@app.get("/")
async def index(request: Request):
    """Home page"""

    my_image = "https://media-exp1.licdn.com/dms/image/C4D35AQESWyM0aSBHOw/profile-framedphoto-shrink_200_200/0?e=1597608000&v=beta&t=CpQDRFg5v0YGQwBICStA7TbaHpkNLsNlqWWS2tFeiYk"
    full_name = 'Michael Duncan'
    first_name, last_name = full_name.split()

    return templates.TemplateResponse("index.html", {"request": request, "my_image": my_image, "name":first_name})

@app.get("/tutorial")
async def tutorial():
    """ This is a tutorial function, to use this run curl http://0.0.0.0:5700/tutorial """
    return {'message': {'this is another route'}}