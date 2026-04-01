from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

clientes = []

class Cliente(BaseModel):
    nome: str
    email: str
    telefone: str

@app.post("/clientes")
def criar_cliente(dados: Cliente):
    novo_cliente = {
        "id": len(clientes) + 1,
        "nome": dados.nome,
        "email": dados.email,
        "telefone": dados.telefone,
        "created_at": datetime.now()
    }
    clientes.append(novo_cliente)
    return novo_cliente

@app.get("/clientes")
def listar_clientes():
    return clientes

@app.put("/clientes/{cliente_id}")
def atualizar_cliente(cliente_id: int, dados: Cliente):
    for cliente in clientes:
        if cliente["id"] == cliente_id:
            cliente["nome"] = dados.nome
            cliente["email"] = dados.email
            cliente["telefone"] = dados.telefone
            return cliente

    raise HTTPException(status_code=404, detail="Cliente não encontrado")

@app.delete("/clientes/{cliente_id}")
def deletar_cliente(cliente_id: int):
    for cliente in clientes:
        if cliente["id"] == cliente_id:
            clientes.remove(cliente)
            return {"mensagem": "Cliente removido com sucesso"}

    raise HTTPException(status_code=404, detail="Cliente não encontrado")