from os import name
from fastapi import APIRouter
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schema import schema
from app.config import database
from app.repository import student_repo
from app.functions.oauth2 import get_current_user

router = APIRouter(
    prefix="/student",
    tags=['Students']
)

get_db = database.get_db


@router.post('/',response_model=schema.ShowStudent)
def create_student(request: schema.StudentRegister, db: Session = Depends(get_db)):
    return student_repo.create(request, db)


@router.get('/{id}', response_model=schema.ShowStudent)
def get_student(id: int, db: Session = Depends(get_db)):
    return student_repo.show(id, db)

