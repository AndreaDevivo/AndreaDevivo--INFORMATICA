import random


def crea_tabellone():
    tabellone = []

    for _ in range(3):
        riga = []
        for _ in range(3):
            riga.append(' ')
        tabellone.append(riga)

    return tabellone


def stampa_tabellone(tabellone):
    print("\n")

    for riga in tabellone:
        print("|".join(riga))
        print("-" * 5)


def controlla_vittoria(tabellone, simbolo):
    # Controllo righe
    for i in range(3):
        vinta = True

        for j in range(3):
            if tabellone[i][j] != simbolo:
                vinta = False
                break

        if vinta:
            return True

    # Controllo colonne
    for i in range(3):
        vinta = True

        for j in range(3):
            if tabellone[j][i] != simbolo:
                vinta = False
                break

        if vinta:
            return True

    # Diagonale principale
    if (
        tabellone[0][0] == simbolo and
        tabellone[1][1] == simbolo and
        tabellone[2][2] == simbolo
    ):
        return True

    # Diagonale secondaria
    if (
        tabellone[0][2] == simbolo and
        tabellone[1][1] == simbolo and
        tabellone[2][0] == simbolo
    ):
        return True

    return False


def controlla_pareggio(tabellone):
    for riga in tabellone:
        if ' ' in riga:
            return False

    return True


def mosse_possibili(tabellone):
    mosse = []

    for i in range(3):
        for j in range(3):
            if tabellone[i][j] == ' ':
                mosse.append((i, j))

    return mosse


def esegui_turno_bot(tabellone, bot):
    mosse = mosse_possibili(tabellone)

    for mossa in mosse:
        i, j = mossa

        copia = []
        for riga in tabellone:
            copia.append(riga[:])

        copia[i][j] = bot['simbolo']

        if controlla_vittoria(copia, bot['simbolo']):
            tabellone[i][j] = bot['simbolo']
            print(f"{bot['nome']} ha scelto la mossa: riga {i + 1}, colonna {j + 1}")
            return

    mossa = random.choice(mosse)
    i, j = mossa
    tabellone[i][j] = bot['simbolo']

    print(f"{bot['nome']} ha scelto la mossa: riga {i + 1}, colonna {j + 1}")


def esegui_turno(tabellone, giocatore):
    if giocatore.get('tipo') == 'bot':
        esegui_turno_bot(tabellone, giocatore)
        return

    while True:
        riga_input = input(f"{giocatore['nome']}, scegli la riga (1-3): ")
        colonna_input = input(f"{giocatore['nome']}, scegli la colonna (1-3): ")

        if riga_input.isdigit() and colonna_input.isdigit():
            riga = int(riga_input) - 1
            colonna = int(colonna_input) - 1

            if (
                0 <= riga < 3 and
                0 <= colonna < 3 and
                tabellone[riga][colonna] == ' '
            ):
                tabellone[riga][colonna] = giocatore['simbolo']
                break
            else:
                print("Posizione non valida o già occupata. Riprova.")
        else:
            print("Input non valido. Inserisci numeri tra 1 e 3.")


def gioco_tic_tac_toe():
    nome_giocatore = input("Inserisci il tuo nome: ")

    giocatore1 = {
        'nome': nome_giocatore,
        'simbolo': 'X',
        'vittorie': 0
    }

    giocatore2 = {
        'nome': 'Bot',
        'simbolo': 'O',
        'vittorie': 0,
        'tipo': 'bot'
    }

    giocatori = [giocatore1, giocatore2]

    partita_completata = False

    while not partita_completata:
        tabellone = crea_tabellone()
        turno = 0

        while True:
            stampa_tabellone(tabellone)

            giocatore_corrente = giocatori[turno % 2]

            esegui_turno(tabellone, giocatore_corrente)

            if controlla_vittoria(tabellone, giocatore_corrente['simbolo']):
                stampa_tabellone(tabellone)
                print(f"\n{giocatore_corrente['nome']} ha vinto!")
                giocatore_corrente['vittorie'] += 1
                break

            if controlla_pareggio(tabellone):
                stampa_tabellone(tabellone)
                print("\nLa partita è finita in pareggio!")
                break

            turno += 1

        print(
            f"\nPunteggio: {giocatore1['nome']} ({giocatore1['vittorie']})"
            f" - {giocatore2['nome']} ({giocatore2['vittorie']})"
        )

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
