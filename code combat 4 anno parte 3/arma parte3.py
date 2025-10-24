class Weapon:
    def __init__(self, name: str, min_damage: int, max_damage: int, type_: str):
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.type = type_

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Weapon name cannot be empty.")
        self.__name = value

    @property
    def min_damage(self):
        return self.__min_damage

    @min_damage.setter
    def min_damage(self, value):
        if not isinstance(value, int) or value < 1:
            raise ValueError("min_damage must be int >= 1")
        self.__min_damage = value

    @property
    def max_damage(self):
        return self.__max_damage

    @max_damage.setter
    def max_damage(self, value):
        if not isinstance(value, int) or value < self.min_damage:
            raise ValueError("max_damage must be int >= min_damage")
        self.__max_damage = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        if value not in {"melee", "ranged"}:
            raise ValueError("Weapon type must be 'melee' or 'ranged'")
        self.__type = value

    def __str__(self):
        return f"{self.name} [{self.type}] dmg: {self.min_damage}-{self.max_damage}"
