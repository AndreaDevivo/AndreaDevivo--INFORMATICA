import random

# Liste dei nomi e dei cognomi per i personaggi
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

# Funzione per generare un nome completo combinando nome e cognome
def genera_nome():
    nome = random.choice(nomi)  # Selezione casuale del nome
    cognome = random.choice(cognomi)  # Selezione casuale del cognome
    return f"{nome} {cognome}"  # Restituisce il nome completo

# Funzione per lanciare i dadi e applicare la selezione dei risultati
def lancia_dadi(num_dadi, facce_dadi, scarta_basso=1, scarta_alto=1):
    dadi = [random.randint(1, facce_dadi) for _ in range(num_dadi)]  # Lancio dei dadi
    dadi.sort()  # Ordinamento dei risultati
    # Rimuove i dadi più bassi e più alti
    return dadi[scarta_basso: -scarta_alto]  # Restituisce i dadi rimanenti dopo averli scartati

# Funzione per calcolare il danno e aggiornare la salute
def calcola_danno(dadi, scudo):
    danno = sum(dadi) - scudo  # Calcola il danno sottraendo lo scudo
    return max(danno, 0)  # Se il danno è negativo, restituisce 0 (attacco evitato)

# Funzione principale per gestire il gioco
def gioca():
    # Generazione dei personaggi
    nome_giocatore1 = genera_nome()
    nome_giocatore2 = genera_nome()

    # Valori di salute e scudo iniziali
    salute_giocatore1 = 98
    salute_giocatore2 = 82
    scudo_giocatore1 = 6
    scudo_giocatore2 = 9
    
    # Stampa dei dettagli iniziali
    print(f"{nome_giocatore1} salute iniziale: {salute_giocatore1}")
    print(f"{nome_giocatore1} scudo: {scudo_giocatore1}")
    print(f"{nome_giocatore2} salute iniziale: {salute_giocatore2}")
    print(f"{nome_giocatore2} scudo: {scudo_giocatore2}")
    
    turni = 0  # Contatore dei turni
    while salute_giocatore1 > 0 and salute_giocatore2 > 0:
        turni += 1  # Incrementa il numero di turni
        
        # Giocatore 1 lancia 6 dadi da 6 facce (dl1dh1)
        dadi_giocatore1 = lancia_dadi(6, 6)
        print(f"[{nome_giocatore1}] dadi: {dadi_giocatore1}")
        
        if dadi_giocatore1:
            # Calcola il danno per il Giocatore 1
            danno1 = calcola_danno(dadi_giocatore1, scudo_giocatore1)
            if danno1 > 0:
                print(f"[{nome_giocatore1}] Danno: {danno1} (totale: {sum(dadi_giocatore1)} - scudo: {scudo_giocatore1})")
                salute_giocatore2 -= danno1  # Riduce la salute del Giocatore 2
                print(f"[{nome_giocatore2}] Salute: {salute_giocatore2}")
            else:
                print(f"[{nome_giocatore1}] Danno: {danno1} (totale: {sum(dadi_giocatore1)} - scudo: {scudo_giocatore1}). L'attacco è stato evitato.")
        
        # Giocatore 2 lancia 4 dadi da 12 facce (dl1dh1)
        dadi_giocatore2 = lancia_dadi(4, 12)
        print(f"[{nome_giocatore2}] dadi: {dadi_giocatore2}")
        
        if dadi_giocatore2:
            # Calcola il danno per il Giocatore 2
            danno2 = calcola_danno(dadi_giocatore2, scudo_giocatore2)
            if danno2 > 0:
                print(f"[{nome_giocatore2}] Danno: {danno2} (totale: {sum(dadi_giocatore2)} - scudo: {scudo_giocatore2})")
                salute_giocatore1 -= danno2  # Riduce la salute del Giocatore 1
                print(f"[{nome_giocatore1}] Salute: {salute_giocatore1}")
            else:
                print(f"[{nome_giocatore2}] Danno: {danno2} (totale: {sum(dadi_giocatore2)} - scudo: {scudo_giocatore2}). L'attacco è stato evitato.")
        
        print()  # Separatore per una migliore leggibilità
    
    # Risultato finale
    print(f"Turni giocati: {turni}")
    if salute_giocatore1 > salute_giocatore2:
        print(f"{nome_giocatore1} VINCE!")  # Giocatore 1 vince
    else:
        print(f"{nome_giocatore2} VINCE!")  # Giocatore 2 vince

# Eseguiamo il gioco
gioca()

