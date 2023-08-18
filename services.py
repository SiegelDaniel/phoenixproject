from sqlalchemy.orm import Session

from domain_models import DepartmentDomain
from repositories import ProjectRepository, EmployeeRepository, DepartmentRepository


class ProjectService:
    def __init__(self, project_repo: ProjectRepository):
        self.project_repo = project_repo

    def create_project(self, project):
        return self.project_repo.create_project(project)


class EmployeeService:
    def __init__(self, employee_repository: EmployeeRepository):
        self.employee_repo = employee_repository

    def create_employee(self, employee):
        return self.employee_repo.create_employee(employee)


class DepartmentService:
    def __init__(self, department_repository: DepartmentRepository):
        self.department_repo = department_repository

    def create_department(self, department: DepartmentDomain):
        return self.department_repo.create_department(department)

    def get_department(self, department_id: int):
        return self.department_repo.get_department(department_id)

    def update_department(self, department: DepartmentDomain):
        return self.department_repo.update_department(department)

    def delete_department(self, department_id: int):
        return self.department_repo.delete_department(department_id)
