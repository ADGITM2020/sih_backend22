
from pydantic import BaseModel


class StudentRegister(BaseModel):

    name: str
    email: str
    password: str
    year: int
    course: str
    is_student: bool


class ShowStudent(BaseModel):

    id: int
    name: str
    email: str
    year: int
    course: str
    is_student: bool

    class Config():
        orm_mode = True
