from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/items/")
def read_items(q: str | None = None):
    return {"q": q}


client = TestClient(app)


def test_query_params_empty_keys_ignored():
    # Sending a request with empty keys (e.g. dangling '&' or '?=')
    response = client.get("/items/?=&q=test&")
    assert response.status_code == 200, response.text
    assert response.json() == {"q": "test"}


from fastapi.dependencies.utils import request_params_to_args
from fastapi.utils import create_model_field
from starlette.datastructures import Headers, ImmutableMultiDict


def test_request_params_to_args_headers_empty_keys_ignored():
    headers = Headers(raw=[(b"", b"empty"), (b"x-test", b"value")])
    field = create_model_field(name="x_test", type_=str, default=None)
    values, errors = request_params_to_args([field], headers)
    assert values.get("x_test") == "value"


def test_request_params_to_args_immutable_multi_dict_empty_keys_ignored():
    imd = ImmutableMultiDict([("", "empty"), ("q", "test")])
    field = create_model_field(name="q", type_=str, default=None)
    values, errors = request_params_to_args([field], imd)
    assert values.get("q") == "test"


def test_request_params_to_args_dict_empty_keys_ignored():
    d = {"": "empty", "q": "test"}
    field = create_model_field(name="q", type_=str, default=None)
    values, errors = request_params_to_args([field], d)
    assert values.get("q") == "test"
