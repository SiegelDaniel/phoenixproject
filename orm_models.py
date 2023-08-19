from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class ProjectModel(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    client = Column(String)

    # Define a foreign key to the department that this project belongs to
    department_id = Column(Integer, ForeignKey('departments.id'))

    # Establish a one-to-many relationship between DepartmentModel and ProjectModel
    department = relationship("DepartmentModel", back_populates="projects")


class EmployeeModel(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)

    # Define a foreign key to the department that this employee belongs to
    department_id = Column(Integer, ForeignKey('departments.id'))

    # Establish a many-to-one relationship between DepartmentModel and EmployeeModel
    department = relationship("DepartmentModel", back_populates="employees")


class DepartmentModel(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    # Establish a one-to-many relationship between DepartmentModel and ProjectModel
    projects = relationship("ProjectModel", back_populates="department")

    # Establish a one-to-many relationship between DepartmentModel and EmployeeModel
    employees = relationship("EmployeeModel", back_populates="department")
