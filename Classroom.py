from typing import List

class Classroom(list):
    _grade: int
    _letter: str
    _students: List["Student"]
    _homeroom_teacher: "Teacher"
    ...

    def __init__(self, grade, letter):
        self._grade = grade
        self._letter = letter

    def __getitem__(self, name):

        ...

    def __len__(self):
        return len(self._students)

    def __str__(self):
        return f"Класс {self._grade}{self._letter}, преподователь - {self._homeroom_teacher}, ученики: {self._students}"

    def otlist():
      #super().append
      pass