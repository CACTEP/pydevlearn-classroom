from Human import Human
from Classroom import Classroom

class Student(Human):
    _class: Classroom

    def __init__(self, name, last_name, group=None):
        #print("init STUDENT")
        super().__init__(name, last_name)
        if group is not None:
            self.set_class(group)
        else:
            self._class = None

    def set_class(self, group):
        if isinstance(group, Classroom):
            self._class = group
        else:
            Exception("Класс ученика задан не верно")

    def get_class(self):
        if self._class is not None:
            return self._class
        else:
            print("У ученика не задан класс")
            #Exception("У ученика не задан класс")

    def __repr__(self):
        return f"Ученик (Имя = '{self.name}', Фамилия = '{self.last_name}')"