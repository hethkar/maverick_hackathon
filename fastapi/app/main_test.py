from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}
    
def test_hello_world():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"Status": "Success", "output" : "Hello Mavericks!"}
    
def test_hello_mini_llm():
    response = client.get("/helloMiniLLM")
    assert response.status_code == 200
    assert response.json() == {"Status": "Success", "embeddings" : 2}
    
def test_create_item():
    requestBody = {"name": "Sandeep", "description" : "sample"}
    response = client.post(url = "/items/", json = {"name": "Sandeep", "description" : "sample"})
    assert response.status_code == 200
    assert response.json() == requestBody