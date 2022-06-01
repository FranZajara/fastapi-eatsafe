from cgitb import html
from fastapi import FastAPI, Request, Form
import json

from urllib3 import HTTPResponse
from funciones import *
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pdfkit
from xhtml2pdf import pisa
from io import BytesIO
from jinja2 import Environment, PackageLoader



app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.post("/analisis/", response_class=HTMLResponse)
async def analisis( request: Request,
                nombre: str = Form(...), 
                edad: int = Form(...), 
                peso: int = Form(...),
                sexo: str = Form(...),
                altura: int = Form(...),
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
    
    #guardamos el indice de masa corporal del paciente
    imc = IMC(peso,altura)
    
    #guardamos el indice metabolico basal del paciente
    imb = IMB(sexo,altura,peso,edad)
    
    #guardamos en una variable si el paciente presenta o no el trastorno de Pica.
    if (Pica(cuestion1,cuestion2) == True):
        pica = "El paciente probablemente presenta el trastorno alimentario de Pica."
    else:
        pica = "El paciente no presenta el trastorno alimentario de Pica."
    
    #guardamos en una variable si el paciente presenta o no el trastorno de Pica.
    if(Rumiacion(cuestion3) == True):
        rumiacion = "El paciente probablemente presenta el trastorno alimentario de Rumiación."
    else:
        rumiacion = "El paciente no presenta el trastorno alimentario de Rumiación."

    #guardamos en una variable si el paciente presenta o no el trastorno de evitación.
    if (Evitacion(cuestion4,cuestion5) == True):
        evitacion = "El paciente probablemente presenta el trastorno alimentario de Evitación."
    else:
        evitacion = "El paciente no presenta el trastorno alimentario de Evitación."
    
    #guardamos en una variable si el paciente presenta o no el trastorno de Anorexia nerviosa.
    if(Anorexia(cuestion4,cuestion6,cuestion7,cuestion8,cuestion9) == True):
        anorexia = "El paciente probablemente presenta el trastorno alimentario de Anorexia nerviosa, "
        if((cuestion8 == 1) | (cuestion9 == 1) | (cuestion10 == 1)):
            tipoanorexia = "tipo con atracones o purgas, "
        else:
            tipoanorexia = "tipo restrictivo, "
        
        if(imc >= 17):
            severidad = "severidad leve."
        elif(16 <= imc < 17):
            severidad = "severidad moderada."
        elif(15 <= imc < 16):
            severidad = "severidad grave."
        else:
            severidad = "severidad extrema."
        anorexia = anorexia + tipoanorexia + severidad
    else:
        anorexia = "El paciente no presenta el trastorno alimentario de Anorexia nerviosa."
    
    
    if(Bulimia(cuestion10,cuestion11,cuestion9,cuestion12,cuestion13,cuestion16) == True):
        bulimia = "El paciente probablemente presenta el trastorno alimentario de Bulimia nerviosa, "
        if(cuestion16 == 0):
            severidad2 = "severidad leve."
        elif(cuestion16 == 1):
            severidad2 = "severidad moderada."
        elif(cuestion16 == 2):
            severidad2 = "severidad grave."
        else:
            severidad2 = "severidad extrema."
        bulimia = bulimia + severidad2
    else:
        bulimia = "El paciente no presenta el trastorno alimentario de Bulimia nerviosa."

    cuenta = len(cuestion14)

    if(Atracon(cuestion10,cuestion11, cuenta, cuestion13) == True):
        atracon = "El paciente probablemente presenta el trastorno alimentario de Atracones, "
        if(cuestion13 == 0):
            severidad3 = "severidad leve."
        elif(cuestion13 == 1):
            severidad3 = "severidad moderada."
        elif(cuestion13 == 2):
            severidad3 = "severidad grave."
        else:
            severidad3 = "severidad extrema."
        atracon = atracon + severidad3
    
    else:
        atracon = "El paciente no presenta el trastorno alimentario de Atracones."

    if(Nocturno(cuestion15) == True):
        nocturno = "El paciente probablemente presenta el síndrome de ingestión nocturna de alimentos."
    else:
        nocturno = "El paciente no presenta el síndrome de ingestión nocturna de alimentos."
   
    
    
    return             templates.TemplateResponse ("analisis.html", {
                                                         "request" : request,
                                                        "nombre" : nombre, 
                                                        "edad" : edad,
                                                        "peso" : peso,
                                                        "sexo" : sexo,
                                                        "altura" : altura,
                                                        "imc" : imc,
                                                        "imb" : imb,
                                                        "pica" : pica,
                                                        "rumiacion" : rumiacion,
                                                        "evitacion" : evitacion,
                                                        "anorexia" : anorexia,
                                                        "bulimia" : bulimia,
                                                        "atracon" : atracon,
                                                        "nocturno" : nocturno
                                                        })
   