import random


def genera_matrice(n):

    numeri = [] 

    while len(numeri) < n * n:
        num = random.randint(1, n * n) 
        if num not in numeri:
            numeri.append(num)

    
    matrice = [numeri[i:i + n] for i in range(0, len(numeri), n)]
    return matrice


def somma_riga(matrice, riga):
  
    return sum(matrice[riga])


def somma_colonna(matrice, colonna):
    
    return sum(matrice[i][colonna] for i in range(len(matrice)))


def somma_diagonale(matrice, diagonale):

    n = len(matrice)  
    if diagonale == 0: 
        return sum(matrice[i][i] for i in range(n))
    else: 
        return sum(matrice[i][n - 1 - i] for i in range(n))


def verifica_quadrato_magico(matrice):
   
    n = len(matrice)  
    costante_magica = somma_riga(matrice, 0)

   
    for i in range(n):
        if somma_riga(matrice, i) != costante_magica:
            return False, None

    
    for i in range(n):
        if somma_colonna(matrice, i) != costante_magica:
            return False, None

  
    if somma_diagonale(matrice, 0) != costante_magica or somma_diagonale(matrice, 1) != costante_magica:
        return False, None

   
    return True, costante_magica


def stampa_matrice(matrice, costante_magica=None):
    
    for riga in matrice:
        print(" ".join(str(x) for x in riga))  
    if costante_magica is not None:
        print(f"Costante di magia: {costante_magica}")


def main():
  
    for n in range(3, 11):
        while True:
            matrice = genera_matrice(n) 
            verifica, costante_magica = verifica_quadrato_magico(matrice) 
            if verifica:
                break 
        stampa_matrice(matrice, costante_magica)

# Avvio del programma
if __name__ == "__main__":
    main()
