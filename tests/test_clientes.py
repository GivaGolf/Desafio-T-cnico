import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def get_token():
    client.post("/auth/register", json={
        "email": "cliente@email.com",
        "password": "123456"
    })

    response = client.post("/auth/login", json={
        "email": "cliente@email.com",
        "password": "123456"
    })

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

    assert response.status_code == 200


def test_listar_clientes():
    token = get_token()

    response = client.get(
        "/clientes",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert isinstance(response.json()["data"], list)


def test_buscar_cliente():
    token = get_token()

    create = client.post(
        "/clientes",
        json={
            "nome": "Maria",
            "email": "maria@email.com",
            "telefone": "888888888"
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    cliente_id = create.json()["data"]["id"]

    response = client.get(
        f"/clientes/{cliente_id}",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200


def test_atualizar_cliente():
    token = get_token()

    create = client.post(
        "/clientes",
        json={
            "nome": "Pedro",
            "email": "pedro@email.com",
            "telefone": "777777777"
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    cliente_id = create.json()["data"]["id"]

    response = client.put(
        f"/clientes/{cliente_id}",
        json={
            "nome": "Pedro Atualizado",
            "email": "pedro@email.com",
            "telefone": "777777777"
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200


def test_deletar_cliente():
    token = get_token()

    create = client.post(
        "/clientes",
        json={
            "nome": "Ana",
            "email": "ana@email.com",
            "telefone": "666666666"
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    cliente_id = create.json()["data"]["id"]

    response = client.delete(
        f"/clientes/{cliente_id}",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200


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