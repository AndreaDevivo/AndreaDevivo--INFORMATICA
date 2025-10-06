from arma import Arma

class Giocatore:
    def __init__(self, nome: str, salute_massima: int, forza: int, destrezza: int):
        self.nome = nome
        self.salute_massima = max(1, salute_massima)
        self.salute = self.salute_massima
        self.forza = max(1, min(20, forza))
        self.destrezza = max(1, min(20, destrezza))
        self.arma: Arma | None = None

    def equipaggia(self, arma: Arma):
        self.arma = arma

    def modificatore(self, valore: int) -> int:
        return (valore - 10) // 2

    def è_vivo(self) -> bool:
        return self.salute > 0

    def subisce(self, danno: int) -> int:
        danno_effettivo = max(0, danno)
        self.salute = max(0, self.salute - danno_effettivo)
        return danno_effettivo

    def attacca(self, nemico: "Giocatore") -> int:
        if self.arma is None:
            danno_base = 1
            modificatore = self.modificatore(self.forza)
        else:
            danno_base = self.arma.get_danno()
            if self.arma.tipo == "mischia":
                modificatore = self.modificatore(self.forza)
            else:
                modificatore = self.modificatore(self.destrezza)

        danno_totale = max(0, danno_base + modificatore)
        return nemico.subisce(danno_totale)

    def __str__(self):
        return f"{self.nome} (HP: {self.salute}/{self.salute_massima})"
