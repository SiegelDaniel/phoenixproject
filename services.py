from sqlalchemy.orm import Session

from domain_models import DepartmentDomain, EmployeeDomain, ProjectDomain
from repositories import ProjectRepository, EmployeeRepository, DepartmentRepository


class ProjectService:
    def __init__(self, project_repo: ProjectRepository):
        self.project_repo = project_repo

    def create_project(self, project: ProjectDomain):
        return self.project_repo.create_project(project)

    def get_project(self, project_id: int):
        return self.project_repo.get_project(project_id)

    def update_project(self, project: ProjectDomain):
        return self.project_repo.update_project(project)

    def delete_project(self, project_id: int):
        return self.project_repo.delete_project(project_id)


class EmployeeService:
    def __init__(self, employee_repository: EmployeeRepository):
        self.employee_repo = employee_repository

    def create_employee(self, department: DepartmentDomain):
        return self.employee_repo.create_employee(department)

    def get_employee(self, department_id: int):
        return self.employee_repo.get_employee(department_id)

    def update_employee(self, employee: EmployeeDomain):
        return self.employee_repo.update_employee(employee)

    def delete_employee(self, employee_id: int):
        return self.employee_repo.delete_employee(employee_id)


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
