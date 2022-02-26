from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_read_root():
    response = client.get("/users") # /?skip=0&limit=10
    assert response.status_code == 500
    # assert response.json() == ("message": "Hello World")

# pytest

'''

from fastapi.testclient import TestClient

def test_get_root(client: TestClient) -> None:
    response = client.get("/")
    body = response.json()
    assert response.status_code == 200
    assert body["mensagem"] == "api de papeis"
    
    
from fastapi.testclient import TestClient
from models.papel import Papel
from tests.utils.papeis import create_papel_valido

def test_cria_papel(client: TestClient) -> None:
    body = create_papel_valido()
    response = client.post("/papeis/", json=body)
    content = response.json()
    assert response.status_code == 200
    assert content["cnpj"] == body["cnpj"]
    
    
    
    
    
'''

#
#
# from fastapi.testclient import TestClient
#
# from main import app
#
# client = TestClient(app)
#
# data = {
#     "name": "IsaiahT-Tech",
#     "due_date": "Today",
#     "description": "string"
# }
#
# def test_create_todo():
#     response = client.post("/todo/", json=data)
#     assert response.status_code == 200
#     assert response.json() == data
#
# def test_get_all_todo():
#     response = client.get("/todo/", json=data)
#     assert response.status_code == 200
#     assert data in response.json()
#
# def test_get_todo():
#     response = client.get("/todo/0")
#     assert response.status_code == 200
#     assert response.json() == data
#
# def test_update_todo():
#     response = client.put("/todo/0", json = {
#         "name": "Test",
#         "due_date": "Now",
#         "description": "Python"
#     })
#     assert response.status_code == 200
#     assert response.json() == {
#         "name": "Test",
#         "due_date": "Now",
#         "description": "Python"
#     }
#
# def test_delete_todo():
#     response = client.delete("/todo/0")
#     assert response.status_code == 200
#     assert response.json() == {
#         "name": "Test",
#         "due_date": "Now",
#         "description": "Python"
#     }


# from unittest import mock
#
# import pytest
# from fastapi.testclient import TestClient
#
# from .repositories import UserRepository, UserNotFoundError
# from .models import User
# from .application import app
#
#
# @pytest.fixture
# def client():
#     yield TestClient(app)
#
#
# def test_get_list(client):
#     repository_mock = mock.Mock(spec=UserRepository)
#     repository_mock.get_all.return_value = [
#         User(id=1, email="test1@email.com", hashed_password="pwd", is_active=True),
#         User(id=2, email="test2@email.com", hashed_password="pwd", is_active=False),
#     ]
#
#     with app.container.user_repository.override(repository_mock):
#         response = client.get("/users")
#
#     assert response.status_code == 200
#     data = response.json()
#     assert data == [
#         {"id": 1, "email": "test1@email.com", "hashed_password": "pwd", "is_active": True},
#         {"id": 2, "email": "test2@email.com", "hashed_password": "pwd", "is_active": False},
#     ]
#
#
# def test_get_by_id(client):
#     repository_mock = mock.Mock(spec=UserRepository)
#     repository_mock.get_by_id.return_value = User(
#         id=1,
#         email="xyz@email.com",
#         hashed_password="pwd",
#         is_active=True,
#     )
#
#     with app.container.user_repository.override(repository_mock):
#         response = client.get("/users/1")
#
#     assert response.status_code == 200
#     data = response.json()
#     assert data == {"id": 1, "email": "xyz@email.com", "hashed_password": "pwd", "is_active": True}
#     repository_mock.get_by_id.assert_called_once_with(1)
#
#
# def test_get_by_id_404(client):
#     repository_mock = mock.Mock(spec=UserRepository)
#     repository_mock.get_by_id.side_effect = UserNotFoundError(1)
#
#     with app.container.user_repository.override(repository_mock):
#         response = client.get("/users/1")
#
#     assert response.status_code == 404
#
#
# @mock.patch("webapp.services.uuid4", return_value="xyz")
# def test_add(_, client):
#     repository_mock = mock.Mock(spec=UserRepository)
#     repository_mock.add.return_value = User(
#         id=1,
#         email="xyz@email.com",
#         hashed_password="pwd",
#         is_active=True,
#     )
#
#     with app.container.user_repository.override(repository_mock):
#         response = client.post("/users")
#
#     assert response.status_code == 201
#     data = response.json()
#     assert data == {"id": 1, "email": "xyz@email.com", "hashed_password": "pwd", "is_active": True}
#     repository_mock.add.assert_called_once_with(email="xyz@email.com", password="pwd")
#
#
# def test_remove(client):
#     repository_mock = mock.Mock(spec=UserRepository)
#
#     with app.container.user_repository.override(repository_mock):
#         response = client.delete("/users/1")
#
#     assert response.status_code == 204
#     repository_mock.delete_by_id.assert_called_once_with(1)
#
#
# def test_remove_404(client):
#     repository_mock = mock.Mock(spec=UserRepository)
#     repository_mock.delete_by_id.side_effect = UserNotFoundError(1)
#
#     with app.container.user_repository.override(repository_mock):
#         response = client.delete("/users/1")
#
#     assert response.status_code == 404
#
#
# def test_status(client):
#     response = client.get("/status")
#     assert response.status_code == 200
#     data = response.json()
#     assert data == {"status": "OK"}