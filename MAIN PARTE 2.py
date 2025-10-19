import random
from giocatore import Giocatore
from arma import Arma

def crea_arma_per(giocatore: Giocatore) -> Arma:
    if giocatore.get_forza() >= giocatore.get_destrezza():
        return Arma("Spadone", 8, 15, "mischia")
    else:
        return Arma("Arco Lungo", 6, 12, "distanza")

def main():
    print("=== SIMULAZIONE COMBATTIMENTO ===\n")

    g1 = Giocatore("Gimli", 50, random.randint(1, 20), random.randint(1, 20))
    g2 = Giocatore("Legolas", 45, random.randint(1, 20), random.randint(1, 20))

    print(f"{g1.get_nome()}: Forza={g1.get_forza()}, Destrezza={g1.get_destrezza()}")
    print(f"{g2.get_nome()}: Forza={g2.get_forza()}, Destrezza={g2.get_destrezza()}\n")

    arma1 = crea_arma_per(g1)
    arma2 = crea_arma_per(g2)

    g1.equipaggia(arma1)
    g2.equipaggia(arma2)

    print(f"{g1.get_nome()} equipaggia: {arma1}")
    print(f"{g2.get_nome()} equipaggia: {arma2}\n")

    print("=== INIZIO COMBATTIMENTO ===\n")
    turno = 1

    while g1.è_vivo() and g2.è_vivo():
        print(f"--- Turno {turno} ---")

        danno1 = g1.attacca(g2)
        print(f"{g1.get_nome()} attacca {g2.get_nome()} e infligge {danno1} danni!")
        print(g2)

        if not g2.è_vivo():
            break

        danno2 = g2.attacca(g1)
        print(f"{g2.get_nome()} attacca {g1.get_nome()} e infligge {danno2} danni!")
        print(g1)

        print()
        turno += 1

    print("=== FINE COMBATTIMENTO ===\n")
    if g1.è_vivo() and not g2.è_vivo():
        print(f"🏆 {g1.get_nome()} ha vinto il combattimento!")
    elif g2.è_vivo() and not g1.è_vivo():
        print(f"🏆 {g2.get_nome()} ha vinto il combattimento!")
    else:
        print("🤝 Pareggio! Entrambi sono caduti.")

if __name__ == "__main__":
    main()
