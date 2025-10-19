import random

class Arma:
    def __init__(self, nome: str, danno_minimo: int, danno_massimo: int, tipo: str):
        self.__set_nome(nome)
        self.__set_danno_minimo(danno_minimo)
        self.__set_danno_massimo(danno_massimo)
        self.__set_tipo(tipo)

    def get_nome(self) -> str:
        return self.__nome

    def get_danno_minimo(self) -> int:
        return self.__danno_minimo

    def get_danno_massimo(self) -> int:
        return self.__danno_massimo

    def get_tipo(self) -> str:
        return self.__tipo

    def __set_nome(self, nome: str):
        self.__nome = nome

    def __set_danno_minimo(self, danno_minimo: int):
        if danno_minimo >= 1:
            self.__danno_minimo = danno_minimo
        else:
            print("Attenzione: il danno minimo deve essere almeno 1. Impostato a 1.")
            self.__danno_minimo = 1

    def __set_danno_massimo(self, danno_massimo: int):
        if danno_massimo >= self.__danno_minimo:
            self.__danno_massimo = danno_massimo
        else:
            print("Attenzione: il danno massimo deve essere maggiore o uguale al danno minimo. Impostato a minimo + 1.")
            self.__danno_massimo = self.__danno_minimo + 1

    def __set_tipo(self, tipo: str):
        if tipo in ["mischia", "distanza"]:
            self.__tipo = tipo
        else:
            raise ValueError(" ERRORE: il tipo deve essere 'mischia' o 'distanza'.")

    def get_danno(self) -> int:
        return random.randint(self.__danno_minimo, self.__danno_massimo)

    def __str__(self):
        return f"{self.__nome} ({self.__danno_minimo}–{self.__danno_massimo} danni, tipo: {self.__tipo})"
