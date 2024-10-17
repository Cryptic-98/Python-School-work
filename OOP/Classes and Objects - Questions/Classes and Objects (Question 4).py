class Employee:
    def __init__(self, employee_id, name, salary):
        self.__employee_id = employee_id
        self.__name = name
        self.__salary = salary

    def set_employee_id(self, em):
        self.__employee_id = em

    def get_employee_id(self):
        return self.__employee_id

    def set_name(self, n):
        self.__name = n

    def get_name(self):
        return self.__name

    def set_salary(self, s):
        if s > 15000:
            self.__salary = s

    def get_salary(self):
        return self.__salary


emp = Employee('9608075413086', 'Susan', '15000')
emp.set_employee_id(int(input('Enter ID: ').strip()))
emp.set_name(str(input('Enter name: ').strip().capitalize()))
emp.set_salary((int(input('Enter salary: ').strip())))
print(f'ID: {emp.get_employee_id()}')
print(f'Name: {emp.get_name()}')
print(f'Salary: R{emp.get_salary()}')

