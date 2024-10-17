class Students:
    def __init__(self, student_name, age, grade):
        self.__student_name = student_name
        self.__age = age
        self.__grade = grade

    def set_student_name(self, set_name):
        self.__student_name = set_name

    def get_student_name(self):
        return self.__student_name

    def set_age(self, age_set):
        if age_set >= 0:
            self.__age = age_set

    def get_age(self):
        return self.__age

    def set_grade(self, grade_set):
        self.__grade = grade_set

    def get_grade(self):
        return self.__grade


st = Students("Rudy", 14, 8)
st.set_student_name(input('Enter name: ').strip().capitalize())
st.set_age(int(input('Enter age: ').strip()))
st.set_grade(int(input('Enter grade: ').strip()))
print(f'Hi! My name is {st.get_student_name()}. I am {st.get_age()} years old, and in grade {st.get_grade()}.')
