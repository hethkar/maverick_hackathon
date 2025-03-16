from fastapi import FastAPI
from miniLLM import getEmbeddings
from sample import hello
import logging
from sentence_transformers import SentenceTransformer
import torch
from opensearchpy import OpenSearch
from vecconfig import INDEX_NAME
import env

from pydantic import BaseModel
from typing import Optional

logging.basicConfig(level=logging.INFO)

class Item(BaseModel):
    name: str
    description: Optional[str] = None

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
def hello_mini_llm():
    logging.info("Hello MiniLLM API called")
    embeddings = getEmbeddings()
    embeddingsListSize = len(embeddings)
    return {"Status": "Success", "embeddings" : embeddingsListSize}

@app.post("/items/")
async def create_item(item: Item):
    return item


@app.post("/search_customer")
def search_customer(query: str):
    logging.info("Hello Search Customer called")
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    # check if GPU is available and use it
    if torch.cuda.is_available():
        model = model.to(torch.device("cuda"))
        print(model.device)
    query_embeddings = model.encode(query, show_progress_bar=True)
    # Define OpenSearch connection parameters
    client = OpenSearch(
        hosts=[{"host": env.elastic_server_host, "port": env.elastic_server_port}],
        http_compress=True,
        use_ssl=False,
        verify_certs=False,
        http_auth=(env.opensearch_rest_username, env.opensearch_rest_password),
    )

    # Check connection
    try:
        info = client.info()
        print("Connected to OpenSearch:", info)
    except Exception as e:
        print("Error connecting to OpenSearch:", e)
    # Define KNN query
    knn_query = {
        "size": 5,  # Number of nearest neighbors to retrieve
        "query": {
            "knn": {
                "compositevector_vector": {
                    "vector": query_embeddings.tolist(),
                    "k": 5,
                }
            }
        }
    }
    # Execute Search
    response = client.search(index=INDEX_NAME, body=knn_query)

    # Print search results
    for hit in response['hits']['hits']:
        print(f"ID: {hit['_id']}, Score: {hit['_score']}, Source: {hit['_source']}")
    # Filter results where score > 0.65
    filtered_results = [
        hit for hit in response["hits"]["hits"] if hit["_score"] > 0.65
    ]

    return {"results": filtered_results}
