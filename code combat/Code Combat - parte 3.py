import random


nomi = [
    "Drakar", "Lirael", "Thalas", "Eldorin", "Lyndra", "Kaelith", "Sylas", 
    "Faelan", "Mirabelle", "Zephyr", "Isolde", "Thorn", "Elysia", "Varian", 
    "Aeris", "Nerys", "Gwynn", "Eldira", "Soren", "Lirion"
]

cognomi = [
    "Stoneforge", "Moonshadow", "Starwhisper", "Thunderbeard", "Fireheart", 
    "Ravenwing", "Icebane", "Stormrider", "Swiftfoot", "Dragonflame", 
    "Shadowcloak", "Ironhammer", "Frostbeard", "Silverleaf", "Goldenshield", 
    "Windrider", "Hawkseye", "Deepstone", "Steelheart", "Oakenshield"
]


def genera_nome():
    nome = random.choice(nomi)
    cognome = random.choice(cognomi)
    return f"{nome} {cognome}"

def lancia_dadi(num_dadi, facce_dadi, scarta_basso=1, scarta_alto=1):
    dadi = [random.randint(1, facce_dadi) for _ in range(num_dadi)]
    dadi.sort()
    return dadi[scarta_basso: -scarta_alto]

def calcola_danno(dadi, scudo):
    danno = sum(dadi) - scudo
    return max(danno, 0)

def gioca():
    nome_giocatore1 = genera_nome()
    nome_giocatore2 = genera_nome()

    salute_giocatore1 = 98
    salute_giocatore2 = 82
    scudo_giocatore1 = 6
    scudo_giocatore2 = 9
    
    print(f"{nome_giocatore1} salute iniziale: {salute_giocatore1}")
    print(f"{nome_giocatore1} scudo: {scudo_giocatore1}")
    print(f"{nome_giocatore2} salute iniziale: {salute_giocatore2}")
    print(f"{nome_giocatore2} scudo: {scudo_giocatore2}")
    
    turni = 0
    while salute_giocatore1 > 0 and salute_giocatore2 > 0:
        turni += 1
        
        dadi_giocatore1 = lancia_dadi(6, 6)
        print(f"[{nome_giocatore1}] dadi: {dadi_giocatore1}")
        
        if dadi_giocatore1:
            danno1 = calcola_danno(dadi_giocatore1, scudo_giocatore1)
            if danno1 > 0:
                print(f"[{nome_giocatore1}] Danno: {danno1} (totale: {sum(dadi_giocatore1)} - scudo: {scudo_giocatore1})")
                salute_giocatore2 -= danno1
                print(f"[{nome_giocatore2}] Salute: {salute_giocatore2}")
            else:
                print(f"[{nome_giocatore1}] Danno: {danno1} (totale: {sum(dadi_giocatore1)} - scudo: {scudo_giocatore1}). L'attacco è stato evitato.")
        
        dadi_giocatore2 = lancia_dadi(4, 12)
        print(f"[{nome_giocatore2}] dadi: {dadi_giocatore2}")
        
        if dadi_giocatore2:
            danno2 = calcola_danno(dadi_giocatore2, scudo_giocatore2)
            if danno2 > 0:
                print(f"[{nome_giocatore2}] Danno: {danno2} (totale: {sum(dadi_giocatore2)} - scudo: {scudo_giocatore2})")
                salute_giocatore1 -= danno2
                print(f"[{nome_giocatore1}] Salute: {salute_giocatore1}")
            else:
                print(f"[{nome_giocatore2}] Danno: {danno2} (totale: {sum(dadi_giocatore2)} - scudo: {scudo_giocatore2}). L'attacco è stato evitato.")
        
        print()
    
    print(f"Turni giocati: {turni}")
    if salute_giocatore1 > salute_giocatore2:
        print(f"{nome_giocatore1} VINCE!")
    else:
        print(f"{nome_giocatore2} VINCE!")

gioca()
