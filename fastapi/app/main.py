from fastapi import FastAPI
from miniLM import getEmbeddings

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "OK"}

@app.get("/hello")
def hello_world():
    embeddings = getEmbeddings()
    embeddingsListSize = len(embeddings)
    return {"Status": "Success", "embeddings" : embeddingsListSize}