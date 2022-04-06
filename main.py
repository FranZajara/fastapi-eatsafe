from fastapi import FastAPI, Request, Form
import json
from pydantic import BaseModel
from funciones import *
from fastapi.encoders import jsonable_encoder

app = FastAPI()

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

@app.post('/form')
async def formulario(number1: str == Form(...), number: str == Form(...)):
    return {'number1': number1 , 'number': number}