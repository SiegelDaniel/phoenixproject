from sqlalchemy.orm import Session

from domain_models import DepartmentDomain
from models import ProjectModel, EmployeeModel, DepartmentModel


class ProjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_project(self, project):
        db_project = ProjectModel(**project.dict())
        self.db.add(db_project)
        self.db.commit()
        self.db.refresh(db_project)
        return db_project


class EmployeeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_employee(self, employee):
        db_employee = EmployeeModel(**employee.dict())
        self.db.add(db_employee)
        self.db.commit()
        self.db.refresh(db_employee)
        return db_employee


class DepartmentRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_department(self, department_id: int) -> DepartmentDomain:
        department_model = self.db.get(DepartmentModel, department_id)
        return DepartmentDomain(
            name=department_model.name,
            id=department_model.id
        )

    def create_department(self, department_create: DepartmentDomain):
        department_model = DepartmentModel(
            name=department_create.name
        )
        self.db.add(department_model)
        self.db.commit()
        self.db.refresh(department_model)
        return department_model

    def update_department(self, department_update: DepartmentDomain):
        department_model = self.db.get(DepartmentModel, department_update.id)
        department_model.name = department_update.name
        self.db.commit()
        self.db.refresh(department_model)

    def delete_department(self, department_id: int):
        db_department = self.db.query(DepartmentModel).filter(DepartmentModel.id == department_id).first()
        if db_department:
            self.db.delete(db_department)
            self.db.commit()
            return db_department
