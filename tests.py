import unittest
from Classroom import Classroom
from Subjects import Subject
from Human import Human
from Student import Student
from Teacher import Teacher

class TestSchoolClasses(unittest.TestCase):

    def setUp(self):
        # Создание учителя
        self.teacher = Teacher('Петр', 'Горуйкин', [Subject.MATH, Subject.PHYSICS])
        # Создание класса
        self.classroom_instance = Classroom(grade=5, letter='А', homeroom_teacher=self.teacher)

    def test_add_student(self):
        # Добавление учеников
        student1 = Student('Александр', 'Бутырин')
        student2 = Student('Илья', 'Серов')
        self.classroom_instance.add_student(student1)
        self.classroom_instance.add_student(student2)

        # Проверка, что ученики добавлены
        self.assertIn(student1, self.classroom_instance.students)
        self.assertIn(student2, self.classroom_instance.students)

    def test_lastname_sort(self):
        # Добавление учеников в произвольном порядке
        student1 = Student('Петр', 'Горуйкин')
        student2 = Student('Александр', 'Бутырин')
        student3 = Student('Илья', 'Серов')
        self.classroom_instance.add_student(student2)
        self.classroom_instance.add_student(student3)
        self.classroom_instance.add_student(student1)
        sorted_students = self.classroom_instance.get_students_sorted_by_last_name()
        expected_sorted_students = sorted(self.classroom_instance.students, key=lambda student: student.last_name)
        self.assertEqual(sorted_students, expected_sorted_students)

    def test_find_student_by_substring(self):
        # Добавление учеников
        student1 = Student('Петр', 'Горуйкин')
        student2 = Student('Александр', 'Бутырин')
        student3 = Student('Илья', 'Серов')
        self.classroom_instance.add_student(student1)
        self.classroom_instance.add_student(student2)
        self.classroom_instance.add_student(student3)

        # Поиск ученика по подстроке
        found_students = self.classroom_instance.find_student_by_substring('икт')
        self.assertIn(student3, found_students)
        self.assertNotIn(student1, found_students)
        self.assertNotIn(student2, found_students)

    def test_grade_setter(self):
        # Проверка установки корректного значения класса
        self.classroom_instance.grade = 5
        self.assertEqual(self.classroom_instance.grade, 5)

        # Проверка вызова исключения при некорректном значении
        with self.assertRaises(ValueError):
            self.classroom_instance.grade = 12

    def test_letter_setter(self):
        # Проверка установки корректного значения буквы класса
        self.classroom_instance.letter = 'А'
        self.assertEqual(self.classroom_instance.letter, 'А')

        # Проверка вызова исключения при некорректном значении
        with self.assertRaises(ValueError):
            self.classroom_instance.letter = '1'

    def test_repr_method(self):
        # Проверка работы метода __repr__
        student = Student('Петр', 'Горуйкин')
        self.classroom_instance.add_student(student)
        classroom_repr = repr(self.classroom_instance)
        self.assertIn("Ученик (Имя = 'Петр', Фамилия = 'Горуйкин')", classroom_repr)


if __name__ == '__main__':
    unittest.main()