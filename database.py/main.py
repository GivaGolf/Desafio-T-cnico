from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import engine, SessionLocal
from models import Base
import models, schemas

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

# cria as tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI()

# conexão com banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRIAR CLIENTE
@app.post("/clientes", response_model=schemas.ClienteResponse)
def criar_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    novo_cliente = models.Cliente(nome=cliente.nome, email=cliente.email)
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)
    return novo_cliente

# LISTAR CLIENTES
@app.get("/clientes", response_model=list[schemas.ClienteResponse])
def listar_clientes(db: Session = Depends(get_db)):
    return db.query(models.Cliente).all()

@app.put("/clientes/{cliente_id}", response_model=schemas.ClienteResponse)
def atualizar_cliente(cliente_id: int, cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    db_cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()

    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    db_cliente.nome = cliente.nome
    db_cliente.email = cliente.email

    db.commit()
    db.refresh(db_cliente)

    return db_cliente

@app.delete("/clientes/{cliente_id}")
def deletar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    db_cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()

    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    db.delete(db_cliente)
    db.commit()

    return {"msg": "Cliente deletado"}