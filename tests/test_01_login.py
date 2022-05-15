from fastapi.testclient import TestClient
from main import app
from src.schemas.login import LoginIn


client = TestClient(app)


def test_entrar():
    body = LoginIn(txtEmail="<txtEmail>", txtSenha="<txtSenha>")
    response = client.post(url="/login/entrar", json={"txtEmail": body.txtEmail, "txtSenha": body.txtSenha})
    content = response.json()
    assert response.status_code == 200
    assert content["Email"] == body.txtEmail


def test_logado():
    response = client.get("/login/logado")
    assert response.status_code == 200

# pytest
# pytest -v
# pytest -vv
