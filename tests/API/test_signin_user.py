
from helper import *


def test_sign_in_successful():
    response = sign_in_user()
    assert response.status_code == 200
    assert response.json()["status_code"] == 200
    assert response.json()["status"] == "Pass"
    assert response.json()["data"] == {
        "id": "001",
        "first_name": "John",
        "last_name": "Doe",
        "permission": "admin"
    }
    assert response.json()["message"] == "Sign in success"


def test_sign_in_failed():
    response = sign_in_user(1, 3)
    assert response.status_code == 404
    assert response.json()["status_code"] == 404
    assert response.json()["status"] == "Not found"
    assert response.json()["data"] == {}
    assert response.json()["message"] == "User not found"
