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
                cuestion6: int = Form(...),
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
    
    
    return                                            ( {"request" : request, 
                                                        "nombre" : nombre, 
                                                        "edad" : edad,
                                                        "peso" : peso,
                                                        "sexo" : sexo,
                                                        "cuestion1" : cuestion1,
                                                        "cuestion2" : cuestion2,
                                                        "cuestion3" : cuestion3,
                                                        "cuestion4" : cuestion4,
                                                        "cuestion5" : cuestion5,
                                                        "cuestion6" : cuestion6,
                                                        "cuestion7" : cuestion7,
                                                        "cuestion8" : cuestion8,
                                                        "cuestion9" : cuestion9,
                                                        "cuestion10" : cuestion10,
                                                        "cuestion11" : cuestion11,
                                                        "cuestion12" : cuestion12,
                                                        "cuestion13" : cuestion13,
                                                        "cuestion14" : cuestion14,
                                                        "cuestion15" : cuestion15,
                                                        "cuestion16" : cuestion16})
   