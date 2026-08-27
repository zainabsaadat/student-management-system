from colorama import Fore, Style, init

from constants import MAX_AGE, MAX_MARKS, MIN_AGE, MIN_MARKS
from models import Student

init(autoreset=True)


def print_title(title: str) -> None:
    print(Fore.CYAN + "=" * 40)
    print(Fore.YELLOW + title.center(40))
    print(Fore.CYAN + "=" * 40)


def print_success(message: str) -> None:
    print(Fore.GREEN + message)


def print_error(message: str) -> None:
    print(Fore.RED + message)


def format_student(student: Student) -> str:
    return (
        f"ID: {student.student_id} | "
        f"Name: {student.name} | "
        f"Age: {student.age} | "
        f"Marks: {student.marks}"
    )


def get_valid_age() -> int:
    while True:
        try:
            age = int(input("Enter student age: "))

            if MIN_AGE <= age <= MAX_AGE:
                return age

            print_error(
                f"Age must be between {MIN_AGE} and {MAX_AGE}."
            )

        except ValueError:
            print_error("Please enter a valid whole number.")


def get_valid_marks() -> float:
    while True:
        try:
            marks = float(input("Enter student marks: "))

            if MIN_MARKS <= marks <= MAX_MARKS:
                return marks

            print_error(
                f"Marks must be between {MIN_MARKS} and {MAX_MARKS}."
            )

        except ValueError:
            print_error("Please enter a valid number.")