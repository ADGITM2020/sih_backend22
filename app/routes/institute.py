from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.config import database
from app.schema import schema
from app.repository import institute_repo
from typing import List

router = APIRouter(
    prefix="/institute",
    tags=['Institute']
)

get_db = database.get_db


@router.post("/", status_code=status.HTTP_201_CREATED,response_model=schema.ShowInstitute)
def create_institute(request: schema.Institute, db: Session = Depends(get_db)):
    return institute_repo.create(request, db)


@router.get("/{id}", status_code=status.HTTP_200_OK,response_model=schema.ShowInstitute)
def show_institute(id, db: Session = Depends(get_db)):
    return institute_repo.show(id, db)


@router.get("/{id}/labs")
def get_all_labs(id: int, db: Session = Depends(get_db)):
    return institute_repo.get_all_labs(id, db)


@router.get("/{id}/students",response_model=List[schema.ShowStudent])
def get_all_students(id: int, db: Session = Depends(get_db)):
    return institute_repo.get_all_students(id, db)
