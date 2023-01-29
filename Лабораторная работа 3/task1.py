class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author
    @property
    def name(self) ->str:
        return self._name
    @property
    def author(self) ->str:
        return self._author
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages < 0:
            raise ValueError("количество страниц должно быть больше 0")
        self.pages = pages

    def __str__(self):
        return f"Бумажная книга - {self.name}. Автор - {self.author}. Страниц - {self.pages}"
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"




class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, int):
            raise TypeError("Длительность должна быть типа int")
        if duration < 0:
            raise ValueError("Длительность должна быть больше 0")
        self.duration = duration


    def __str__(self):
        return f"Аудио книга - {self.name}. Автор - {self.author}. Длительность - {self.duration} минут"
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

print(PaperBook("Золотая рыбка", "Пушкин", 100))
print(PaperBook("Кавказский пленник", "Лермонтов", 200))
print(AudioBook("Капитал", "Маркс", 40))