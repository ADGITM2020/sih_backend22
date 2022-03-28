from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.schema import schema
from app.functions.hashing import Hash
from app.models import models


def create(request: schema.Institute, db: Session):

    hashed_password = Hash.bcrypt(request.institute_password)

    new_institute = models.Institute(
        institute_name=request.institute_name,
        institute_email=request.institute_email,
        institute_password=hashed_password,
        institute_address=request.institute_address,
        is_institute_parent=request.is_institute_parent,
        is_institute_resource=request.is_institute_resource
    )
    db.add(new_institute)
    db.commit()
    db.refresh(new_institute)
    return new_institute


def show(id: int, db: Session):
    institute = db.query(models.Institute).filter(
        models.Institute.institute_id == id).first()
    if not institute:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"institute with the id {id} is not found")
    return institute


def get_all_labs(id: int, db: Session):
    all_labs = db.query(models.Lab).where(models.Lab.institute_id == id).all()
    return all_labs


def get_all_students(id: int, db: Session):
    all_students = db.query(models.Student).where(models.Student.id == id).all()
    return all_students
