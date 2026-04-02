from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database.auth import create_access_token, verify_token
from database.database import engine, SessionLocal, Base
from database import models, schemas

app = FastAPI()

# ✅ CORS CORRETO (SEM CONFLITO)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# cria tabelas
Base.metadata.create_all(bind=engine)

# =========================
# AUTH
# =========================

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Token inválido")
    return payload

@app.get("/protegido")
def rota_protegida(user=Depends(get_current_user)):
    return {
        "statusCode": 200,
        "message": "Acesso autorizado",
        "data": {"user": user}
    }

# =========================
# BANCO
# =========================

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# =========================
# CLIENTES (PROTEGIDO)
# =========================

@app.post("/clientes")
def criar_cliente(
    cliente: schemas.ClienteCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    novo_cliente = models.Cliente(
        nome=cliente.nome,
        email=cliente.email,
        telefone=cliente.telefone
    )
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)

    return {
        "statusCode": 200,
        "message": "Cliente criado",
        "data": novo_cliente
    }


@app.get("/clientes")
def listar_clientes(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    clientes = db.query(models.Cliente).all()

    return {
        "statusCode": 200,
        "message": "Clientes listados",
        "data": clientes
    }


@app.get("/clientes/{cliente_id}")
def buscar_cliente(
    cliente_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    return {
        "statusCode": 200,
        "message": "Cliente encontrado",
        "data": cliente
    }


@app.put("/clientes/{cliente_id}")
def atualizar_cliente(
    cliente_id: int,
    cliente: schemas.ClienteCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    db_cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()

    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    db_cliente.nome = cliente.nome
    db_cliente.email = cliente.email
    db_cliente.telefone = cliente.telefone

    db.commit()
    db.refresh(db_cliente)

    return {
        "statusCode": 200,
        "message": "Cliente atualizado",
        "data": db_cliente
    }


@app.delete("/clientes/{cliente_id}")
def deletar_cliente(
    cliente_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    db_cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()

    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    db.delete(db_cliente)
    db.commit()

    return {
        "statusCode": 200,
        "message": "Cliente deletado",
        "data": None
    }

# =========================
# AUTH
# =========================

@app.post("/auth/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()

    if db_user:
        raise HTTPException(status_code=400, detail="Usuário já existe")

    novo_user = models.User(
        email=user.email,
        password=user.password
    )

    db.add(novo_user)
    db.commit()
    db.refresh(novo_user)

    return {
        "statusCode": 200,
        "message": "Usuário criado",
        "data": {"email": novo_user.email}
    }


@app.post("/auth/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()

    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = create_access_token({"sub": db_user.email})

    return {
        "statusCode": 200,
        "message": "Login realizado",
        "data": {"access_token": token}
    }