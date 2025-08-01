from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.translator import translate_text

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/translate", response_class=HTMLResponse)
def translate(request: Request, text: str = Form(...), from_lang: str = Form(...), to_lang: str = Form(...)):
    result = translate_text(text, from_lang, to_lang)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": result,
        "text": text,
        "from_lang": from_lang,
        "to_lang": to_lang
    })
