

# MyStore-fastapi

A lightweight **FastAPI** backend with **SQLAlchemy** database support for managing store products.

## 🔥 Tech Used

* **FastAPI** (REST API framework)
* **SQLAlchemy** (ORM & DB handling)
* **SQLite** by default (can be changed to MySQL/PostgreSQL)
* Optional frontend → **React** or any JS UI

## 📦 Features

* Product CRUD (**Create, Read, Update, Delete**)
* Auto-seed of sample product data on first run
* CORS enabled for `http://localhost:3000`

## 🚀 Run the Project

```bash
git clone https://github.com/harshitha020703/MyStore-fastapi-.git
cd MyStore-fastapi-
pip install -r requirements.txt
uvicorn main:app --reload
```

Visit API Docs:
➡️ `http://127.0.0.1:8000/docs`

## 📡 API Endpoints

| Method | Route            | Description       |
| ------ | ---------------- | ----------------- |
| GET    | `/products/`     | Get all products  |
| GET    | `/products/{id}` | Get product by ID |
| POST   | `/products/`     | Add product       |
| PUT    | `/products/{id}` | Update product    |
| DELETE | `/products/{id}` | Delete product    |

## 🎨 Frontend Connection

If using **React**, just call the API using `fetch()` or `axios` from:

```
http://127.0.0.1:8000/products/
```


