from weapon import Weapon
from potion import Potion
import random

class Player:
    def __init__(self, name: str, max_health: int, strength: int, dexterity: int, weapon):
        # --- VALIDAZIONE COME DA TESTO ---
        if name == "":
            raise ValueError("Il nome del giocatore non può essere vuoto.")
        if max_health <= 0:
            raise ValueError("I punti vita massimi devono essere > 0.")
        if strength <= 0:
            raise ValueError("La forza deve essere > 0.")
        if dexterity <= 0:
            raise ValueError("La destrezza deve essere > 0.")
        # ----------------------------------

        self.__name = name
        self.__max_health = max_health
        self.__health = max_health
        self.__strength = strength
        self.__dexterity = dexterity
        self.__weapon = weapon
        self.__buffs = []
        self.__potions = []

    @property
    def name(self): return self.__name
    @property
    def health(self): return self.__health
    @property
    def max_health(self): return self.__max_health
    @property
    def strength(self): return self.__strength
    @property
    def dexterity(self): return self.__dexterity

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        elif value > self.__max_health:
            self.__health = self.__max_health
        else:
            self.__health = value

    def take_damage(self, amount: int):
        # --- VALIDAZIONE COME DA TESTO ---
        if type(amount) is not int:
            raise TypeError("Il danno subito deve essere un numero intero.")
        if amount < 0:
            raise ValueError("Il danno non può essere negativo.")
        # ----------------------------------
        self.health = self.__health - amount
        return amount

    def heal(self, amount: int):
        # --- VALIDAZIONE COME DA TESTO ---
        if type(amount) is not int:
            raise TypeError("Il valore di cura deve essere un intero.")
        if amount < 0:
            raise ValueError("Il valore di cura non può essere negativo.")
        # ----------------------------------
        vecchi_hp = self.__health
        self.health = self.__health + amount
        return self.__health - vecchi_hp

    def equip(self, weapon):
        # --- DUCK TYPING COME DA TESTO ---
        # Controlliamo se l’oggetto "si comporta" come un’arma
        try:
            _ = weapon.min_damage
            _ = weapon.max_damage
            _ = weapon.type
        except Exception:
            raise TypeError("Oggetto non equipaggiabile, non è un’arma valida.")
        # ---------------------------------
        self.__weapon = weapon

    def add_buff(self, stat: str, amount: int, duration: int):
        self.__buffs.append((stat, amount, duration))

    def effective_strength(self):
        totale = self.__strength
        for stat, amount, dur in self.__buffs:
            if stat == "str":
                totale += amount
        return totale

    def effective_dexterity(self):
        totale = self.__dexterity
        for stat, amount, dur in self.__buffs:
            if stat == "dex":
                totale += amount
        return totale

    def attack(self, target):
        # Calcolo danno base
        if self.__weapon is None:
            tipo = "mani nude"
            base = 1
        else:
            tipo = self.__weapon.type
            base = random.randint(self.__weapon.min_damage, self.__weapon.max_damage)

        # Aggiungo bonus statistiche
        if tipo == "melee":
            base += max(0, self.effective_strength() - 10)
        elif tipo == "ranged":
            base += max(0, self.effective_dexterity() - 10)

        target.take_damage(base)
        return tipo, base

    def is_alive(self):
        return self.__health > 0

    def __str__(self):
        return f"{self.__name} (HP: {self.__health}/{self.__max_health}, STR: {self.__strength}, DEX: {self.__dexterity})"
