# Expense Tracker

A simple Expense Tracker application built with **FastAPI** for the backend and **HTML, CSS, and JavaScript** for the frontend.

This project demonstrates how a frontend communicates with a backend using REST APIs.

---

# Features

- Add an expense
- View all expenses
- Delete an expense
- FastAPI REST API
- In-memory data storage (data resets when the server restarts)

---

# Tech Stack

## Frontend
- HTML
- CSS
- JavaScript

## Backend
- FastAPI
- Pydantic

---

# Project Structure

```
expense-tracker/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── ...
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   ├── style.css
│   └── ...
│
└── README.md
```

---

# Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/Swarnima-Khadka1/software_fellowship_day3.git
```

Navigate to the project folder.

```bash
cd expense-tracker
```

---

## 2. Navigate to the Backend

```bash
cd backend
```

---

## 3. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

### macOS / Linux

```bash
python3 -m venv venv
```

---

## 4. Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

After activation, your terminal should display something similar to:

```text
(venv)
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note:** `requirements.txt` includes `fastapi[standard]`, so you do not need to install Uvicorn separately.

---

## 6. Run the Backend

Start the FastAPI development server with:

```bash
fastapi dev main.py
```

The backend will start at:

```
http://127.0.0.1:8000
```

Interactive API documentation is available at:

```
http://127.0.0.1:8000/docs
```

---

# Running the Frontend

Open the `frontend` folder in VS Code.

Right-click on `index.html` and select:

```
Open with Live Server
```

The frontend will communicate with the FastAPI backend running on port **8000**.

---

# API Endpoints

## Get All Expenses

```http
GET /expenses
```

Returns all stored expenses.

---

## Add an Expense

```http
POST /expenses
```

Example Request Body

```json
{
  "category": "Food",
  "description": "Pizza",
  "amount": 20
}
```

---

## Delete an Expense

```http
DELETE /expenses/{expense_id}
```

Deletes an expense using its unique ID.

---

# Validation

The backend validates incoming data using **Pydantic**.

Validation rules:

- `category` is required.
- `description` is optional.
- `amount` must be greater than **0**.

---

# Notes

- Data is stored **in memory**.
- Restarting the backend will clear all saved expenses.
- This project does **not** use a database and is intended for learning purposes.

---

# Learning Objectives

This project demonstrates:

- FastAPI
- REST APIs
- HTTP Methods (GET, POST, DELETE)
- Pydantic Validation
- JSON Requests & Responses
- Fetch API
- Frontend ↔ Backend Communication
