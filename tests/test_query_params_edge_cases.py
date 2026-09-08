from typing import Optional
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get("/items/")
def read_items(q: Optional[str] = None):
    return {"q": q}

client = TestClient(app)

def test_query_params_empty_keys_ignored():
    # Sending a request with empty keys (e.g. dangling '&' or '?=')
    response = client.get("/items/?=&q=test&")
    assert response.status_code == 200, response.text
    assert response.json() == {"q": "test"}
