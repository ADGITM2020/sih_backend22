from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.config import database
from app.schema import schema
from app.repository import equipment_repo

router = APIRouter(
    prefix="/equipment",
    tags=['Equipment']
)

get_db = database.get_db


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_equiment(request: schema.Equipment, db: Session = Depends(get_db)):
    return equipment_repo.create(request, db)


@router.get("/{id}", status_code=status.HTTP_200_OK)
def show_equipment(id, db: Session = Depends(get_db)):
    return equipment_repo.show(id, db)
