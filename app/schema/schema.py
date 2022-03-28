
from pydantic import BaseModel


class StudentRegister(BaseModel):

    name: str
    email: str
    password: str
    year: int
    institute_id: int
    course: str
    is_student: bool

    class Config():
        orm_mode = True

class Institute(BaseModel):
    institute_name:str
    institute_email:str
    institute_password:str
    institute_address:str
    is_institute_parent:bool    
    is_institute_resource:bool

    class Config():
        orm_mode = True

class ShowStudent(BaseModel):
    id: int
    name: str
    email: str
    year: int
    course: str
    institute_id:int
    is_student: bool


    class Config():
        orm_mode = True

class ShowInstitute(BaseModel):
    institute_id:int
    institute_name:str
    institute_email:str
    institute_address:str
    is_institute_parent:bool    
    is_institute_resource:bool

    class Config():
        orm_mode = True