from typing import List, Optional


class Person:
    def __init__(self, first_name: str, last_name: str, birthdate: str, gender: str):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.gender = gender

    def __str__(self) -> str:
        return f"Firstname: {self.first_name}, Lastname: {self.last_name}, Birthdate: {self.birthdate}, Gender: {self.gender}"


class Employee(Person):
    pass


class DepartmentHead(Employee):
    pass


class Department:
    def __init__(self, name: str):
        self.name = name
        self.employees: List[Employee] = []

    def __str__(self) -> str:
        return self.name

    def add_employee(self, employee: Employee) -> None:
        if isinstance(employee, DepartmentHead) and any(isinstance(e, DepartmentHead) for e in self.employees):
            print(f"Department {self.name} already has a Department Head.")
            return
        self.employees.append(employee)

    def count_employees(self) -> int:
        return len(self.employees)

    def count_department_heads(self) -> int:
        return sum(isinstance(e, DepartmentHead) for e in self.employees)


class Company:
    def __init__(self, name: str):
        self.name = name
        self.departments: List[Department] = []

    def __str__(self) -> str:
        return self.name

    def add_department(self, department: Department) -> None:
        self.departments.append(department)

    def count_departments(self) -> int:
        return len(self.departments)

    def count_employees(self) -> int:
        return sum(department.count_employees() for department in self.departments)

    def count_department_heads(self) -> int:
        return sum(department.count_department_heads() for department in self.departments)

    def get_biggest_department(self) -> Optional[str]:
        if not self.departments:
            return None
        return max(self.departments, key=lambda d: d.count_employees()).name

    def get_male_female_ratio(self) -> str:
        total_employees = self.count_employees()
        if total_employees == 0:
            return "No employees to calculate ratio."
        males = sum(e.gender.lower() == "male" for d in self.departments for e in d.employees)
        male_ratio = round((males / total_employees) * 100, 2)
        female_ratio = round(100 - male_ratio, 2)
        return f"In {self.name}: {male_ratio}% of the employees are male and {female_ratio}% are female."


if __name__ == "__main__":
    company = Company("Geldmacher_AG")
    dep1 = Department("Production")
    dep2 = Department("Marketing")
    dep3 = Department("Sales")

    emp1 = Employee("Jonathan", "Gendu", "01.06.2004", "male")
    emp2 = Employee("Lara", "Marthe", "14.04.2005", "female")
    emp3 = Employee("David", "Cech", "21.10.2004", "male")
    emp4 = Employee("Felix", "Haider", "29.11.2004", "male")
    emp5 = Employee("Daniel", "Egger", "06.07.2005", "male")
    emp6 = Employee("Daniel", "Kopp", "29.11.2004", "male")
    dph = DepartmentHead("Richard", "McRich", "10.06.1980", "male")
    dph2 = DepartmentHead("Moni", "Haver", "01.01.1991", "female")
    dph3 = DepartmentHead("David", "Mark", "01.01.2003", "male")

    company.add_department(dep1)
    company.add_department(dep2)
    company.add_department(dep3)

    dep1.add_employee(emp1)
    dep1.add_employee(dph)
    dep1.add_employee(dph2)
    dep1.add_employee(emp2)
    dep2.add_employee(emp3)
    dep2.add_employee(emp4)
    dep3.add_employee(emp5)
    dep3.add_employee(emp6)
    dep2.add_employee(dph3)

    print(f"Number of employees in department {dep1} is: {dep1.count_employees()}")
    print(f"Number of employees in department {dep2} is: {dep2.count_employees()}")
    print(f"Number of employees in department {dep3} is: {dep3.count_employees()}")
    print(f"Number of Department heads in department {dep1} is: {dep1.count_department_heads()}")
    print(f"Number of Department heads in department {dep2} is: {dep2.count_department_heads()}")
    print(f"Number of Department heads in department {dep3} is: {dep3.count_department_heads()}")
    print(f"Number of Department heads in company {company} is: {company.count_department_heads()}")
    print(f"Number of the employees in company {company} is: {company.count_employees()}")
    print(f"Department with the highest Number of employees is: {company.get_biggest_department()}")
    print(company.get_male_female_ratio())
