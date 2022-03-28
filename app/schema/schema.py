
from pydantic import BaseModel


class StudentRegister(BaseModel):

    name: str
    email: str
    password: str
    year: str
    course: str
    college_id: str
    is_student: str


class ShowStudent(BaseModel):

    id: int
    name: str
    email: str
    password: str
    year: str
    course: str
    college_id: str
    is_student: str

    class Config():
        orm_mode = True
