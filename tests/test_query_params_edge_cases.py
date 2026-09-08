from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/query/")
def read_query(q: str | None = None):
    return {"q": q}


client = TestClient(app)


def test_query_params_empty_keys_ignored():
    response = client.get("/query/?=&q=test&")
    assert response.status_code == 200
    assert response.json() == {"q": "test"}
