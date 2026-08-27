import json
from pathlib import Path

from constants import DATA_FILE
from models import Student


def save_students(students: list[Student]) -> None:
    data = []

    for student in students:
        data.append(
            {
                "student_id": student.student_id,
                "name": student.name,
                "age": student.age,
                "marks": student.marks,
            }
        )

    Path(DATA_FILE).write_text(
        json.dumps(data, indent=4),
        encoding="utf-8",
    )


def load_students() -> list[Student]:
    file_path = Path(DATA_FILE)

    if not file_path.exists():
        return []

    data = json.loads(
        file_path.read_text(encoding="utf-8")
    )

    students = []

    for student_data in data:
        student = Student(
            student_id=student_data["student_id"],
            name=student_data["name"],
            age=student_data["age"],
            marks=student_data["marks"],
        )

        students.append(student)

    return students