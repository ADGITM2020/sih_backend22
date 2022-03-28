from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.models import models
from app.functions import token
from app.config import database
from app.functions.hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter(tags=['Authentication'])


@router.post('/login_student')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    student: models.Student = db.query(models.Student).filter(
        models.Student.student_email == request.username).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(student.student_password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")

    access_token = token.create_access_token(
        data={"sub": student.student_email})
    return {"access_token": access_token, "token_type": "bearer", "student_id": student.student_id}