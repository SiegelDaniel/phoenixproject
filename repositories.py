from sqlalchemy.orm import Session

from domain_models import DepartmentDomain, EmployeeDomain, ProjectDomain
from models import ProjectModel, EmployeeModel, DepartmentModel


class ProjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_project(self, project_id: int) -> ProjectDomain:
        project_model = self.db.get(ProjectModel, project_id)
        return ProjectDomain(
            name=project_model.name,
            client=project_model.client,
            id=project_model.id
        )

    def create_project(self, project_create: ProjectDomain):
        project_model = ProjectModel(
            name=project_create.name,
            client=project_create.client
        )
        self.db.add(project_model)
        self.db.commit()
        self.db.refresh(project_model)
        return project_model

    def update_project(self, project_update: ProjectDomain):
        project_model = self.db.get(ProjectModel, project_update.id)
        project_model.name = project_update.name
        project_model.client = project_update.client
        self.db.commit()
        self.db.refresh(project_model)

    def delete_project(self, project_id: int):
        db_project = self.db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
        if db_project:
            self.db.delete(db_project)
            self.db.commit()
            return db_project


class EmployeeRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_employee(self, employee_id: int) -> EmployeeDomain:
        employee_model = self.db.get(EmployeeModel, employee_id)
        return EmployeeDomain(
            firstname=employee_model.firstname,
            lastname=employee_model.lastname,
            email=employee_model.email,
            age=employee_model.age,
            id=employee_model.id
        )

    def create_employee(self, employee_create: EmployeeDomain):
        employee_model = EmployeeModel(
            name=employee_create.name
        )
        self.db.add(employee_model)
        self.db.commit()
        self.db.refresh(employee_model)
        return employee_model

    def update_employee(self, employee_update: EmployeeDomain):
        employee_model = self.db.get(EmployeeModel, employee_update.id)
        employee_model.name = employee_update.name
        self.db.commit()
        self.db.refresh(employee_model)

    def delete_employee(self, employee_id: int):
        db_employee = self.db.query(EmployeeModel).filter(EmployeeModel.id == employee_id).first()
        if db_employee:
            self.db.delete(db_employee)
            self.db.commit()
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
