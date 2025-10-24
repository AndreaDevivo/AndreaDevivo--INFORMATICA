 from potion import Potion
from weapon import Weapon

class Player:
    def __init__(self, name: str, max_health: int, strength: int, dexterity: int, weapon: Weapon | None):
        self.__name = name
        self.__max_health = max_health
        self.__health = max_health
        self.__strength = strength
        self.__dexterity = dexterity
        self.__weapon = weapon
        self.__buffs = []  # list of tuples: (stat, amount, remaining_turns)
        self.__potions = []

    @property
    def name(self):
        return self.__name

    @property
    def max_health(self):
        return self.__max_health

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = max(0, min(value, self.__max_health))

    @property
    def strength(self):
        return self.__strength

    @property
    def dexterity(self):
        return self.__dexterity

    @property
    def weapon(self):
        return self.__weapon

    @weapon.setter
    def weapon(self, w: Weapon | None):
        if w is not None and not isinstance(w, Weapon):
            raise TypeError("weapon must be a Weapon instance or None")
        self.__weapon = w

    @property
    def effective_strength(self):
        return self.__strength + sum(amount for stat, amount, _ in self.__buffs if stat == "str")

    @property
    def effective_dexterity(self):
        return self.__dexterity + sum(amount for stat, amount, _ in self.__buffs if stat == "dex")

    @property
    def potions(self):
        return self.__potions.copy()

    @potions.setter
    def potions(self, potions_list):
        if not isinstance(potions_list, list):
            raise TypeError("potions must be a list")
        if len(potions_list) > 3:
            raise ValueError("maximum 3 potions allowed")
        if not all(isinstance(p, Potion) for p in potions_list):
            raise TypeError("all items in potions must be Potion instances")
        self.__potions = potions_list.copy()

    def add_buff(self, stat: str, amount: int, duration: int) -> None:
        if stat not in ("str", "dex"):
            raise ValueError("Invalid buff stat")
        if duration <= 0:
            return
        self.__buffs.append((stat, amount, duration))

    def tick_buffs(self) -> None:
        new_buffs = []
        for stat, amount, turns in self.__buffs:
            if turns > 1:
                new_buffs.append((stat, amount, turns - 1))
        self.__buffs = new_buffs

    def is_alive(self) -> bool:
        return self.__health > 0

    def heal(self, amount: int) -> int:
        old_health = self.__health
        self.health += amount  # setter clamp
        return self.__health - old_health

    def __take(self, damage: int) -> int:
        self.health -= damage
        return damage

    def __calculate_damage(self) -> int:
        import random
        if not self.__weapon:
            base = 1
        else:
            base = random.randint(self.__weapon.min_damage, self.__weapon.max_damage)
       
        if self.__weapon:
            if self.__weapon.type == "melee":
                base += max(0, self.effective_strength - 10)
            else:
                base += max(0, self.effective_dexterity - 10)
        return max(0, base)

    def attack(self, enemy: "Player") -> int:
        dmg = self.__calculate_damage()
        enemy.__take(dmg)
        return dmg

    def use_potion(self, p: Potion) -> dict:
        if p not in self.__potions:
            print("Potion not in inventory")
            return {"error": "not_in_inventory"}
        result = p.apply_to(self)
        if "error" not in result:
            self.__potions.remove(p)
        return result

    def should_use_potion(self, enemy: "Player") -> Potion | None:
       
        for p in self.__potions:
            if p.effect == "heal" and self.health / self.max_health <= 0.3:
                return p
      
        active_buffs = [b for b in self.__buffs if b[2] > 0]
        if not active_buffs:
            for p in self.__potions:
                if p.effect in {"buff_str", "buff_dex"}:
                    return p
        return None
