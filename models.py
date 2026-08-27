class Student:
    def __init__(
        self,
        student_id: int,
        name: str,
        age: int,
        marks: float
    ) -> None:
        self.student_id = student_id
        self.name = name
        self.age = age
        self.marks = marks