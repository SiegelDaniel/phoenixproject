from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class ProjectModel(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    client = Column(String)

    department_id = Column(Integer, ForeignKey('departments.id'))

    department = relationship("DepartmentModel", back_populates="projects")


class EmployeeModel(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)

    department_id = Column(Integer, ForeignKey('departments.id'))

    department = relationship("DepartmentModel", back_populates="employees")


class DepartmentModel(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    projects = relationship("ProjectModel", back_populates="department")

    employees = relationship("EmployeeModel", back_populates="department")
