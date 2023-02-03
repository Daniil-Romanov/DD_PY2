from typing import Union  # добавляю Union для класса AudioBook


class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f'Книга "{self.name}". Автор {self.author}.'

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self):
        """getter делает этот атрибут неизменяемым со стороны пользователя."""

        return self._name  # обращение к защищенному атрибуту

    @property
    def author(self):
        """getter делает этот атрибут неизменяемым со стороны пользователя."""

        return self._author  # обращение к защищенному атрибуту


class PaperBook(Book):
    """ Производный класс бумажной книги. """

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)  # наследование конструктора из базового класса
        self.pages = pages

    def __repr__(self):  # наследовать нельзя, так как добавляется дополнительный атрибут, надо перегружать
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"

    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге."""

        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """Устанавливает количество страниц в книге."""

        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц в книге должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть больше 0")
        self._pages = new_pages


class AudioBook(Book):
    """ Производный класс аудиокниги. """

    def __init__(self, name: str, author: str, duration: Union[float, int]):
        super().__init__(name, author)  # наследование конструктора из базового класса
        self.duration = duration

    def __repr__(self):  # наследовать нельзя, так как добавляется дополнительный атрибут, надо перегружать
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

    @property
    def duration(self) -> Union[float, int]:
        """Возвращает продолжительность аудиокниги."""

        return self._duration

    @duration.setter
    def duration(self, new_duration: Union[int, float]) -> None:
        """Устанавливает продолжительность аудиокниги."""

        if not isinstance(new_duration, Union[int, float]):
            raise TypeError("Продолжительность аудиокниги должна быть типа int или float")
        if new_duration <= 0:
            raise ValueError("Продолжительность аудиокниги должна быть больше 0")
        self._duration = new_duration
