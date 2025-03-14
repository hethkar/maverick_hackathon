from fastapi import FastAPI
from miniLLM import getEmbeddings
from sample import hello
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.get("/")
def index():
    logging.info("Index API called")
    return {"message": "OK"}

@app.get("/hello")
def hello_world():
    logging.info("hello API called")
    return {"Status": "Success", "output" : hello}

@app.get("/helloMiniLLM")
def hello_world():
    logging.info("Hello MiniLLM API called")
    embeddings = getEmbeddings()
    embeddingsListSize = len(embeddings)
    return {"Status": "Success", "embeddings" : embeddingsListSize}
