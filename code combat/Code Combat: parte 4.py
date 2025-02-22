import random

CLASSI = {
    "Guerriero": {"vita": (100, 120), "energia": (8, 10), "difesa": (4, 8), "attacco": (2, 6), "abilita": (1, 6)},
    "Mago": {"vita": (70, 90), "energia": (14, 18), "difesa": (3, 5), "attacco": (1, 20), "abilita": (1, 8)},
    "Ladro": {"vita": (80, 100), "energia": (10, 12), "difesa": (3, 5), "attacco": (3, 4), "abilita": (1, 4)},
    "Chierico": {"vita": (80, 100), "energia": (10, 12), "difesa": (4, 6), "attacco": (1, 12), "abilita": (1, 6)}
}

def crea_personaggio(tipo):
    attributi = CLASSI[tipo]
    return {
        "tipo": tipo,
        "vita": random.randint(*attributi["vita"]),
        "energia": random.randint(*attributi["energia"]),
        "difesa": random.randint(*attributi["difesa"]),
        "attacco": attributi["attacco"],
        "abilita": attributi["abilita"]
    }

def crea_squadra():
    return [crea_personaggio(tipo) for tipo in CLASSI]

def lancia_dadi(numero, facce):
    return sum(random.randint(1, facce) for _ in range(numero))

def scegli_bersaglio(attaccante, nemici):
    if attaccante["tipo"] == "Guerriero":
        return max(nemici, key=lambda p: p["vita"], default=None)
    elif attaccante["tipo"] == "Mago":
        return random.choice(nemici[len(nemici)//2-1:len(nemici)//2+1])
    elif attaccante["tipo"] == "Ladro":
        return min(nemici, key=lambda p: p["vita"], default=None)
    elif attaccante["tipo"] == "Chierico":
        return random.choice([nemici[0], nemici[-1]])
    return None

def attacca(attaccante, bersaglio):
    if attaccante["energia"] < 2:
        attaccante["energia"] = CLASSI[attaccante["tipo"]]["energia"][1] 
        return
    danno = max(0, lancia_dadi(*attaccante["attacco"]) - bersaglio["difesa"])
    bersaglio["vita"] -= danno
    attaccante["energia"] -= 2

def usa_abilita(personaggio, nemici, alleati):
    if lancia_dadi(1, personaggio["abilita"][1]) == personaggio["abilita"][1]:
        if personaggio["tipo"] == "Guerriero":
            if lancia_dadi(1, 6) >= 5:
                attacca(personaggio, scegli_bersaglio(personaggio, nemici))
        elif personaggio["tipo"] == "Mago":
            personaggio["attacco"] = (personaggio["attacco"][0] + 1, personaggio["attacco"][1])
        elif personaggio["tipo"] == "Ladro":
            if lancia_dadi(2, 4) >= 7:
                for nemico in nemici:
                    nemico["difesa"] = max(0, nemico["difesa"] - nemico["difesa"] // 4)
        elif personaggio["tipo"] == "Chierico":
            piu_debole = min(alleati, key=lambda p: p["vita"], default=None)
            if piu_debole:
                piu_debole["vita"] += lancia_dadi(2, 6)

def combattimento(squadra1, squadra2):
    while squadra1 and squadra2:
        for i in range(min(len(squadra1), len(squadra2))):
            attacca(squadra1[i], scegli_bersaglio(squadra1[i], squadra2))
            usa_abilita(squadra1[i], squadra2, squadra1)
            attacca(squadra2[i], scegli_bersaglio(squadra2[i], squadra1))
            usa_abilita(squadra2[i], squadra1, squadra2)
        squadra1 = [p for p in squadra1 if p["vita"] > 0]
        squadra2 = [p for p in squadra2 if p["vita"] > 0]
    return "Squadra 1 vince!" if squadra1 else "Squadra 2 vince!"

squadra1 = crea_squadra()
squadra2 = crea_squadra()
risultato = combattimento(squadra1, squadra2)
print(risultato)
