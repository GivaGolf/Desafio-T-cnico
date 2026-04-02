import sys
import os
import uuid

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_register():
    email_unico = f"{uuid.uuid4()}@email.com"

    response = client.post("/auth/register", json={
        "email": email_unico,
        "password": "123456"
    })

    print("REGISTER:", response.json())

    assert response.status_code == 200


def test_login():
    email_unico = f"{uuid.uuid4()}@email.com"

    client.post("/auth/register", json={
        "email": email_unico,
        "password": "123456"
    })

    response = client.post("/auth/login", json={
        "email": email_unico,
        "password": "123456"
    })

    print("LOGIN:", response.json())

    assert response.status_code == 200
    assert "access_token" in response.json()["data"]


def test_login_invalido():
    response = client.post("/auth/login", json={
        "email": "naoexiste@email.com",
        "password": "123456"
    })

    assert response.status_code == 401


def get_token():
    email_unico = f"{uuid.uuid4()}@email.com"

    client.post("/auth/register", json={
        "email": email_unico,
        "password": "123456"
    })

    response = client.post("/auth/login", json={
        "email": email_unico,
        "password": "123456"
    })

    return response.json()["data"]["access_token"]


def test_rota_protegida():
    token = get_token()

    response = client.get(
        "/protegido",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200


def test_token_invalido():
    response = client.get(
        "/clientes",
        headers={"Authorization": "Bearer token_invalido"}
    )

    assert response.status_code == 401