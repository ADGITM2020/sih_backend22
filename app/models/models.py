from app.config.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Student(Base):
    __tablename__ = 'student'

    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    # institute_id = Column(Integer, ForeignKey("institute.institute_id"))
    password = Column(String)
    year = Column(String)
    course = Column(String)
    college_id = Column(String)
    is_student = Column(Boolean)

    # slots = relationship("Slot", back_populates="student")
    # institute = relationship("Institute", back_populates="students")
