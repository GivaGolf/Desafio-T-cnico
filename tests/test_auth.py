import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def get_token():
    client.post("/auth/register", json={
        "email": "teste@teste.com",
        "password": "123456"
    })

    response = client.post("/auth/login", json={
        "email": "teste@teste.com",
        "password": "123456"
    })

    print("LOGIN RESPONSE:", response.json())

    return response.json()["data"]["access_token"]


def test_criar_cliente():
    token = get_token()

    response = client.post(
        "/clientes",
        json={
            "nome": "João",
            "email": "joao@email.com",
            "telefone": "999999999"
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    print("CREATE RESPONSE:", response.json())

    assert response.status_code == 200


def test_listar_clientes():
    token = get_token()

    response = client.get(
        "/clientes",
        headers={"Authorization": f"Bearer {token}"}
    )

    print("LIST RESPONSE:", response.json())

    assert response.status_code == 200

def test_login_invalido():
    response = client.post("/auth/login", json={
        "email": "naoexiste@email.com",
        "password": "123456"
    })

    assert response.status_code == 401

def test_rota_protegida():
    token = get_token()   # ✅ tem espaço antes

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


def test_atualizar_cliente_inexistente():
    token = get_token()

    response = client.put(
        "/clientes/999",
        json={
            "nome": "X",
            "email": "x@email.com",
            "telefone": "000"
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 404


def test_deletar_cliente_inexistente():
    token = get_token()

    response = client.delete(
        "/clientes/999",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 404