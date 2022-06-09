from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

def test_clssify_card():
    response = client.get("/card_id/286", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json() ==  {"result_predict":"early","card_name":"Rebel Quartermaster"}

def test_invalid_card():
    response = client.get("/card_id/286i", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 422
    assert response.json() ==  {"detail":[{"loc":["path","card_id"],"msg":"value is not a valid integer","type":"type_error.integer"}]}

def test_no_card():
    response = client.get("/card_id/", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 404
    assert response.json() ==  {"detail":"Not Found"}

def test_inexistent_card():
    response = client.get("/card_id/11111111111111", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 404
    assert response.json() ==  {"detail":"Item not found"}