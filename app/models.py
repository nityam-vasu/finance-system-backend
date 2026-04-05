from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base
import datetime

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    category = Column(String)
    amount = Column(Float)
    date = Column(Date, default=datetime.date.today)
    note = Column(String)