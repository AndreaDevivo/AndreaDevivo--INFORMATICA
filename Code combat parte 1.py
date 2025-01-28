import random 
print("La vita del personaggio è 30")

vita_personaggio = 30
turni = 0

while vita_personaggio > 0:
    dado = random.randint(1, 6)
    vita_personaggio -= dado  # Sottrai il danno dai punti vita
    turni += 1  # Incrementa il contatore dei turni
    
    print(f"Il danno inflitto al personaggio è {dado}")
    print(f"La vita del personaggio è {vita_personaggio}")

print("Il personaggio è morto")
print(f"sono stati giocati {turni} turni")
