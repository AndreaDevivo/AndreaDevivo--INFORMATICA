class Weapon:
    def __init__(self, name: str, min_damage: int, max_damage: int, type_: str):
        # --- VALIDAZIONE COME DA TESTO ---
        if name == "":
            raise ValueError("Errore: Il nome dell'arma non può essere vuoto.")
        if min_damage < 1:
            raise ValueError("Errore: Il danno minimo deve essere almeno 1.")
        if max_damage < min_damage:
            raise ValueError("Errore: Il danno massimo non può essere inferiore al danno minimo.")
        if type_ != "melee" and type_ != "ranged":
            raise ValueError("Errore: Il tipo di arma deve essere 'melee' o 'ranged'.")
        # ---------------------------------

        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.type = type_

    def __str__(self):
        return f"{self.name} [{self.type}] {self.min_damage}-{self.max_damage} dmg"
