from app_name import app, templates
from fastapi import Request
from datetime import datetime
import re

def clean_phone(phone_num):
    return "".join(re.findall("[\d-]", phone_num))

@app.get("/")
async def index(request: Request):
    """Home page"""
    date = datetime.today().strftime("%b %d, %Y")

    html_args = dict(
    image_url = "https://media-exp1.licdn.com/dms/image/C4D35AQESWyM0aSBHOw/profile-framedphoto-shrink_200_200/0?e=1599048000&v=beta&t=WDvS-Y_xlvWQfICiEsGAo7e-rxKeTszho1qlSzYTVaY",
    full_name = "Michael Duncan",
    headline = "Super Cool Guy | Climber Bro",
    current_job = "Executive Chiller",
    current_company = "Bros Chill inc.",
    company_link = "https://www.linkedin.com//company/galvanize-it/",
    phone=clean_phone("406-546-0438\n (Home)"),
    email="msduncan82@gmail.com",
    date=date,
    notes="Here are some notes.\nI wonder if line breaks work?\nHopefully!"
    )

    first_name, last_name = html_args['full_name'].split()
    html_args.update(dict(first_name=first_name, last_name=last_name))

    return templates.TemplateResponse(
        "brython.html",
        {
            "request": request,
            **html_args
        },
    )


@app.get("/tutorial")
async def tutorial():
    """ This is a tutorial function, to use this run curl http://0.0.0.0:5700/tutorial """
    return {"message": {"this is another route"}}
