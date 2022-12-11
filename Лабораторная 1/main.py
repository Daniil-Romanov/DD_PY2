from typing import Union
import doctest

brand_list = ["Samsung", "Lenovo", "Asus", "Apple"]  # список "разрешенных" брендов
color_list = ["белый", "синий", "красный", "зеленый", "фиолетовый"]  # список возможных цветов
dopsa_list = {"Петров": "Максим", "Иванов": "Константин"}  # список на отчисление


class Phone:
    def __init__(self, brand: str, RAM: int, diagonal: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Мобильный телефон"
        :param brand: Бренд телефона
        :param RAM: Объем оперативной памяти(в Гигабайтах)
        :param diagonal: Диагональ экрана(в дюймах)

        Примеры:
        >>> phone = Phone("Samsung", 64, 5.8) # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Название бренда должно быть типа str")
        self.brand = brand

        if not isinstance(RAM, int):
            raise TypeError("Объем памяти должно быть типа int")
        if RAM < 0:
            raise ValueError("Объем памяти должен быть не меньше 0")
        self.RAM = RAM

        if not isinstance(diagonal, (int, float)):
            raise TypeError("Диагональ экрана должна быть типа int или float")
        if not diagonal > 0:
            raise ValueError("Диагональ экрана должна быть больше 0")
        self.diagonal = diagonal

    def brand_in_list(self) -> bool:
        """
        Функция которая проверяет является ли бренд "разрешенным", то есть входит в brand_list

        :return: Является ли бренд "разрешенным"

        Примеры:
        >>> phone = Phone("Samsung", 64, 5.8)
        >>> phone.brand_in_list()
        """
        ...

    def RAM_test(self, need_RAM: int) -> bool:
        """
        Функция которая проверяет достаточно ли оперативной памяти для пользователя
        :param need_RAM: Необходимый объем для пользователя

        :return: Достаточно ли оперативной памяти для пользователя

        Примеры:
        >>> phone = Phone("Samsung", 64, 5.8)
        >>> phone.RAM_test(32)
        """
        if not isinstance(need_RAM, int):
            raise TypeError("Необходимый объем должен быть типа int")
        if need_RAM < 0:
            raise ValueError("Необходимый объем должен быть не меньше 0")
        ...

    def diagonal_test(self, min_diag: Union[int, float], max_diag: Union[int, float]) -> bool:
        """
        Функция которая проверяет нормальная ли диагональ экрана для пользователя
        :param min_diag: Минимальная диагональ экрана для пользователя
        :param max_diag: Максимальная диагональ экрана для пользователя

        :return: Нормальная ли диагональ экрана для пользователя

        Примеры:
        >>> phone = Phone("Samsung", 64, 5.8)
        >>> phone.diagonal_test(5, 6.5)
        """
        if not isinstance(min_diag, (int, float)):
            raise TypeError("Диагональ должна быть типа int или float")
        if min_diag < 0:
            raise ValueError("Диагональ должна быть не меньше 0")

        if not isinstance(max_diag, (int, float)):
            raise TypeError("Диагональ должна быть типа int или float")
        if not max_diag > 0:
            raise ValueError("Диагональ должна быть больше 0")

        if min_diag > max_diag:
            raise ValueError("Минимальная диагональ должна быть меньше максимальной!")
        ...


class SmartLedLamp:
    def __init__(self, color: str, power: int, on_off: int):
        """
        Создание и подготовка к работе объекта "Умная светодиодная лампочка"
        :param color: Цвет света лампочки(цвета из color_list)
        :param power: Яркость лампочки(в процентах), не может быть 0!!!
        :param on_off: Положение: включена(1) или выключена(0)

        Примеры:
        >>> lamp = SmartLedLamp("белый", 100, 1) # инициализация экземпляра класса
        """
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть типа str")
        if color not in color_list:
            raise NameError("Лампочка не может гореть таким цветом!")
        self.color = color

        if not isinstance(power, int):
            raise TypeError("Яркость должна быть типа int")
        if power <= 0 or power > 100:
            raise ValueError("Неправильные проценты яркости")
        self.power = power

        if not isinstance(on_off, int):
            raise TypeError("Положение должно быть типа int")
        if on_off != 0 and on_off != 1:
            raise ValueError("Неправильные значения положения")
        self.on_off = on_off

    def change_color(self, new_color: str) -> None:
        """
        Функция которая меняет цвет лампочки на введенный пользователем
        :param new_color: Новый цвет лампочки(из того же списка color_list)

        Примеры:
        >>> lamp = SmartLedLamp("белый", 100, 1)
        >>> lamp.change_color("синий")
        """
        if not isinstance(new_color, str):
            raise TypeError("Новый цвет должен быть типа str")
        if new_color not in color_list:
            raise NameError("Лампочка не может гореть таким цветом!")
        ...

    def change_power(self, new_power: int) -> None:
        """
        Функция которая меняет яркость лампочки на новое значение процентов
        :param new_power: Новая яркость лампочки(также не может быть 0)

        Примеры:
        >>> lamp = SmartLedLamp("белый", 100, 1)
        >>> lamp.change_power(50)
        """
        if not isinstance(new_power, int):
            raise TypeError("Новая яркость должна быть типа int")
        if new_power <= 0 or new_power > 100:
            raise ValueError("Неправильные проценты яркости")
        ...

    def change_on_off(self) -> None:
        """
        Функция которая меняет положение лампочки на противоположное

        Примеры:
        >>> lamp = SmartLedLamp("белый", 100, 1)
        >>> lamp.change_on_off()
        """
        ...


class Student:
    def __init__(self, surname: str, name: str, age: int, height: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Студент"
        :param surname: Фамилия студента
        :param name: Имя студента
        :param age: Возраст студента(0 - 100 лет)
        :param height: Рост студента(50 - 250 см)

        Примеры:
        >>> student = Student("Романов", "Даниил", 19, 174) # инициализация экземпляра класса
        """
        if not isinstance(surname, str):
            raise TypeError("Фамилия должна быть типа str")
        self.surname = surname

        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if age < 0 or age > 100:
            raise ValueError("Неправильный возраст!")
        self.age = age

        if not isinstance(height, (int, float)):
            raise TypeError("Рост должен быть типа int или float")
        if height < 50 or height > 250:
            raise ValueError("Неправильный рост!")
        self.height = height

    def student_in_list(self) -> bool:
        """
        Функция которая проверяет есть ли студент в списке на отчисление

        :return: Есть ли студент в списке

        Примеры:
        >>> student = Student("Романов", "Даниил", 19, 174)
        >>> student.student_in_list()
        """
        # в словаре dopsa_list: ключ - фамилия, значение - имя
        ...

    def age_18(self) -> bool:
        """
        Функция которая проверяет есть ли студенту 18 лет

        :return: Есть ли студенту 18 лет

        Примеры:
        >>> student = Student("Романов", "Даниил", 19, 174)
        >>> student.age_18()
        """
        ...

    def height_test(self, need_height: Union[int, float]) -> bool:
        """
        Функция которая проверяет имеет ли студент необходимый рост
        :param need_height: Необходимый рост

        :return: Достаточный ли рост у студента

        Примеры:
        >>> student = Student("Романов", "Даниил", 19, 174)
        >>> student.height_test(170)
        """
        if not isinstance(need_height, (int, float)):
            raise TypeError("Необходимый рост должен быть типа int или float")
        if need_height < 0 or need_height > 250:
            raise ValueError("Необходимый рост должен быть в пределах разумного")
        ...


if __name__ == "__main__":
    doctest.testmod()  # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
