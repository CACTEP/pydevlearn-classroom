import Human
import Classroom

class Student(Human):
    _class: Classroom

    def __init__(self, name, last_name, group=None):
        #print("init STUDENT")
        self.name = name
        self.last_name = last_name
        if group is not None:
            self.set_class(group)
        else:
            self._class = None

    def set_class(self, group):
        if isinstance(group, Class):
            self._class = group
        else:
            Exception("Класс ученика задан не верно")

    def get_class(self):
        if self._class is not None:
            return self._class
        else:
            print("У ученика не задан класс")
            #Exception("У ученика не задан класс")