class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f'Name: {self.name}')


class Employee(Person):
    def __init__(self, name, employeeId):
        super().__init__(name)
        self.employeeId = employeeId

    def employee_id(self):
        print(f'Employee ID: {self.employeeId}')


class Manager(Employee):
    def __init__(self, name, employeeId, department):
        super().__init__(name, employeeId)
        self.department = department

    def show_department(self):
        print(f'Department name: {self.department}')


manager_class = Manager('Jane Doe', 'DF465', 'Human Resources')
manager_class.show_name()
manager_class.employee_id()
manager_class.show_department()
