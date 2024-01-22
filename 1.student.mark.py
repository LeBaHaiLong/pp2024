def input_students():
    num_students = int(input("Enter the number of students in the class: "))
    students = []
    for i in range(num_students):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student date of birth (DoB): ")
        student = (student_id, student_name, student_dob)
        students.append(student)
    return students

def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    courses = []
    for i in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        course = (course_id, course_name)
        courses.append(course)
    return courses

def input_marks(students, courses):
    course_id = input("Enter course ID: ")
    course = None
    for c in courses:
        if c[0] == course_id:
            course = c
            break
    if course is None:
        print("Course not found")
        return
    marks = {}
    for s in students:
        mark = input(f"Enter mark for {s[1]}: ")
        marks[s[0]] = mark
    return (course, marks)

def list_courses(courses):
    print("Courses:")
    for c in courses:
        print(f"{c[0]}: {c[1]}")

def list_students(students):
    print("Students:")
    for s in students:
        print(f"{s[0]}: {s[1]}")

def show_marks(course, marks):
    print(f"Marks for {course[1]}:")
    for s in marks:
        print(f"{s}: {marks[s]}")

students = input_students()
courses = input_courses()

while True:
    print("1. Input marks")
    print("2. List courses")
    print("3. List students")
    print("4. Show marks for a course")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        input_marks(students, courses)
    elif choice == "2":
        list_courses(courses)
    elif choice == "3":
        list_students(students)
    elif choice == "4":
        course, marks = input_marks(students, courses)
        show_marks(course, marks)
    elif choice == "5":
        break
    else:
        print("Invalid choice")
