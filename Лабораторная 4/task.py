import doctest


class People:
    """ Базовый класс людей. """

    def __init__(self, name: str, surname: str, age: int):
        """
        Создание и подготовка к работе объекта "Человек"
        :param name: Имя человека.
        :param surname: Фамилия человека.
        :param age: Возраст человека.

        Примеры:
        >>> man = People("Иван", "Петров", 18) # инициализация экземпляра класса
        """

        if not isinstance(name, str):
            raise TypeError("Имя человека должно быть типа str.")
        self._name = name

        if not isinstance(surname, str):
            raise TypeError("Фамилия человека должна быть типа str.")
        self._surname = surname

        if not isinstance(age, int):
            raise TypeError("Возраст человека должен быть типа int.")
        if age < 0:
            raise ValueError("Возраст человека не может быть отрицательным.")
        self.age = age

    def __str__(self):
        return f'{self.surname} {self.name}. Возраст: {self.age}.'

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, surname={self.surname!r}, age={self.age})'

    @property
    def name(self):  # должен быть защищенным, так как имя человека нельзя изменить
        """getter делает этот атрибут неизменяемым со стороны пользователя."""

        return self._name  # обращение к защищенному атрибуту

    @property
    def surname(self):  # должен быть защищенным, так как фамилию человека нельзя изменить
        """getter делает этот атрибут неизменяемым со стороны пользователя."""

        return self._surname  # обращение к защищенному атрибуту

    # age остается публичным, так как возраст у человека меняется

    def check_age(self, need_age: int) -> bool:
        """
        Проверяет больше ли возраст человека, чем необходимый, который принимает на вход.

        :param need_age: Необходимый возраст человека.

        :return: Достиг ли человек этого возраста.

        Примеры:
        >>> woman = People("Маша", "Сидорова", 20) # инициализация экземпляра класса
        >>> woman.check_age(5)
        """


class Pupil(People):
    """ Производный класс школьников. """

    def __init__(self, name: str, surname: str, age: int, school_number: int, class_number: int):
        """
        Создание и подготовка к работе объекта "Школьник"
        :param name: Имя человека.
        :param surname: Фамилия человека.
        :param age: Возраст человека.
        :param school_number: Номер школы.
        :param class_number: Номер класса (1 - 11 класс).

        Примеры:
        >>> pupil = Pupil("Петр", "Иванов", 10, 55, 3)  # инициализация экземпляра класса
        """
        super().__init__(name, surname, age)

        if not isinstance(school_number, int):
            raise TypeError("Номер школы должен быть типа int.")
        if not school_number > 0:
            raise ValueError("Номер школы должен быть положительным.")
        self.school_number = school_number

        if not isinstance(class_number, int):
            raise TypeError("Номер класса должен быть типа int.")
        if not 1 <= class_number <= 11:
            raise ValueError("Номер класса должен быть от 1 до 11.")
        self.class_number = class_number

    # str не буду перегружать, так как будет печататься одна и та же строка без изменений

    def __repr__(self):  # repr надо перегрузить, так как меняется количество аргументов
        return f'{self.__class__.__name__}(name={self.name!r}, surname={self.surname!r}, age={self.age}, school_number={self.school_number}, class_number={self.class_number})'

    # school_number остается публичным, так как ученик может сменить школу

    # class_number остается публичным, так как ученик перейдет в следующий класс

    # метод check_age наследуется


class Student(People):
    """ Производный класс студентов. """

    def __init__(self, name: str, surname: str, age: int, curs_number: int):
        """
        Создание и подготовка к работе объекта "Школьник"
        :param name: Имя человека.
        :param surname: Фамилия человека.
        :param age: Возраст человека.
        :param curs_number: Номер курса (1 - 6 курс).

        Примеры:
        >>> student = Student("Даниил", "Романов", 19, 2)  # инициализация экземпляра класса
        """
        super().__init__(name, surname, age)

        if not isinstance(curs_number, int):
            raise TypeError("Номер курса должен быть типа int.")
        if not 1 <= curs_number <= 6:
            raise ValueError("Номер курса должен быть от 1 до 6.")
        self.curs_number = curs_number

    # str не буду перегружать, так как будет печататься одна и та же строка без изменений

    def __repr__(self):  # repr надо перегрузить, так как меняется количество аргументов
        return f'{self.__class__.__name__}(name={self.name!r}, surname={self.surname!r}, age={self.age}, curs_number={self.curs_number})'

    # curs_number остается публичным, так как студент перейдет на следующий курс (наверное)

    # метод check_age наследуется


if __name__ == "__main__":
    doctest.testmod()
    pass
