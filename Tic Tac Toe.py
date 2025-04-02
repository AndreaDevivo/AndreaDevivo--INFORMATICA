def crea_tabellone():
    return [[' ' for _ in range(3)] for _ in range(3)]


def stampa_tabellone(tabellone):
    print("\n")
    for riga in tabellone:
        print("|".join(riga))
        print("-" * 5)


def controlla_vittoria(tabellone, simbolo):
    for i in range(3):
        vinta = True
        for j in range(3):
            if tabellone[i][j] != simbolo:
                vinta = False
                break
        if vinta:
            return True

    for i in range(3):
        vinta = True
        for j in range(3):
            if tabellone[j][i] != simbolo:
                vinta = False
                break
        if vinta:
            return True

    if tabellone[0][0] == simbolo and tabellone[1][1] == simbolo and tabellone[2][2] == simbolo:
        return True
    if tabellone[0][2] == simbolo and tabellone[1][1] == simbolo and tabellone[2][0] == simbolo:
        return True

    return False


def controlla_pareggio(tabellone):
    for riga in tabellone:
        if ' ' in riga:
            return False
    return True


def esegui_turno(tabellone, giocatore):
    while True:

        riga_input = input(f"{giocatore['nome']}, scegli la riga (1-3): ")
        colonna_input = input(f"{giocatore['nome']}, scegli la colonna (1-3): ")

        if riga_input.isdigit() and colonna_input.isdigit():
            riga = int(riga_input) - 1 
            colonna = int(colonna_input) - 1  
            if 0 <= riga < 3 and 0 <= colonna < 3 and tabellone[riga][colonna] == ' ':
                tabellone[riga][colonna] = giocatore['simbolo']
                break
            else:
                print("Posizione non valida o già occupata. Riprova.")
        else:
            print("Input non valido. Assicurati di inserire numeri compresi tra 1 e 3.")


def gioco_tic_tac_toe():
    giocatore1 = {'nome': input("Nome del primo giocatore: "), 'simbolo': 'X', 'vittorie': 0}
    giocatore2 = {'nome': input("Nome del secondo giocatore: "), 'simbolo': 'O', 'vittorie': 0}
    giocatori = [giocatore1, giocatore2]

    partita_completata = False
    while not partita_completata:
        tabellone = crea_tabellone()
        turno = 0
        while True:
            stampa_tabellone(tabellone)
            esegui_turno(tabellone, giocatori[turno % 2])

            if controlla_vittoria(tabellone, giocatori[turno % 2]['simbolo']):
                print(f"\n{giocatori[turno % 2]['nome']} ha vinto!")
                giocatori[turno % 2]['vittorie'] += 1
                break

            if controlla_pareggio(tabellone):
                print("\nLa partita è finita in pareggio!")
                break

            turno += 1

        print(
            f"\nPunteggio: {giocatore1['nome']} ({giocatore1['vittorie']}) - {giocatore2['nome']} ({giocatore2['vittorie']})")

        if giocatore1['vittorie'] == 2:
            print(f"\n{giocatore1['nome']} ha vinto la sfida!")
            partita_completata = True
        elif giocatore2['vittorie'] == 2:
            print(f"\n{giocatore2['nome']} ha vinto la sfida!")
            partita_completata = True

        if not partita_completata:
            ripeti = input("Vuoi continuare? (sì/no): ").lower()
            if ripeti != 'sì':
                partita_completata = True
                print("Grazie per aver giocato!")


gioco_tic_tac_toe()
