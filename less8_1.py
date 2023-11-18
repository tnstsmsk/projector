class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def drop(self, course):
        if course in self.courses:
            self.courses.remove(course)

    def view_courses(self):
        if self.courses:
            print(', '.join([course.name for course in self.courses]))
        else:
            print("No courses enrolled.")

class Course:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class University:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.courses = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def view_students(self):
        if self.students:
            print(', '.join([student.name for student in self.students]))
        else:
            print("No students in the university.")

    def view_courses(self):
        if self.students:
            for student in self.students:
                print(f"{student.name}: {', '.join([course.name for course in student.courses])}")
        else:
            print("No students in the university.")


uni = University("Harvard")

maths = Course("Mathematics", "MATH101")
physics = Course("Physics", "PHYS101")

uni.add_course(maths)
uni.add_course(physics)

alice = Student("Alice", "S101")

uni.add_student(alice)
alice.enroll(maths)

alice.view_courses()
uni.view_students()
uni.view_courses()
