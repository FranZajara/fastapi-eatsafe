from fastapi import FastAPI

app = FastAPI()

@app.get('/inicio')
async def rutadeprueba():
    return "Hola desde FastAPI"

@app.post('/quiero/<num1>/<num2>')
def mul(num1,num2):
    return num1*num2
