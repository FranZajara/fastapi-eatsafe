from fastapi import FastAPI, Request
import json
from pydantic import BaseModel
#from funciones import *

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

#@app.post('/posts')
#async def create(respuesta: Respuestas):
   # return Pica(respuesta.number1, respuesta.number)