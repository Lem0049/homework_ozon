class Person:
    """Базовый класс для студентов"""

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'


if __name__ == '__main__':
    ivn = Person('Ivan', 'Ivanov')
    print(ivn)
    petr = Person('Petr', 'Petrov')
    print(petr)
