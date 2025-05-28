# 📚 API de Livros com Flask

Este projeto é uma API RESTful para gerenciamento de livros, construída com Flask utilizando o padrão arquitetural **MVC**, documentação automática via **Swagger (Flasgger)**, e testes automatizados com **pytest** e **cobertura de código**.

---

## 📁 Estrutura do Projeto

```

meu\_projeto/
├── app/
│   ├── __init__.py          
│   ├── config.py            
│   ├── models/              
│   │   └── book_model.py
│   ├── controllers/         
│   │   └── book_controller.py
│   ├── routes/              
│   │   └── book_routes.py
├── tests/                   
│   ├── conftest.py
│   └── test\_books.py
├── run.py                   
└── requirements.txt         

````

---

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/api-livros-flask.git
cd api-livros-flask
````

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
python run.py
```

Acesse:
[http://localhost:5000/](http://localhost:5000/)

---

## 📘 Documentação com Swagger

Acesse a documentação interativa em:
🔗 **[http://localhost:5000/apidocs/](http://localhost:5000/apidocs/)**

---

## 🧪 Rodando os testes

```bash
pytest
```

### 🔍 Com relatório de cobertura

```bash
pytest --cov=app
```

### 📊 Cobertura HTML

```bash
pytest --cov=app --cov-report=html
```

Abra o arquivo `htmlcov/index.html` para visualizar.

---

## ✅ Funcionalidades

* [x] Criar livros (`POST /books`)
* [x] Listar livros (`GET /books`)
* [x] Obter livro por ID (`GET /books/<id>`)
* [x] Atualizar livro (`PUT /books/<id>`)
* [x] Remover livro (`DELETE /books/<id>`)
* [x] Documentação Swagger com Flasgger
* [x] Testes automatizados com `pytest`
* [x] Banco de dados SQLite

---

## 🛠 Tecnologias utilizadas

* Flask
* SQLAlchemy
* Flasgger (Swagger UI)
* Pytest
* SQLite

---

## 🧠 Padrão de Projeto

O projeto segue o padrão **MVC**:

* **Model**: define os dados da aplicação (ex: `Book`)
* **View (routes)**: define as rotas e expõe a API
* **Controller**: implementa a lógica de negócio

---

## 📄 Licença

Este projeto é open-source e pode ser utilizado livremente para fins acadêmicos e profissionais.

```