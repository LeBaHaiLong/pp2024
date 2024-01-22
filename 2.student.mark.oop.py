class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_mark(self, course_id, mark):
        self.marks[course_id] = mark

    def get_marks(self, course_id):
        return self.marks.get(course_id)

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class MarkManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def input_students(self):
        num_students = int(input("Enter the number of students in the class: "))
        for i in range(num_students):
            student_id = input("Enter student ID: ")
            student_name = input("Enter student name: ")
            student_dob = input("Enter student date of birth (DoB): ")
            student = Student(student_id, student_name, student_dob)
            self.add_student(student)

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for i in range(num_courses):
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            course = Course(course_id, course_name)
            self.add_course(course)

    def input_marks(self):
        course_id = input("Enter course ID: ")
        course = None
        for c in self.courses:
            if c.id == course_id:
                course = c
                break
        if course is None:
            print("Course not found")
            return
        for s in self.students:
            mark = input(f"Enter mark for {s.name}: ")
            s.add_mark(course_id, mark)

    def list_courses(self):
        print("Courses:")
        for c in self.courses:
            print(f"{c.id}: {c.name}")

    def list_students(self):
        print("Students:")
        for s in self.students:
            print(f"{s.id}: {s.name}")

    def show_marks(self):
        course_id = input("Enter course ID: ")
        course = None
        for c in self.courses:
            if c.id == course_id:
                course = c
                break
        if course is None:
            print("Course not found")
            return
        print(f"Marks for {course.name}:")
        for s in self.students:
            mark = s.get_marks(course_id)
            if mark is not None:
                print(f"{s.name}: {mark}")

system = MarkManagementSystem()
system.input_students()
system.input_courses()

while True:
    print("1. Input marks")
    print("2. List courses")
    print("3. List students")
    print("4. Show marks for a course")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        system.input_marks()
    elif choice == "2":
        system.list_courses()
    elif choice == "3":
        system.list_students()
    elif choice == "4":
        system.show_marks()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
