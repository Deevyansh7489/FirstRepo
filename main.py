from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def app_func():
    return {"message": "Hello, World!"}

@app.get("/hello-deevyansh")
async def hello_deevyansh():
    return {"message": "Hello from Deevyansh!"}