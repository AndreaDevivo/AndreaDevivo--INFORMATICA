import random

class Arma:
    def __init__(self, nome: str, danno_minimo: int, danno_massimo: int, tipo: str):
        self.nome = nome

        if danno_minimo >= 1:
            self.danno_minimo = danno_minimo
        else:
            print(" Attenzione: il danno minimo deve essere almeno 1. Impostato a 1.")
            self.danno_minimo = 1

        if danno_massimo >= self.danno_minimo:
            self.danno_massimo = danno_massimo
        else:
            print(" Attenzione: il danno massimo deve essere maggiore o uguale al danno minimo. Impostato a minimo + 1.")
            self.danno_massimo = self.danno_minimo + 1

        if tipo in ["mischia", "distanza"]:
            self.tipo = tipo
        else:
            raise ValueError(" ERRORE: il tipo deve essere 'mischia' o 'distanza'.")

    def get_danno(self) -> int:
        return random.randint(self.danno_minimo, self.danno_massimo)

    def __str__(self):
        return f"{self.nome} ({self.danno_minimo}–{self.danno_massimo} danni, tipo: {self.tipo})"

