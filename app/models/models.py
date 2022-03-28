from app.config.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


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