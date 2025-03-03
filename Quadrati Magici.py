import random

def crea_griglia(dimensione: int, valori_possibili: list):
    griglia = []
    valori_disponibili = valori_possibili[:]
    
    for _ in range(dimensione):
        riga_corrente = []
        for _ in range(dimensione):
            valore = random.choice(valori_disponibili)
            riga_corrente.append(valore)
            valori_disponibili.remove(valore)
        griglia.append(riga_corrente)
    
    return griglia

def controlla_quadrato_magico(griglia):
    somme_righe = []
    somma_corrente = 0
    
    for riga in griglia:
        for elemento in riga:
            somma_corrente += elemento
        somme_righe.append(somma_corrente)
        somma_corrente = 0
    
    for i in range(len(somme_righe)):
        if somme_righe[i] != somme_righe[0]:
            return False
    
    return True

def mostra_griglia(griglia, somma_magica=None):
    for i in range(len(griglia)):
        for j in range(len(griglia[i])):
            print(griglia[i][j], end=" ")
        print("\n")

def main():
    valori_possibili = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    while True:
        griglia = crea_griglia(3, valori_possibili)
        verifica = controlla_quadrato_magico(griglia)
        
        if verifica:
            break
        else:
            continue
    
    return f"{griglia} è un quadrato perfetto"

if __name__ == "__main__":
    print(main())
