import random


# Funzione per generare il valore di un dado
def lancia_dado(sides):
    return random.randint(1, sides)


# Funzione per generare le statistiche dei personaggi
def crea_personaggio(nome):
    if nome == "Guerriero":
        vita = random.randint(100, 120)
        energia = random.randint(8, 10)
        difesa = random.randint(4, 8)
        attacco = sum([lancia_dado(6) for _ in range(2)])  # 2d6
        abilita = "Berserk"
    elif nome == "Mago":
        vita = random.randint(70, 90)
        energia = random.randint(14, 18)
        difesa = random.randint(3, 5)
        attacco = lancia_dado(20)  # 1d20
        abilita = "Concentrazione assoluta"
    elif nome == "Ladro":
        vita = random.randint(80, 100)
        energia = random.randint(10, 12)
        difesa = random.randint(3, 5)
        attacco = sum([lancia_dado(4) for _ in range(3)])  # 3d4
        abilita = "Pugnali acidi"
    elif nome == "Chierico":
        vita = random.randint(80, 100)
        energia = random.randint(10, 12)
        difesa = random.randint(4, 6)
        attacco = lancia_dado(12)  # 1d12
        abilita = "Favore degli dei"

    return {
        "nome": nome,
        "vita": vita,
        "energia": energia,
        "difesa": difesa,
        "attacco": attacco,
        "abilita": abilita,
    }


# Funzione per eseguire l'abilità speciale
def abilita_speciale(personaggio):
    if personaggio["abilita"] == "Berserk":
        dado = lancia_dado(6)
        if dado >= 5:
            return "Attacco extra"
        elif dado >= 3:
            perdita_vita = max(1, personaggio["vita"] // 5)  # 20% della vita
            personaggio["vita"] -= perdita_vita
            return f"Attacco extra, perdita di vita: {perdita_vita}"
        else:
            perdita_vita = max(1, personaggio["vita"] // 5)  # 20% della vita
            personaggio["vita"] -= perdita_vita
            return f"Perdita di vita: {perdita_vita}"

    elif personaggio["abilita"] == "Concentrazione assoluta":
        dado = lancia_dado(6)
        if dado >= 5:
            incremento_attacco = lancia_dado(4)
            personaggio["attacco"] += incremento_attacco
            return f"Incremento attacco di {incremento_attacco}"

    elif personaggio["abilita"] == "Pugnali acidi":
        dado1 = lancia_dado(4)
        dado2 = lancia_dado(4)
        if dado1 + dado2 >= 7:
            return "Riduzione difesa nemici del 25%"

    elif personaggio["abilita"] == "Favore degli dei":
        cura = sum([lancia_dado(6) for _ in range(2)])  # 2d6
        return f"Cura per il compagno più debole: {cura}"


# Funzione per determinare l'attacco
def esegui_attacco(attaccante, difensore):
    if attaccante["energia"] >= 2:
        # Attacco
        attaccante["energia"] -= 2
        danno = max(attaccante["attacco"] - difensore["difesa"], 0)  # Calcola danno
        difensore["vita"] -= danno
        return f"{attaccante['nome']} attacca {difensore['nome']} causando {danno} danni."
    else:
        # Riposo per recuperare energia
        energia_ripristinata = min(2, difensore["energia"] - attaccante["energia"])
        attaccante["energia"] += energia_ripristinata
        return f"{attaccante['nome']} riposa e recupera energia."


# Funzione per eseguire il combattimento tra due squadre
def combattimento(party1, party2):
    turno = 0
    while party1 and party2:  # Finché entrambe le squadre sono vive
        attaccante, difensore = party1[turno % len(party1)], party2[turno % len(party2)]

        print(f"\nTurno {turno + 1}")
        print(f"{attaccante['nome']} attacca {difensore['nome']}")

        # Esegui l'attacco
        esito_attacco = esegui_attacco(attaccante, difensore)
        print(esito_attacco)

        # Esegui l'abilità speciale
        esito_abilita = abilita_speciale(attaccante)
        print(f"Abilità speciale attivata: {esito_abilita}")

        # Verifica la condizione di vittoria
        if difensore["vita"] <= 0:
            print(f"{difensore['nome']} è stato eliminato!")
            party2.remove(difensore)

        turno += 1

    # Verifica la vittoria
    if len(party1) == 0:
        print("La squadra 2 ha vinto!")
    elif len(party2) == 0:
        print("La squadra 1 ha vinto!")


# Crea un party con i 4 personaggi
party1 = [crea_personaggio("Guerriero"), crea_personaggio("Mago"), crea_personaggio("Ladro"),
          crea_personaggio("Chierico")]
party2 = [crea_personaggio("Guerriero"), crea_personaggio("Mago"), crea_personaggio("Ladro"),
          crea_personaggio("Chierico")]

# Avvia il combattimento
combattimento(party1, party2)
