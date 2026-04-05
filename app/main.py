from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, app.crud as crud
from app.database import SessionLocal, engine
from app.schemas import TransactionCreate

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Finance API Running"}

@app.post("/add")
def add(transaction: TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db, transaction)

@app.get("/all")
def get_all(db: Session = Depends(get_db)):
    return crud.get_transactions(db)

@app.get("/balance")
def balance(db: Session = Depends(get_db)):
    data = crud.get_transactions(db)
    total = 0
    for i in data:
        if i.type == "income":
            total += i.amount
        else:
            total -= i.amount
    return {"balance": total}


# Category filter API
@app.get("/category/{cat}")
def get_by_category(cat: str, db: Session = Depends(get_db)):
    data = crud.get_transactions(db)
    return [i for i in data if i.category == cat]