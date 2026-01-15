# 🎬 Flix API

API REST desenvolvida com **Django + Django REST Framework** para gerenciamento de filmes, gêneros, avaliações (reviews) e autenticação de usuários.

Este projeto foi criado com fins de estudo e prática de desenvolvimento backend, seguindo boas práticas de versionamento, organização de apps e segurança básica para publicação no GitHub.

---

## 🚀 Funcionalidades

* 📽️ Cadastro e listagem de filmes
* 🗂️ Organização por gêneros
* ⭐ Sistema de avaliações (reviews)
* 👤 Autenticação de usuários
* 🔐 Preparada para uso com variáveis de ambiente

---

## 🛠️ Tecnologias utilizadas

* Python 3
* Django
* Django REST Framework
* SQLite (ambiente de desenvolvimento)
* Git & GitHub

---

## 📂 Estrutura do projeto

```
flix-api/
├── actors/
├── app/
├── authentication/
├── genres/
├── movies/
├── reviews/
├── manage.py
├── .gitignore
├── .env.example
└── README.md
```

---

## ⚙️ Como rodar o projeto localmente

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/flix-api.git
cd flix-api
```

### 2️⃣ Criar e ativar o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Criar arquivo `.env`

Crie um arquivo `.env` baseado no `.env.example`:

```env
SECRET_KEY=sua_secret_key
DEBUG=True
```

---

### 5️⃣ Rodar migrações

```bash
python manage.py migrate
```

### 6️⃣ Criar superusuário (opcional)

```bash
python manage.py createsuperuser
```

### 7️⃣ Iniciar o servidor

```bash
python manage.py runserver
```

A API estará disponível em:

```
http://127.0.0.1:8000/
```

---

## 🔐 Segurança

* Arquivos sensíveis (`.env`, `db.sqlite3`) não são versionados
* Uso de variáveis de ambiente para configurações críticas
* Projeto preparado para deploy futuro

---

## 📌 Observações

* Banco de dados SQLite é utilizado apenas para desenvolvimento
* Ideal para evoluir para PostgreSQL em produção

---

## 📄 Licença

Este projeto é apenas para fins educacionais.

---

## 👩‍💻 Autora

**Luciana Furtado**
Desenvolvedora Backend | Python | Django

---

Se você gostou do projeto, ⭐ no repositório!
