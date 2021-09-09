from DZ_11_1 import Person


class Student(Person):
    """Класс для Студентов по группам"""

    def __init__(self, name, surname, group_number):
        super().__init__(name, surname)
        self.group_number = group_number
        self.score = []

    def __set_test_score__(self, gr):  # метод добавления оценок
        self.score.append(gr)

    def __str__(self):
        return f'{self.name} {self.surname} group №{self.group_number} оценки{self.score}'


if __name__ == '__main__':
    ivn = Student('Ivan', 'Ivanov', 8, )
    ivn.__set_test_score__(5)
    ivn.__set_test_score__(6)

    petr = Student('Petr', 'Petrov', 9)
    petr.__set_test_score__(7)
    petr.__set_test_score__(9)

    print(petr)
    print(ivn)
