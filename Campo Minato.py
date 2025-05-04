import random  

# Tutte le 8 direzioni intorno a una cella (riga, colonna)
direzioni = [(-1, -1), (-1, 0), (-1, 1),
             ( 0, -1),          ( 0, 1),
             ( 1, -1), ( 1, 0), ( 1, 1)]

def genera_griglia(dimensione, numero_mine):
    griglia = []  

    for _ in range(dimensione):  # Crea le righe
        riga = []
        for _ in range(dimensione):  # Crea le colonne per ogni riga
            riga.append(0)  
        griglia.append(riga)  

    posiziona_mine(griglia, numero_mine)  # Posiziona le mine nella griglia
    calcola_numeri(griglia)  # Calcola i numeri adiacenti alle mine

    return griglia  

def posiziona_mine(griglia, numero_mine):
    dimensione = len(griglia)  
    mine_posizionate = 0  

    while mine_posizionate < numero_mine:  
        riga = random.randint(0, dimensione - 1)  # Sceglie una riga casuale
        colonna = random.randint(0, dimensione - 1)  # Sceglie una colonna casuale

        if griglia[riga][colonna] != 'M':  # Controlla che non ci sia già una mina
            griglia[riga][colonna] = 'M'  # Posiziona la mina
            mine_posizionate += 1  

def calcola_numeri(griglia):
    dimensione = len(griglia)  

    for r in range(dimensione):  
        for c in range(dimensione):  
            if griglia[r][c] == 'M':  # Salta se la cella è una mina
                continue

            conteggio = 0  # Inizializza il contatore delle mine adiacenti

            for dr, dc in direzioni:  # Usa le direzioni definite sopra
                nr = r + dr  # Calcola la riga vicina
                nc = c + dc  # Calcola la colonna vicina

                if 0 <= nr < dimensione and 0 <= nc < dimensione:  # Controlla che sia nei limiti
                    if griglia[nr][nc] == 'M': 
                        conteggio += 1 

            griglia[r][c] = conteggio  # Assegna il numero di mine adiacenti alla cella

def rivela_cella(griglia, riga, colonna, celle_rivelate):
    if (riga, colonna) in celle_rivelate:  # Se la cella è già stata rivelata
        return False  

    celle_rivelate.add((riga, colonna))  # Aggiunge la cella all'insieme di quelle rivelate

    if griglia[riga][colonna] == 'M': 
        return True  # Game over

    if griglia[riga][colonna] == 0:  # Se è una cella vuota (0)
        for dr, dc in direzioni:  # Usa le direzioni definite sopra
            nr = riga + dr  # Calcola la riga vicina
            nc = colonna + dc  # Calcola la colonna vicina

            if 0 <= nr < len(griglia) and 0 <= nc < len(griglia):  # Controlla i limiti
                rivela_cella(griglia, nr, nc, celle_rivelate)  # Rivelazione ricorsiva

    return False  # Nessuna mina colpita

def visualizza_griglia(griglia, celle_rivelate):
    dimensione = len(griglia)

    print(" ", end="")  # Intestazione colonne
    for c in range(dimensione):
        print(f"{c:2}", end=" ")
    print()

    for r in range(dimensione):
        print(f"{r:2} ", end="")  # Intestazione riga
        for c in range(dimensione):
            if (r, c) in celle_rivelate:  # Se la cella è stata rivelata
                valore = griglia[r][c]
                if valore == 0:
                    print(" .", end=" ")  # Cella vuota
                elif valore == 'M':
                    print(" *", end=" ")  # Mina
                else:
                    print(f" {valore}", end=" ")  # Numero
            else:
                print(" #", end=" ")  # Cella nascosta
        print()  # Fine riga

def gioco_finito(griglia, celle_rivelate):
    dimensione = len(griglia)

    for r in range(dimensione):
        for c in range(dimensione):
            if griglia[r][c] != 'M' and (r, c) not in celle_rivelate:  
                return False  # Il gioco non è ancora finito

    return True  

def main():
    dimensione = int(input("Inserisci la dimensione della griglia (N): "))  
    totale_celle = dimensione * dimensione  # Calcola numero totale di celle
    numero_mine = int(totale_celle * 0.15) 

    griglia = genera_griglia(dimensione, numero_mine)  # Genera la griglia con mine
    celle_rivelate = set()  # Insieme delle celle già rivelate

    while True:
        visualizza_griglia(griglia, celle_rivelate)  # Mostra lo stato della griglia

        try:
            riga = int(input("Inserisci il numero della riga: ")) 
            colonna = int(input("Inserisci il numero della colonna: ")) 
        except ValueError:
            print("Input non valido. Inserisci numeri interi.")
            continue

        if not (0 <= riga < dimensione and 0 <= colonna < dimensione):  # Controllo limiti
            print("Coordinate fuori dalla griglia.")
            continue

        mina_colpita = rivela_cella(griglia, riga, colonna, celle_rivelate)  # Rivelazione della cella

        if mina_colpita:  # Se l'utente ha colpito una mina
            visualizza_griglia(griglia, {(r, c) for r in range(dimensione) for c in range(dimensione)})  # Mostra tutta la griglia
            print("Hai colpito una mina! Game Over.")  
            break

        if gioco_finito(griglia, celle_rivelate): 
            visualizza_griglia(griglia, celle_rivelate) 
            print("Complimenti! Hai vinto!")  
            break

if __name__ == "__main__":
    main()
