from DZ_11_2 import Person
import random as rnd


class Student(Person):
    """Класс для Студентов по именам преподавателей"""

    def __init__(self, name, surname, prep_name):
        super().__init__(name, surname)
        self.prep_name = prep_name
        self.score = []

    def __set_test_score__(self, gr):
        self.score.append(gr)

    def __str__(self):
        return f'{self.name} {self.surname} group №{self.prep_name} оценки{self.score}'


class Professor(Person):
    """Класс профессоров"""

    def __init__(self, name, surname, study):
        super().__init__(name, surname)
        self.study = study

    @staticmethod
    def __test_students__(students):  # Метод тестирования студентов
        for i in students:
            i.__set_test_score__(rnd.randint(1, 10))

    def __str__(self):
        return f'Преподаватель {self.name} {self.surname} читает курс {self.study}'


if __name__ == '__main__':
    ivn = Student('Ivan', 'ivanov', 'Ordeze')
    petr = Student('Petr', 'Petrov', 'nordez')
    stu = [ivn, petr]
    ordez = Professor('Ordez', 'Grigorovich', 'alchemy')
    ordez.__test_students__(stu)
    ordez.__test_students__(stu)
    print(ordez)
    print(ivn)
    print(petr)
