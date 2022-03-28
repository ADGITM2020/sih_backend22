from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.schema  import schema
from app.models import models

def create(request: schema.Slot, db: Session):
    new_slot = models.Slot(
        lab_id=request.lab_id,
        price=request.price,
        date=request.date,
        start_time=request.start_time,
        end_time=request.end_time
    )
    
    db.add(new_slot)
    lab=db.query(models.Lab).filter(models.Lab.lab_id==request.lab_id).first()
    lab.slots.append(new_slot)
    db.commit()
    db.refresh(new_slot)
    return new_slot


def show(id: int, db: Session):
    slot=db.query(models.Slot).filter(models.Slot.slot_id==id).first()
    if not slot:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Lab with the id {id} is not found")
    return slot  

def show_all_slots(db:Session):
    slots=db.query(models.Slot).all()
    return slots

def delete(id,db:Session):
    slot=db.query(models.Slot).filter(models.Slot.slot_id==id).first()
    db.delete(slot)
    db.commit()