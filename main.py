from fastapi import FastAPI, Request
import json


app = FastAPI()

@app.get('/inicio')
async def rutadeprueba():
    return "Hola desde FastAPI"

@app.get("/mul")
async def calc(request:Request):
    num1= int(request.form.get('num1'))
    num2= int(request.form.get('num2'))
    return num1*num2
    


@app.post('/posts')
def fetch(self,page=1):
     request = fetch(self.url(page))
     if self.mode == 'object':
         return json.load(request)
     else:
         return request.read()