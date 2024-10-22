from typing import List
from Human import Human
from Classroom import Classroom
from Subjects import Subject

class Teacher(Human):
    _homeroom_class: Classroom or None
    _subjects: List[Subject]

    def __init__(self, name: str, last_name: str, *subjects, group=None):
        #print("init Teacher")
        super().__init__(name, last_name)
        self._subjects = list(*subjects)
        if group is not None:
            self.set_class(group)
        else:
            self._homeroom_class = None

    def set_class(self, group):
        if isinstance(group, Classroom):
            self._homeroom_class = group
        else:
            Exception("Класс преподователя задан не верно")

    def get_class(self):
        if self._homeroom_class is not None:
            return self._homeroom_class
        else:
            print("У преподователя не задан класс")
            #Exception("У преподователя не задан класс")

    def __repr__(self):
        return f"Учитель(Имя = '{self.name}', Фамилия = '{self.last_name}', Предмет(ы) = {self.subjects})"