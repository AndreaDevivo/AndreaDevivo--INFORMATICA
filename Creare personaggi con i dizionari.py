import random

print('\n#1: CREAZIONE DEL PERSONAGGIO\n')
# 1. Crea un dizionario inserendo al suo interno:
# - Un nome scelto a caso dalla lista di nomi
# - Chiedi all'utente di inserire una classe per il proprio personaggio a scelta tra Guerriero, Mago, Chierico, Ladro
# Memorizza queste informazioni in un dizionario chiamato 'personaggio'.
nomi = ["Drakar", "Lirael", "Thalas", "Eldorin", "Lyndra", "Kaelith", "Sylas", "Faelan", "Mirabelle", "Zephyr",
        "Isolde", "Thorn", "Elysia", "Varian", "Aeris", "Nerys", "Gwynn", "Eldira", "Soren", "Lirion"]




nome_personaggio = random.choice(nomi)


classe = input("Inserisci la classe del tuo personaggio (Guerriero, Mago, Chierico, Ladro): ")


personaggio = {
    "nome": nome_personaggio,
    "classe": classe
}



print('\n#2: ATTRIBUTI DEL PERSONAGGIO\n')
# 2. Aggiungi al dizionario i seguenti attributi generati casualmente:
# - Punti vita tra 80 e 100
# - Armatura tra 5 e 10
# - Tipo di dado d'attacco (es. "1d6") scelto dall'utente




punti_vita = random.randint(80, 100)
armatura = random.randint(5, 10)


dado_attacco = input("Inserisci il tipo di dado per l'attacco (es. 1d6): ")


personaggio["punti_vita"] = punti_vita
personaggio["armatura"] = armatura
personaggio["dado_attacco"] = dado_attacco



print('\n#2.1: AGGIUNTA DELLO ZAINO\n')
# 2.1. Aggiungi al dizionario un nuovo attributo chiamato 'zaino' che sia a sua volta un dizionario contenente:
# - 'monete': valore casuale tra 20 e 50
# - 'oggetti': due oggetti casuali estratti dalla lista di oggetti
# - 'arma': un oggetto casuale estratto dalla lista delle armi


oggetti = ["Pozione curativa", "Rampino", "Attrezzi da scasso", "Razioni di cibo", "Corda"]
armi = {
    "fisico": ["Spada", "Pugnale", "Arco", "Balestra"],
    "magico": ["Bastone magico", "Bacchetta"]
}


monete = random.randint(20, 50)
oggetti_selezionati = random.choices(oggetti, k=2)


if personaggio["classe"] in ["Guerriero", "Ladro"]:
    arma = random.choice(armi["fisico"])
else:
    arma = random.choice(armi["magico"])


zaino = {
    "monete": monete,
    "oggetti": oggetti_selezionati,
    "arma": arma
}


personaggio["zaino"] = zaino



print('\n#3: STAMPA DEL PERSONAGGIO\n')
# 3. Stampa a video tutte le informazioni del personaggio, una per riga.




for chiave, valore in personaggio.items():
    print(f"{chiave}: {valore}")



print('\n#4: FUNZIONI - CREAZIONE PERSONAGGIO\n')


# 4. Trasforma il codice della creazione di un personaggio in una funzione chiamata 'crea_personaggio'.
# La funzione deve restituire un dizionario con i dati del personaggio.



def crea_personaggio():
    nome_personaggio = random.choice(nomi)


    classe = input("Inserisci la classe del tuo personaggio (Guerriero, Mago, Chierico, Ladro): ")

    personaggio = {
        "nome": nome_personaggio,
        "classe": classe
    }


    punti_vita = random.randint(80, 100)
    armatura = random.randint(5, 10)


    dado_attacco = input("Inserisci il tipo di dado per l'attacco (es. 1d6): ")


    personaggio["punti_vita"] = punti_vita
    personaggio["armatura"] = armatura
    personaggio["dado_attacco"] = dado_attacco

    # Genero le monete e gli oggetti
    monete = random.randint(20, 50)
    oggetti_selezionati = random.sample(oggetti, 2)


    if personaggio["classe"] in ["Guerriero", "Ladro"]:
        arma = random.choice(armi["fisico"])
    else:
        arma = random.choice(armi["magico"])


    zaino = {
        "monete": monete,
        "oggetti": oggetti_selezionati,
        "arma": arma
    }


    personaggio["zaino"] = zaino

    return personaggio




print('\n#5: FUNZIONI - CREAZIONE PARTY\n')


# 5. Trasforma il codice della creazione di un party in una funzione chiamata 'crea_party'.
# La funzione deve restituire una lista di personaggi (lista di dizionari).



def crea_party():
    party = []
    num_personaggi = int(input("Quanti personaggi vuoi creare per il tuo party? "))

    for _ in range(num_personaggi):
        party.append(crea_personaggio())

    return party




print('\n#6: FUNZIONI - STAMPA PARTY\n')


# 6. Trasforma il codice della stampa del party in una funzione chiamata 'stampa_party'.
# La funzione deve ricevere una lista di dizionari come parametro e stampare i dati di ogni personaggio.



def stampa_party(party):
    for personaggio in party:
        for chiave, valore in personaggio.items():
            print(f"{chiave}: {valore}")
        print("\n")



print('\nFUNZIONE PRINCIPALE\n')
def main():
    party = crea_party()
    stampa_party(party)


main()
