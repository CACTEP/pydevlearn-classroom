from typing import List
import Human
import Classroom
import Subjects

class Teacher(Human):
    _homeroom_class: Classroom | None
    _subjects: List[Subject]

    def __init__(self, name, last_name, *subjects, group=None):
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