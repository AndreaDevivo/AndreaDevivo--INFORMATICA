class Potion:
    def __init__(self, name: str, effect: str, amount: int, duration: int = 0):
        if name == "":
            raise ValueError("Il nome della pozione non può essere vuoto.")
        if effect not in ["heal", "buff_str", "buff_dex"]:
            raise ValueError("Effetto non valido.")
        if amount < 1:
            raise ValueError("Il valore della pozione deve essere >= 1.")
        if duration < 0:
            raise ValueError("La durata deve essere >= 0.")

        self.name = name
        self.effect = effect
        self.amount = amount
        self.duration = duration
        self.__consumed = False

    def apply_to(self, target):
        if self.__consumed:
            raise ValueError("Pozione già usata.")

        # --- VALIDAZIONE COME DA TESTO ---
        if self.effect == "heal" and target.health == target.max_health:
            raise ValueError(f"{target.name} ha già gli HP al massimo.")
        if self.effect == "buff_str":
            for stat, amount, turns in target._Player__buffs:
                if stat == "str":
                    raise ValueError("Buff alla forza già attivo.")
        if self.effect == "buff_dex":
            for stat, amount, turns in target._Player__buffs:
                if stat == "dex":
                    raise ValueError("Buff alla destrezza già attivo.")
        # ---------------------------------

        # Applicazione effetto
        if self.effect == "heal":
            cura = target.heal(self.amount)
            self.__consumed = True
            return f"{self.name} (+{cura} HP)"
        elif self.effect == "buff_str":
            target.add_buff("str", self.amount, self.duration)
            self.__consumed = True
            return f"{self.name} (+{self.amount} STR x{self.duration}t)"
        elif self.effect == "buff_dex":
            target.add_buff("dex", self.amount, self.duration)
            self.__consumed = True
            return f"{self.name} (+{self.amount} DEX x{self.duration}t)"
