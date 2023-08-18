from typing import Optional

from pydantic import BaseModel, Field


class DomainModel(BaseModel):
    class Config:
        orm_mode = True


class ProjectDomain(DomainModel):
    name: str
    client: str
    id: int


class EmployeeDomain(DomainModel):
    email: str
    firstname: str
    lastname: str
    age: int
    id: int


class DepartmentDomain(DomainModel):
    name: str
    id: Optional[int] = Field(default=None)
