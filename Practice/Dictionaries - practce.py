students_grades = {}


def add_student_grades(student_name, subject, grade):
    if student_name not in students_grades:
        students_grades[student_name] = {}
        students_grades[student_name][subject] = grade
    print(f"Added/Updated {student_name}'s grade for {subject}: {grade}")


def update_student_grades(student_name, subject, grade):
    if student_name in students_grades and subject in students_grades[subject]:
        students_grades[student_name][subject] = grade
        print(f"Updated {student_name}'s grade for {subject} to {grade}")


def remove_student(student_name):
    if student_name in students_grades:
        del students_grades[student_name]
        print(f'Removed student: {student_name}')
    else:
        print(f'Student not found.')


name = input('Enter student name: ').strip().capitalize()
sub = input('Enter subject: ').strip().capitalize()
grades = int(input('Enter grade: ').strip())

def main():
    while True:
        print('\n\nEnter grades for students here.')
        print('1. View students')
        print('2. Add new student grades')
        print('3. ')
