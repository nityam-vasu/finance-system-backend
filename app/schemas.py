from pydantic import BaseModel
from datetime import date

class TransactionCreate(BaseModel):
    type: str
    category: str
    amount: float
    date: date
    note: str

class TransactionResponse(TransactionCreate):
    id: int

    class Config:
        orm_mode = True