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

@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}