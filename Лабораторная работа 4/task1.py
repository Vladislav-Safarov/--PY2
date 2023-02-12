class house:
    """ Базовый класс дом. """
    def __init__(self, adres: str, price: str):
        self._adres = adres
        self._price = price
        if not isinstance(adres, str):
            raise TypeError("Адрес должен быть типа str")
        if not isinstance(price, str):
            raise TypeError("Стоимость должна быть типа str, например Х млн. р.")
    @property
    def adres(self) ->str:
        return self._adres
    @property
    def price(self) ->str:
        return self._price
    def __str__(self):
        return f"Адрес {self.adres}. Стоимость {self.price}"

    def __repr__(self):
        return f"{self.__class__.__name__}(address={self.adres!r}, price={self.price!r})"


class privatehouse(house):
    def __init__(self, adres: str, price: str, size: int):
        super().__init__(adres, price)
        if not isinstance(size, int):
            raise TypeError("Размер дома должен быть типа int")
        if size < 0:
            raise ValueError("Размер дома должен быть больше 0")
        self.size = size

    def __str__(self):
        return f"Адрес частного дома- {self.adres}. Цена - {self.price}. Размер - {self.size}"
    def __repr__(self):
        return f"{self.__class__.__name__}(address={self.adres!r}, price={self.price!r}, size={self.size!r})"




class highrisebuilding(house):
    def __init__(self, adres: str, price: str, level: int):
        super().__init__(adres, price)
        if not isinstance(level, int):
            raise TypeError("Этаж должен быть типа int")
        if level < 0:
            raise ValueError("этаж дожен быть больше 0")
        self.level = level


    def __str__(self):
        return f"Адрес многоквартиного дома - {self.adres}. Цена - {self.price}. Этаж - {self.level}"
    def __repr__(self):
        return f"{self.__class__.__name__}(address={self.adres!r}, price={self.price!r}, level={self.level!r})"

print(privatehouse("Иванова 10", "10 млн. р.", 300))
print(privatehouse("Косыгина 65", "5 млн. р.", 100))
print(highrisebuilding("Жукова 16", "7 млн. р.", 13))

if __name__ == "__main__":
    # Write your solution here
    pass