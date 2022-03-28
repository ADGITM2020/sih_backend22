from typing import List
from app.config.database import Base
from sqlalchemy import Table,Boolean, Column, ForeignKey, Integer, String,Float
from sqlalchemy.orm import relationship

from app.routes import experiment


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    institute_id = Column(Integer, ForeignKey("institute.institute_id"))
    password = Column(String)
    year = Column(Integer)
    course = Column(String)
    is_student = Column(Boolean)

    institute = relationship("Institute", back_populates="students")
    # slots = relationship("Slot", back_populates="student")

class Institute(Base):
    __tablename__ = 'institute'

    institute_id = Column(Integer, primary_key=True, index=True)
    institute_name = Column(String)
    institute_email = Column(String)
    institute_password = Column(String)
    institute_address = Column(String)
    is_institute_parent = Column(Boolean)
    is_institute_resource = Column(Boolean)

    students = relationship("Student", back_populates="institute")
    labs = relationship("Lab", back_populates="institute")



experiment_equipments = Table('experiment_equipments', Base.metadata,
                              Column('experiment_id', ForeignKey(
                                  'experiments.experiment_id')),
                              Column('equipment_id', ForeignKey(
                                  'equipments.equipment_id'))
                              )



class Equipment(Base):
    __tablename__ = 'equipments'

    equipment_id = Column(Integer, primary_key=True, index=True)
    equipment_name = Column(String)
    description = Column(String)
    experiments = relationship(
        "Experiment", secondary="experiment_equipments", back_populates="equipments")


class Experiment(Base):
    __tablename__ = "experiments"

    experiment_id = Column(Integer, primary_key=True, index=True)
    lab_id=Column(Integer,ForeignKey("labs.lab_id"))
    aim = Column(String)
    description = Column(String)
    equipments = relationship(
        "Equipment", secondary="experiment_equipments", back_populates="experiments")
    lab = relationship("Lab",back_populates="experiments")

# lab_experiments = Table('lab_experiments', Base.metadata,
#     Column('experiment_id', ForeignKey('experiments.experiment_id'), primary_key=True),
#     Column('lab_id', ForeignKey('labs.lab_id'), primary_key=True)
# )

class Lab(Base):
    __tablename__="labs"
    
    lab_id=Column(Integer,primary_key=True,index=True)
    lab_name=Column(String)
    lab_address=Column(String)
    longitude=Column(Float)
    latitude=Column(Float) 
    lab_student_capacity=Column(Integer)
    lab_admin_name=Column(String)
    institute_id=Column(Integer,ForeignKey("institute.institute_id"))
    experiments=relationship("Experiment",back_populates="labs")

    institute=relationship("Institute",back_populates="labs")
    # slots=relationship("Slot",back_populates="labs")
    
    
    
#Slot date as well