# 💰 Expense Management System

This project is a full-stack Python-based Expense Management System that uses **FastAPI** for the backend and **Streamlit** for the frontend.

---

## 🧾 Project Structure

```
project-expense-tracking/
│
├── backend/               # FastAPI backend server code
│   ├── db_helper.py
│   ├── logging_setup.py
│   └── server.py
│
├── frontend/              # Streamlit frontend code
│   ├── add_update_ui.py
│   ├── analytics_ui.py
│   └── app.py
│
├── tests/                 # Test cases for backend & frontend
├── requirements.txt       # Python package requirements
└── README.md              # Project overview and instructions
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/expense-management-system
cd expense-management-system
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the FastAPI Backend Server

```bash
uvicorn server.server:app --reload
```

### 4. Run the Streamlit Frontend App

```bash
streamlit run frontend/app.py
```

---

## ✅ Features

- Add & update expense records
- View analytics on expense data
- Interactive frontend (Streamlit)
- REST API backend (FastAPI)

---

## 📂 Requirements

All dependencies are listed in `requirements.txt`. Make sure to use Python 3.8+.


---
