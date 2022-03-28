from typing import List
from app.config.database import Base
from sqlalchemy import Table,Boolean, Column, ForeignKey, Integer, String
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
    # labs = relationship("Lab", back_populates="institute")



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
    aim = Column(String)
    description = Column(String)
    equipments = relationship(
        "Equipment", secondary="experiment_equipments", back_populates="experiments")
    # labs = relationship("Lab", secondary="lab_experiments",
    #                     back_populates="experiments")