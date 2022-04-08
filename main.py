from fastapi import FastAPI, Request, Form
import json
from pydantic import BaseModel
from funciones import *
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get('/inicio')
async def rutadeprueba():
    return "Hola desde FastAPI"

@app.get("/mul")
async def calc(request:Request):
    num1= int(request.form.get('num1'))
    num2= int(request.form.get('num2'))
    return num1*num2
    
class Respuestas(BaseModel):
    number1: int
    number: int

    class Config:
        orm_mode = True

@app.post('/posts')
async def create(respuesta: Respuestas):
    return respuesta
    
    #return Pica(respuesta[0], respuestaj[1])

@app.post("/analisis/", response_class=HTMLResponse)
async def analisis(request = Request, nombre: str = Form(...), 
                edad: int = Form(...), 
                peso: int = Form(...),
                sexo: str = Form(...),
                cuestion1: int = Form(...),
                cuestion2: int = Form(...),
                cuestion3: int = Form(...),
                cuestion4: int = Form(...),
                cuestion5: int = Form(...),
                cuestion7: int = Form(...),
                cuestion8: int = Form(...),
                cuestion9: int = Form(...),
                cuestion10: int = Form(...),
                cuestion11: int = Form(...),
                cuestion12: int = Form(...),
                cuestion13: int = Form(...),
                cuestion14: list = Form(...),
                cuestion15: int = Form(...),
                cuestion16: int = Form(...)):
    
    
    return templates.TemplateResponse("analisis.html", {"request" : request, "cuestion14" : cuestion14})
   