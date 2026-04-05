from sqlalchemy.orm import Session
import models

def create_transaction(db: Session, data):
    obj = models.Transaction(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_transactions(db: Session):
    return db.query(models.Transaction).all()

def update_transaction(db: Session, id, data):
    obj = db.query(models.Transaction).filter(models.Transaction.id == id).first()
    if obj:
        obj.type = data.type
        obj.category = data.category
        obj.amount = data.amount
        obj.date = data.date
        obj.note = data.note
        db.commit()
        return obj

def delete_transaction(db: Session, id):
    obj = db.query(models.Transaction).filter(models.Transaction.id == id).first()
    if obj:
        db.delete(obj)
        db.commit()
        return True