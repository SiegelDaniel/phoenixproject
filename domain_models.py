from typing import Optional

from pydantic import BaseModel, Field


class DomainModel(BaseModel):
    class Config:
        orm_mode = True


class ProjectDomain(DomainModel):
    name: str
    client: str
    id: Optional[int] = Field(default=None)
    department_id:Optional[int] = Field(default=None)


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
    department_id: Optional[int] = Field(default=None)
    department_name: str
    employees: list[EmployeeDomain]
    average_age: float
    number_of_projects: int

