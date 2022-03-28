from sqlalchemy.orm import Session
from sqlalchemy import update
from fastapi import HTTPException, Response, status

from app.schema import schema
from app.models import models
from app.functions.hashing import Hash


def create(request: schema.StudentRegister, db: Session):
    new_student: models.Student = models.Student(
        name=request.name,
        email=request.name,
        password=Hash.bcrypt(request.password),
        year=request.year,
        course=request.course,
        college_id=request.college_id,
        is_student=request.is_student
    )

    # if request.institute_id:
    #     new_student.institute_id = request.institute_id
    #     institute = db.query(models.Institute).filter(
    #         models.Institute.institute_id == request.institute_id).first()
    #     institute.students.append(new_student)

    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


def show(id: int, db: Session):
    student: models.Student = db.query(models.Student).filter(
        models.Student.id == id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Student with the id {id} is not available")
    return student


def update(id: int, db: Session, requests: schema.ShowStudent):
    student = db.query(models.Student).filter(
        models.Student.id == id)
    if not student.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Student with the id {id} is not available")

    student.update(requests)
    db.commit()
    return Response(status_code=status.HTTP_200_OK)
