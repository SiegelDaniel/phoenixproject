from pandas import DataFrame
from sqlalchemy.orm import Session, subqueryload

from domain_models import DepartmentDomain, EmployeeDomain, ProjectDomain
from orm_models import ProjectModel, EmployeeModel, DepartmentModel


class ProjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_project(self, project_id: int) -> ProjectDomain:
        project_model = self.db.get(ProjectModel, project_id)
        return ProjectDomain(
            name=project_model.name,
            client=project_model.client,
            id=project_model.id,
            department_id=project_model.department_id
        )

    def get_all_projects(self) -> list[ProjectDomain]:
        projects = self.db.query(ProjectModel).all()
        return [ProjectDomain(id=project.id,
                              name=project.name,
                              client=project.client,
                              department_it=project.department_id) for project in projects]

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
                id=int(row[1]["id"]),
                name=str(row[1]["name"]),
                client=str(row[1]["client"]),
                department_id=int(row[1][3])
            ))
        for project in projects:
            self.db.merge(project)
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
        employee_model.firstname = employee_update.firstname
        employee_model.lastname = employee_update.lastname
        employee_model.age = employee_update.age
        employee_model.email = employee_update.email

        self.db.commit()
        self.db.refresh(employee_model)
        return employee_update

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
        with self.db.begin():
            departments = self.db.query(DepartmentModel).all()
            return [DepartmentDomain(id=department.id,
                                     name=department.name) for department in departments]

    def create_department(self, department_create: DepartmentDomain):
        with self.db.begin():
            department_model = DepartmentModel(
                name=department_create.name
            )
            self.db.add(department_model)
            self.db.commit()
            self.db.refresh(department_model)
            return department_model

    def update_department(self, department_id: int, department_update: DepartmentDomain):
        with self.db.begin():
            department_model = self.db.get(DepartmentModel, department_id)
            department_model.name = department_update.name
            self.db.commit()
            self.db.refresh(department_model)
            return department_update

    def delete_department(self, department_id: int):
        with self.db.begin():
            db_department = self.db.query(DepartmentModel).filter(DepartmentModel.id == department_id).first()
            if db_department:
                self.db.delete(db_department)
                self.db.commit()
                return db_department

    def get_department_by_name(self, department_name: str) -> DepartmentDomain:
        with self.db.begin():
            department_model = self.db.query(DepartmentModel).filter(DepartmentModel.name == department_name).first()
            if department_model:
                return DepartmentDomain(**department_model.__dict__)
            return None

    def insert_departments_from_dataframe(self, df: DataFrame):
        with self.db.begin():
            departments = []
            for row in df.iterrows():
                departments.append(DepartmentModel(id=int(row[0]), name=str(row[1][1])))
            self.db.add_all(departments)
            self.db.commit()

    def get_average_employee_age_per_department(self):
        with self.db.begin():
            departments = self.db.query(DepartmentModel).options(subqueryload(DepartmentModel.employees))
            average_age_per_department = {}
            for department in departments:
                total_age = sum(employee.age for employee in department.employees)
                employee_count = len(department.employees)
                average_age = total_age / employee_count if employee_count > 0 else 0
                average_age_per_department[department.id] = average_age

            return average_age_per_department

    def get_number_of_projects_per_department(self):
        with self.db.begin():
            departments = self.db.query(DepartmentModel).options(
                subqueryload(DepartmentModel.projects)
            ).all()

            number_of_projects_per_department = {}
            for department in departments:
                number_of_projects = len(department.projects)
                number_of_projects_per_department[department.id] = number_of_projects

            return number_of_projects_per_department

    def get_employees_per_department(self):
        with self.db.begin():
            departments = self.db.query(DepartmentModel).options(
                subqueryload(DepartmentModel.employees)
            ).all()

            employees_per_department = {}
            for department in departments:
                employees_per_department[department.id] = [
                    EmployeeDomain(
                        id=employee.id,
                        firstname=employee.firstname,
                        lastname=employee.lastname,
                        email=employee.email,
                        age=employee.age
                    )
                    for employee in department.employees
                ]

            return employees_per_department
