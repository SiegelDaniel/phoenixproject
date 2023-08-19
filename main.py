from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from domain_models import DepartmentDomain, EmployeeDomain, ProjectDomain
from models import Base
from repositories import ProjectRepository, EmployeeRepository, DepartmentRepository
from services import ProjectService, EmployeeService, DepartmentService

app = FastAPI()

DATABASE_URL = "postgresql://postgres:phoenix@127.0.0.1:5432/db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


project_repository = ProjectRepository(get_db().__next__())
employee_repository = EmployeeRepository(get_db().__next__())
department_repository = DepartmentRepository(get_db().__next__())

project_service = ProjectService(project_repository)
employee_service = EmployeeService(employee_repository)
department_service = DepartmentService(department_repository)


@app.get("/departments/{department_id}", response_model=DepartmentDomain)
def read_department(department_id: int, db: Session = Depends(get_db)):
    department = department_service.get_department(department_id)
    if department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return department


@app.put("/departments/{department_id}", response_model=DepartmentDomain)
def update_department(
        department_id: int, department: DepartmentDomain, db: Session = Depends(get_db)
):
    updated_department = department_service.update_department(department)
    if updated_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return updated_department


@app.delete("/departments/{department_id}", response_model=DepartmentDomain)
def delete_department(department_id: int, db: Session = Depends(get_db)):
    deleted_department = department_service.delete_department(department_id)
    if deleted_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return deleted_department


@app.post("/departments/", response_model=DepartmentDomain)
def create_department(department: DepartmentDomain, db: Session = Depends(get_db)):
    return department_service.create_department(department)


# EMPLOYEES#

@app.get("/employees/{employee_id}", response_model=EmployeeDomain)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = employee_service.get_employee(employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@app.put("/employees/{employee_id}", response_model=EmployeeDomain)
def update_employee(
        employee_id: int, employee: EmployeeDomain, db: Session = Depends(get_db)
):
    updated_employee = employee_service.update_employee(employee)
    if updated_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated_employee


@app.delete("/employees/{employee_id}", response_model=EmployeeDomain)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    deleted_employee = employee_service.delete_employee(employee_id)
    if deleted_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return deleted_employee


@app.post("/employees/", response_model=EmployeeDomain)
def create_employee(employee: EmployeeDomain, db: Session = Depends(get_db)):
    return employee_service.create_employee(employee)


# PROJECTS
@app.get("/projects/{project_id}", response_model=ProjectDomain)
def read_project(project_id: int, db: Session = Depends(get_db)):
    project = project_service.get_project(project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@app.put("/projects/{project_id}", response_model=ProjectDomain)
def update_project(
        project_id: int, project: ProjectDomain, db: Session = Depends(get_db)
):
    updated_project = project_service.update_project(project)
    if updated_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return updated_project


@app.delete("/projects/{project_id}", response_model=ProjectDomain)
def delete_project(project_id: int, db: Session = Depends(get_db)):
    deleted_project = project_service.delete_project(project_id)
    if deleted_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return deleted_project


@app.post("/projects/", response_model=ProjectDomain)
def create_project(project: ProjectDomain, db: Session = Depends(get_db)):
    return project_service.create_project(project)
