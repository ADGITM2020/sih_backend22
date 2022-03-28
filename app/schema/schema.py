
from pydantic import BaseModel
from typing import List,Optional

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

class Equipment(BaseModel):
    equipment_name: str
    description: str
    experiments: Optional[List[int]] = []

    class Config:
        orm_mode = True


class Experiment(BaseModel):
    aim: str
    description: str
    equipments: Optional[List[int]] = []

    class Config:
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


class ShowEquipment(BaseModel):
    equipment_id:int
    equipment_name:str
    description:str
    experiments:List[Experiment]=[]   

    class Config:
        orm_mode = True


class ShowExperiment(BaseModel):
    experiment_id:int
    aim:str
    description:str   
    equipments:List[Equipment]=[]

    class Config:
        orm_mode = True
