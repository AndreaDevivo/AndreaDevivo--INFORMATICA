class Potion:
    VALID_EFFECTS = {"heal", "buff_str", "buff_dex"}

    def __init__(self, name: str, effect: str, amount: int, duration: int = 0):
        self.name = name
        self.effect = effect
        self.amount = amount
        self.duration = duration
        self.__consumed = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Potion name cannot be empty")
        self.__name = value

    @property
    def effect(self):
        return self.__effect

    @effect.setter
    def effect(self, value):
        if value not in self.VALID_EFFECTS:
            raise ValueError(f"Invalid potion effect: {value}")
        self.__effect = value

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        if not isinstance(value, int) or value < 1:
            raise ValueError("Potion amount must be int >= 1")
        self.__amount = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Potion duration must be int >= 0")
        self.__duration = value

    def apply_to(self, target) -> dict:
        if self.__consumed:
            print(f"Error: Potion '{self.name}' already consumed.")
            return {"error": "already_consumed"}

        # Heal effect
        if self.effect == "heal":
            if hasattr(target, "heal") and callable(getattr(target, "heal")):
                healed_amount = target.heal(self.amount)
                self.__consumed = True
                return {"effect": "heal", "amount": healed_amount, "duration": 0}
            else:
                print(f"Error: Target does not support healing.")
                return {"error": "unsupported_target"}

        # Buff effects
        elif self.effect in {"buff_str", "buff_dex"}:
            if hasattr(target, "add_buff") and callable(getattr(target, "add_buff")):
                stat = "str" if self.effect == "buff_str" else "dex"
                target.add_buff(stat, self.amount, self.duration)
                self.__consumed = True
                return {"effect": self.effect, "amount": self.amount, "duration": self.duration}
            else:
                print(f"Error: Target does not support buffs.")
                return {"error": "unsupported_target"}

        else:
            print(f"Error: Unknown effect {self.effect}")
            return {"error": "unknown_effect"}

    def __str__(self):
        if self.effect == "heal":
            return f"Potion({self.effect} +{self.amount})"
        else:
            return f"Potion({self.effect} +{self.amount} x{self.duration}t)"
