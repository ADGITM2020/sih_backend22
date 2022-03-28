from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.schema import schema
from app.models import models


def create(request: schema.Equipment, db: Session):
    new_equipment = models.Equipment(
        equipment_name=request.equipment_name,
        description=request.description,
    )

    db.add(new_equipment)
    db.commit()
    db.refresh(new_equipment)
    return new_equipment


def show(id: int, db: Session):
    equipment = db.query(models.Equipment).filter(
        models.Equipment.equipment_id == id).first()
    if not equipment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Equipment with the id {id} is not found")
    return equipment
