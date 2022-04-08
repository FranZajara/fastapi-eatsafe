from fastapi import FastAPI, Request, Form
import json
from pydantic import BaseModel
from funciones import *
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")

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
    
    
    return templates.TemplateResponse("analisis.html", {"request" : request, 
                                                        "nombre" : nombre, 
                                                        "edad" : edad,
                                                        "peso" : peso,
                                                        "sexo" : sexo,
                                                        "cuestion 1" : cuestion1,
                                                        "cuestion 2" : cuestion1,
                                                        "cuestion 3" : cuestion1,
                                                        "cuestion 4" : cuestion1,
                                                        "cuestion 5" : cuestion1,
                                                        "cuestion 6" : cuestion1,
                                                        "cuestion 7" : cuestion1,
                                                        "cuestion 8" : cuestion1,
                                                        "cuestion 9" : cuestion1,
                                                        "cuestion 10" : cuestion1,
                                                        "cuestion 11" : cuestion1,
                                                        "cuestion 12" : cuestion1,
                                                        "cuestion 13" : cuestion1,
                                                        "cuestion 14" : cuestion1,
                                                        "cuestion 15" : cuestion1,
                                                        "cuestion 16" : cuestion1})
   