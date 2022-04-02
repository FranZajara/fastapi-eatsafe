from fastapi import FastAPI, Request
import json
from pydantic import BaseModel

app = FastAPI()

@app.get('/inicio')
async def rutadeprueba():
    return "Hola desde FastAPI"

@app.get("/mul")
async def calc(request:Request):
    num1= int(request.form.get('num1'))
    num2= int(request.form.get('num2'))
    return num1*num2
    
def Pica(C1, C2):
    if(((C1 == 1) & (C2 == 1)) | ((C1 == 1) & (C2 == 0))):
        return True
    elif((C1 == 0) & (C2 == 1)):
        return False
    else:
        return False


class Respuestas(BaseModel):
    number1: int
    number: int

@app.post('/posts')
async def create(respuesta: Respuestas):
    return Pica(respuesta.number1, respuesta.number)