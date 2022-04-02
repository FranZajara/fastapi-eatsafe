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
    

class Post(BaseModel):
    C1: int
    C2: int
    C3: int
    C4: int

@app.post('/posts')
def save_post(post: Post):
    print (post)
    return 'recibido'