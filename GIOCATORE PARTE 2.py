from arma import Arma

class Giocatore:
    def __init__(self, nome: str, salute_massima: int, forza: int, destrezza: int):
        self.__set_nome(nome)
        self.__set_salute_massima(salute_massima)
        self.__salute = self.__salute_massima
        self.__set_forza(forza)
        self.__set_destrezza(destrezza)
        self.__arma: Arma | None = None

    def get_nome(self) -> str:
        return self.__nome

    def get_salute_massima(self) -> int:
        return self.__salute_massima

    def get_salute(self) -> int:
        return self.__salute

    def get_forza(self) -> int:
        return self.__forza

    def get_destrezza(self) -> int:
        return self.__destrezza

    def get_arma(self) -> Arma | None:
        return self.__arma

    def __set_nome(self, nome: str):
        self.__nome = nome

    def __set_salute_massima(self, salute_massima: int):
        self.__salute_massima = max(1, salute_massima)

    def __set_forza(self, forza: int):
        self.__forza = max(1, min(20, forza))

    def __set_destrezza(self, destrezza: int):
        self.__destrezza = max(1, min(20, destrezza))

    def equipaggia(self, arma: Arma):
        self.__arma = arma

    def modificatore(self, valore: int) -> int:
        return (valore - 10) // 2

    def è_vivo(self) -> bool:
        return self.__salute > 0

    def subisce(self, danno: int) -> int:
        danno_effettivo = max(0, danno)
        self.__salute = max(0, self.__salute - danno_effettivo)
        return danno_effettivo

    def attacca(self, nemico: "Giocatore") -> int:
        if self.__arma is None:
            danno_base = 1
            modificatore = self.modificatore(self.__forza)
        else:
            danno_base = self.__arma.get_danno()
            if self.__arma.get_tipo() == "mischia":
                modificatore = self.modificatore(self.__forza)
            else:
                modificatore = self.modificatore(self.__destrezza)
        danno_totale = max(0, danno_base + modificatore)
        return nemico.subisce(danno_totale)

    def __str__(self):
        return f"{self.__nome} (HP: {self.__salute}/{self.__salute_massima})"
