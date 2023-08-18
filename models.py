from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ProjectModel(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    client = Column(String)


class EmployeeModel(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)


class DepartmentModel(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
