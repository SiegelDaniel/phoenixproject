from io import StringIO

from fastapi import UploadFile
import pandas as pd

from domain_models import DepartmentDomain, EmployeeDomain, ProjectDomain
from repositories import ProjectRepository, EmployeeRepository, DepartmentRepository


class ProjectService:
    def __init__(self, project_repo: ProjectRepository):
        self.project_repo = project_repo

    def create_project(self, project: ProjectDomain):
        return self.project_repo.create_project(project)

    def get_project(self, project_id: int):
        return self.project_repo.get_project(project_id)

    def get_all_projects(self):
        return self.project_repo.get_all_projects()

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

    def get_all_employees(self):
        return self.employee_repo.get_all_employees()

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

    def get_all_departments(self):
        return self.department_repo.get_all_departments()

    def update_department(self, department: DepartmentDomain):
        return self.department_repo.update_department(department)

    def delete_department(self, department_id: int):
        return self.department_repo.delete_department(department_id)

    def get_department_by_name(self, department_name: str):
        return self.department_repo.get_department_by_name(department_name)


class FileService:
    def __init__(self, department_repo: DepartmentRepository, employee_repo: EmployeeRepository, project_repo: ProjectRepository):
        self.project_repo = project_repo
        self.department_repo = department_repo
        self.employee_repo = employee_repo

    def process_file(self, file: UploadFile):
        if("employee" in file.filename):
            self._insert_employees_from_csv(file)
        elif("department" in file.filename):
            df = pd.read_csv(StringIO(file.file.read().decode('utf-8')), sep=';')
            self.department_repo.insert_departments_from_dataframe(df)
        elif("project" in file.filename):
            self._insert_projects_from_csv(file)
        return {}

    def _insert_projects_from_csv(self, file):
        df = pd.read_csv(StringIO(file.file.read().decode('utf-8')), sep=';')
        for index, row in df.iterrows():
            department_name = row[3]
            department_id = self.department_repo.get_department_by_name(department_name).id
            df.at[index, 3] = department_id
        self.project_repo.create_projects_from_dataframe(df)

    def _insert_employees_from_csv(self, file):
        df = pd.read_csv(StringIO(file.file.read().decode('utf-8')), sep=';')
        for index, row in df.iterrows():
            department_name = row[4]
            department_id = self.department_repo.get_department_by_name(department_name).id
            df.at[index, 4] = department_id
        self.employee_repo.create_employees_from_dataframe(df)