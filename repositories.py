from pandas import DataFrame
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

    def get_all_projects(self) -> list[ProjectDomain]:
        projects = self.db.query(ProjectModel).all()
        return [ProjectDomain(id=project.id,
                              name=project.name,
                              client=project.client) for project in projects]

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

    def create_projects_from_dataframe(self, df: DataFrame):
        projects = []
        for row in df.iterrows():
            projects.append(ProjectModel(
                id=int(row[0]),
                name=str(row[1]),
                client=str(row[2]),
                department=int(row[3])
            ))
        self.db.add_all(projects)
        self.db.commit()


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

    def get_all_employees(self) -> list[EmployeeDomain]:
        employees = self.db.query(EmployeeModel).all()
        return [EmployeeDomain(id=employee.id,
                               email=employee.email,
                               firstname=employee.firstname,
                               lastname=employee.lastname,
                               age=employee.age) for employee in employees]

    def create_employee(self, employee_create: EmployeeDomain):
        employee_model = EmployeeModel(
            firstname=employee_create.firstname,
            lastname=employee_create.lastname,
            email=employee_create.email,
            age=employee_create.age
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

    def create_employees_from_dataframe(self, df: DataFrame):
        employees = []
        for row in df.iterrows():
            employees.append(EmployeeModel(
                email=str(row[1]["email"]),
                lastname=str(row[1]["lastname"]),
                firstname=str(row[1]["firstname"]),
                age=int(row[1]["age"]),
                department_id=int(row[1][4])
            ))
        self.db.add_all(employees)
        self.db.commit()


class DepartmentRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_department(self, department_id: int) -> DepartmentDomain:
        department_model = self.db.get(DepartmentModel, department_id)
        return DepartmentDomain(
            name=department_model.name,
            id=department_model.id
        )

    def get_all_departments(self) -> list[DepartmentDomain]:
        departments = self.db.query(DepartmentModel).all()
        return [DepartmentDomain(id=department.id,
                                 name=department.name) for department in departments]

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

    def get_department_by_name(self, department_name: str) -> DepartmentDomain:
        department_model = self.db.query(DepartmentModel).filter(DepartmentModel.name == department_name).first()
        if department_model:
            return DepartmentDomain(**department_model.__dict__)
        return None

    def insert_departments_from_dataframe(self, df: DataFrame):
        departments = []
        for row in df.iterrows():
            departments.append(DepartmentModel(id=int(row[0]), name=str(row[1][1])))
        self.db.add_all(departments)
        self.db.commit()
