from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from parsers import *
from config import metadata

app = FastAPI(
    title="WebTemplate"
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

github = metadata['integrations']['github']
telegram_channel = metadata['integrations']['telegram_channel']
x = metadata['integrations']['x']
linkedin = metadata['integrations']['linkedin']
socials = [
    {"title": "GitHub", "link": f"https://github.com/{github}"} if github else None,
    {"title": "Telegram", "link": f"https://t.me/s/{telegram_channel}"} if telegram_channel else None,
    {"title": "X", "link": f"https://x.com/{x}"} if x else None,
    {"title": "LinkedIn", "link": f"https://www.linkedin.com/in/{linkedin}"} if linkedin else None,
]
metadata['socials'] = socials

repositories = getGitHubRepositories(username=metadata['integrations']['github'])
posts = getTelegramChannelPosts(channel_name=metadata['integrations']['telegram_channel'])

@app.get("/", response_class=HTMLResponse)
async def getMainPage(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="main.html",
        context={
            'metadata': metadata,
            'repositories': repositories,
            'posts': posts,
        }
    )