import random

def lancia_dadi(num_dadi, facce):
    return sum(random.randint(1, facce) for _ in range(num_dadi))

salute_player1 = random.randint(80, 100)
scudo_player1 = random.randint(5, 10)
salute_player2 = random.randint(80, 100)
scudo_player2 = random.randint(5, 10)

dadi_player1 = (4, 6)
dadi_player2 = (2, 12)

turni = 0

while salute_player1 > 0 and salute_player2 > 0:
    turni += 1
    
    attacco_player1 = lancia_dadi(dadi_player1[0], dadi_player1[1])
    danno_a_player2 = max(attacco_player1 - scudo_player2, 0)  
    salute_player2 -= danno_a_player2
    
    print(f"Turno {turni}")
    print(f"[Player1] Danno: {danno_a_player2} ({attacco_player1}-{scudo_player2})")
    print(f"[Player2] Salute: {salute_player2}")
    print("\t---")
    
    attacco_player2 = lancia_dadi(dadi_player2[0], dadi_player2[1])
    danno_a_player1 = max(attacco_player2 - scudo_player1, 0)  
    salute_player1 -= danno_a_player1
    
    print(f"[Player2] Danno: {danno_a_player1} ({attacco_player2}-{scudo_player1})")
    print(f"[Player1] Salute: {salute_player1}")
    print("\n")

if salute_player1 > 0 and salute_player2 <= 0:
    print(f"Player1 vince in {turni} turni!")
elif salute_player2 > 0 and salute_player1 <= 0:
    print(f"Player2 vince in {turni} turni!")
else:
    print(f"Pareggio. Entrambi i giocatori sono stati sconfitti in {turni} turni.")
