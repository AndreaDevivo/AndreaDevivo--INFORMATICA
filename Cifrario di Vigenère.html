def genera_tabula_recta():
    tabula_recta = []
    for i in range(26):
        riga = [chr((j % 26) + 65) for j in range(i, i + 26)]
        tabula_recta.append(riga)
    return tabula_recta

def cifra(messaggio, chiave, tabula_recta):
    testo_cifrato = ""
    for i, lettera in enumerate(messaggio):
        riga = ord(chiave[i]) - 65
        colonna = ord(lettera) - 65
        testo_cifrato += tabula_recta[riga][colonna]
    return testo_cifrato

def decifra(messaggio_cifrato, chiave, tabula_recta):
    testo_decifrato = ""
    for i, lettera in enumerate(messaggio_cifrato):
        riga = ord(chiave[i]) - 65
        colonna = tabula_recta[riga].index(lettera)
        testo_decifrato += chr(colonna + 65)
    return testo_decifrato

def normalizza_testo(testo):
    return "".join([c.upper() for c in testo if c.isalpha()])

def estendi_chiave(chiave, lunghezza):
    return (chiave * (lunghezza // len(chiave) + 1))[:lunghezza]

def main():
    print("Cifrario di Vigenère")
    tabula_recta = genera_tabula_recta()
    scelta = input("Vuoi cifrare (C) o decifrare (D)? ").strip().upper()
    
    if scelta == "C":
        messaggio = normalizza_testo(input("Inserisci il messaggio da cifrare: "))
        chiave = normalizza_testo(input("Inserisci la chiave: "))
        chiave_estesa = estendi_chiave(chiave, len(messaggio))
        print(f"Testo cifrato: {cifra(messaggio, chiave_estesa, tabula_recta)}")
    elif scelta == "D":
        messaggio_cifrato = normalizza_testo(input("Inserisci il messaggio cifrato: "))
        chiave = normalizza_testo(input("Inserisci la chiave: "))
        chiave_estesa = estendi_chiave(chiave, len(messaggio_cifrato))
        print(f"Testo decifrato: {decifra(messaggio_cifrato, chiave_estesa, tabula_recta)}")
    else:
        print("Scelta non valida.")

if __name__ == "__main__":
    main()
