# 🚀 Sistema de Gestão de Clientes

Aplicação fullstack desenvolvida para gerenciamento de clientes, com autenticação de usuários, operações CRUD e testes automatizados.

---

## 📌 Tecnologias utilizadas

### 🔧 Backend

* Python
* FastAPI
* SQLite
* Pytest

### 🎨 Frontend

* React
* Vite
* CSS

### 🧪 Testes

* Cypress (E2E)
* Pytest (Backend)

---

## ⚙️ Funcionalidades

* 🔐 Autenticação de usuários (login)
* 👤 Cadastro de clientes
* 📋 Listagem de clientes
* ✏️ Edição de clientes
* ❌ Remoção de clientes
* 🧪 Testes automatizados (backend e E2E)

---

## ▶️ Como rodar o projeto

### 🔹 Backend

```bash
cd meu_projeto
uvicorn main:app --reload
```

Backend disponível em:

```
http://localhost:8000
```

---

### 🔹 Frontend

```bash
cd front
npm install
npm run dev
```

Frontend disponível em:

```
http://localhost:5173
```

---

### 🔹 Testes Backend

```bash
pytest
```

---

### 🔹 Testes E2E (Cypress)

```bash
cd front
npx cypress open
```

---

## 🧪 Exemplo de teste E2E

O Cypress valida se a aplicação carrega corretamente:

```js
describe('Aplicação', () => {
  it('Carrega página', () => {
    cy.visit('http://localhost:5173/')
    cy.get('body').should('be.visible')
  })
})
```

---

## 📁 Estrutura do projeto

```
meu_projeto/
│
├── api_clientes/
├── database/
├── tests/
├── front/
│   ├── src/
│   ├── cypress/
│
├── main.py
└── README.md
```

---

## 🎯 Objetivo do projeto

Desenvolver uma aplicação completa com foco em qualidade de código e testes automatizados, especialmente testes E2E com Cypress.

---

## 👨‍💻 Autor

Givanildo Oliveira

---
