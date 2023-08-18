from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from domain_models import DepartmentDomain
from models import Base, EmployeeModel, ProjectModel, DepartmentModel
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
    updated_department = department_service.update_department(department_id, department)
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