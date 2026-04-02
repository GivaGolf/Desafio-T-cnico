# 🚀 API de Clientes

## 📌 Descrição
API desenvolvida com FastAPI para gerenciamento de clientes, com autenticação JWT e testes automatizados.

O sistema permite:
- Cadastro e login de usuários
- Gerenciamento completo de clientes (CRUD)
- Proteção de rotas com autenticação
- Testes automatizados com Pytest

---

## 🛠️ Tecnologias utilizadas

- Python 3.11
- FastAPI
- SQLite
- Pytest
- JWT (JSON Web Token)

---

## ⚙️ Como rodar o projeto

### 1. Criar ambiente virtual
python -m venv venv

### 2. Ativar ambiente
venv\Scripts\activate

### 3. Instalar dependências
pip install -r requirements.txt

### 4. Rodar a aplicação
uvicorn main:app --reload

A API estará disponível em:
http://127.0.0.1:8000

Documentação automática:
http://127.0.0.1:8000/docs

---

## 🔐 Autenticação

POST /auth/register  
POST /auth/login  

---

## 👥 Endpoints de Clientes

POST /clientes  
GET /clientes  
GET /clientes/{id}  
PUT /clientes/{id}  
DELETE /clientes/{id}  

---

## 🧪 Testes

Rodar testes:
pytest -v

---

## 📂 Estrutura do projeto

meu_projeto/
│
├── main.py
├── database/
├── api-clientes/
├── tests/
│   ├── test_auth.py
│   └── test_clientes.py
└── README.md

---

## 👨‍💻 Autor

Desenvolvido por Givanildo Oliveira 🚀