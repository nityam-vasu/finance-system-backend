# Finance Tracker API (FastAPI)

##  Overview
This is a backend system for managing personal finances.  
It allows users to track income and expenses, filter data, and view summaries.

---

##  Features
- Add transactions (income/expense)
- View all transactions
- Update transactions
- Delete transactions
- Filter by type & category
- View financial summary (income, expense, balance)
- Role-based endpoint (/admin-only)

---

##  Tech Stack
- Python
- FastAPI
- SQLite
- SQLAlchemy

---

## How to Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload