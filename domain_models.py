from typing import Optional

from pydantic import BaseModel, Field


class DomainModel(BaseModel):
    class Config:
        orm_mode = True


class ProjectDomain(DomainModel):
    name: str
    client: str
    id: Optional[int] = Field(default=None)


class EmployeeDomain(DomainModel):
    email: str
    firstname: str
    lastname: str
    age: int
    id: Optional[int] = Field(default=None)


class DepartmentDomain(DomainModel):
    name: str
    id: Optional[int] = Field(default=None)

class DepartmentStatisticsDomain(DomainModel):
    department_id: int
    department_name: str
    number_of_employees: int
    average_age: int
    number_of_projects: int

