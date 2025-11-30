import json
from src.app import app

def test_run():
    client = app.test_client()
    res = client.get("/run")
    assert res.status_code == 200

def test_data():
    client = app.test_client()
    client.get("/run")
    res = client.get("/data")
    assert isinstance(res.json, list)