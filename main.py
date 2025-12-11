from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def app_func():
    return {"message": "Hello, World!"}
