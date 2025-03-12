from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "OK"}

@app.get("/hello")
def hello_world():
    return {"Status": "Success"}