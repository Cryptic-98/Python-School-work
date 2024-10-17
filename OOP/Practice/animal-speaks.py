class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f'Name: {self.name}')


class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def show_employee_id(self):
        print(f'Employee: {self.employee_id}')


class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

    def show_department(self):
        print(f'Department: {self.department}')


obj = Manager('Chris', '508040', 'Human Resources')
obj.show_name()
obj.show_employee_id()
obj.show_department()

