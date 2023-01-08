from typing import Union
import doctest


class Mage:
    def __init__(self, health:int, mana:int, stanina:int):
        """
        Создание и подготовка к работе объекта "маг"
        :param health: здоровье
        :param mana: кол во могии
        :param stanina: выносливость
        Примеры:
        >>> Merlin = Mage(200, 500, 100)  # инициализация экземпляра класса
        """
        if not isinstance(health, int):
            raise TypeError("здовье должно быть типа int")
        if health < 100:
            raise ValueError("здовье должно быть не менее 100 единиц")
        self.health = health

        if not isinstance(mana, int):
            raise TypeError("количество магии должно быть типа int")
        if mana < 100:
            raise ValueError("количество магии не меньше 100 единиц")
        self.mana = mana

        if not isinstance(stanina, int):
            raise TypeError("выносливость должна быть типа int")
        if stanina < 100:
            raise ValueError("выносливость должна быть не менее 100")
        self.stanina = stanina

    def fire_ball(self, spend_mana:int) -> None:
        """
        кастуем огненный шар - расходуем ману
        :param fire_ball: стоимость шара в единицах магии.
        :raise ValueError: если стоимость огненного шара превышает остаток маны, возвращается ошибка
        Примеры:
        >>> Merlin = Mage(200, 500, 100)
        >>> Merlin.fire_ball(250)
        """
        if not isinstance(spend_mana, int):
            raise TypeError("стоимость шара должна быть типа int")
        if spend_mana < 50:
            raise ValueError("стоимость шара не ниже 50 единиц магии")
        ...

    def elixir(self, get_mana:int) -> None:
        """
        восстановление маны.
        :param elixir: кол во полученной маны.
        :raise ValueError: Если количество магии элексира превышает количество магии возвращается ошибка.
        Примеры:
        >>> Merlin = Mage(200, 500, 100)
        >>> Merlin.elixir(250)
        """
        if not isinstance(get_mana, int):
            raise TypeError("кол во полученной маны должно быть типа int")
        if get_mana > 500:
            raise ValueError("количество полученной маны ниже 500 единиц магии")
        ...

class giant:
    def __init__(self, health:int, mana:int, stanina:int):
        """
        Создание и подготовка к работе объекта "великан"
        :param health: здоровье
        :param mana: кол во могии
        :param stanina: выносливость
        Примеры:
        >>> Vyn_Vyn = giant(500, 100, 300)  # инициализация экземпляра класса
        """
        if not isinstance(health, int):
            raise TypeError("здовье должно быть типа int")
        if health < 100:
            raise ValueError("здовье должно быть не менее 100 единиц")
        self.health = health

        if not isinstance(mana, int):
            raise TypeError("количество магии должно быть типа int")
        if mana < 100:
            raise ValueError("количество магии не меньше 100 единиц")
        self.mana = mana

        if not isinstance(stanina, int):
            raise TypeError("выносливость должна быть типа int")
        if stanina < 100:
            raise ValueError("выносливость должна быть не менее 100")
        self.stanina = stanina

    def giant_shield(self, spend_health:int) -> None:
        """
        активируем режим щита, переманивая противников на себя - тратим здоровье
        :param deadly_dash: стоимость режима щита в единицах здоровья.
        :raise ValueError: если стоимость режима щита превышает здоровье, возвращается ошибка
        Примеры:
        >>> Vyn_Vyn = giant(500, 100, 300)
        >>> Vyn_Vyn.giant_shield(250)
        """
        if not isinstance(spend_health, int):
            raise TypeError("стоимость щита должна быть типа int")
        if spend_health < 100:
            raise ValueError("стоимость щита не ниже 50 единиц здоровья")
        ...

    def potion(self, get_health:int) -> None:
        """
        восстановление здоровья.
        :param potion: кол во полученной здоровья.
        :raise ValueError: Если количество полученного здоровья превышает количество здоровья возвращается ошибка.
        Примеры:
        >>> Vyn_Vyn = giant(500, 100, 300)
        >>> Vyn_Vyn.potion(250)
        """
        if not isinstance(get_health, int):
            raise TypeError("кол во полученного здоровья должно быть типа int")
        if get_health > 500:
            raise ValueError("количество полученного здоровья ниже 500 единиц")
        ...

class Berserker:
    def __init__(self, health:int, mana:int, stanina:int):
        """
        Создание и подготовка к работе объекта "берсерк"
        :param health: здоровье
        :param mana: кол во могии
        :param stanina: выносливость
        Примеры:
        >>> Cratos = Berserker(300, 100, 500)  # инициализация экземпляра класса
        """
        if not isinstance(health, int):
            raise TypeError("здовье должно быть типа int")
        if health < 100:
            raise ValueError("здовье должно быть не менее 100 единиц")
        self.health = health

        if not isinstance(mana, int):
            raise TypeError("количество магии должно быть типа int")
        if mana < 100:
            raise ValueError("количество магии не меньше 100 единиц")
        self.mana = mana

        if not isinstance(stanina, int):
            raise TypeError("выносливость должна быть типа int")
        if stanina < 100:
            raise ValueError("выносливость должна быть не менее 100")
        self.stanina = stanina

    def berserk_mode(self, spend_stanina:int) -> None:
        """
        активируем режим берсерка - тратим станину
        :param berserk_mode: стоимость режима берсерка в очках станины.
        :raise ValueError: если стоимость режима берсерка превышает остаток станины, возвращается ошибка
        Примеры:
        >>> Cratos = Berserker(300, 100, 500)
        >>> Cratos.berserk_mode(250)
        """
        if not isinstance(spend_stanina, int):
            raise TypeError("стоимость режима берсерка должна быть типа int")
        if spend_stanina < 100:
            raise ValueError("стоимость режима берсерка не ниже 100 единиц станины")
        ...

    def sleep(self, get_stanina:int) -> None:
        """
        сон возвращает выносливость.
        :param sleep: кол во полученной станины.
        :raise ValueError: Если количество если количество станины от сна превышает количество станины, возвращается ошибка.
        Примеры:
        >>> Cratos = Berserker(300, 100, 500)
        >>> Cratos.sleep(250)
        """
        if not isinstance(get_stanina, int):
            raise TypeError("кол во полученной станины должно быть типа int")
        if get_stanina > 500:
            raise ValueError("количество полученной станины ниже 500 единиц")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации


