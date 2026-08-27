from models import Student
from storage import load_students, save_students
from utils import (
    format_student,
    get_valid_age,
    get_valid_marks,
    print_error,
    print_success,
    print_title,
)


def add_student(students: list[Student]) -> None:
    print_title("ADD STUDENT")

    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print_error("Student ID must be a whole number.")
        return

    name = input("Enter student name: ").strip()

    if not name:
        print_error("Student name cannot be empty.")
        return

    age = get_valid_age()
    marks = get_valid_marks()

    student = Student(
        student_id=student_id,
        name=name,
        age=age,
        marks=marks,
    )

    students.append(student)
    save_students(students)

    print_success("Student added successfully!")


def display_students(students: list[Student]) -> None:
    print_title("ALL STUDENTS")

    if not students:
        print_error("No students found.")
        return

    for student in students:
        print(format_student(student))


def search_student(students: list[Student]) -> None:
    print_title("SEARCH STUDENT")

    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print_error("Student ID must be a whole number.")
        return

    for student in students:
        if student.student_id == student_id:
            print_success("Student found!")
            print(format_student(student))
            return

    print_error("Student not found.")


def delete_student(students: list[Student]) -> None:
    print_title("DELETE STUDENT")

    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print_error("Student ID must be a whole number.")
        return

    for student in students:
        if student.student_id == student_id:
            students.remove(student)
            save_students(students)

            print_success("Student deleted successfully!")
            return

    print_error("Student not found.")


def show_menu() -> None:
    print_title("STUDENT RECORD MANAGER")

    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")


def main() -> None:
    students = load_students()

    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            display_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            delete_student(students)

        elif choice == "5":
            print_success("Goodbye!")
            break

        else:
            print_error("Invalid choice. Please select 1-5.")

        print()


if __name__ == "__main__":
    main()