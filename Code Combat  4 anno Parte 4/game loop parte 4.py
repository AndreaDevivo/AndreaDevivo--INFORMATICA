from weapon import Weapon
from player import Player
from potion import Potion

print("=== CREAZIONE PERSONAGGI ===\n")

# Gimli
try:
    print("Tentativo: Creare Spada Rotta (10-5 dmg)...  ")
    spada_rotta = Weapon("Spada Rotta", 10, 5, "melee")
    arma_gimli = spada_rotta
except ValueError as e:
    print(f"Creazione arma fallita: {e}")
    arma_gimli = None
    print("Gimli userà l'attacco a mani nude.\n")

print("... (Creazione Legolas riuscita) ...\n")

gimli = Player("Gimli", 50, 18, 7, arma_gimli)
legolas = Player("Legolas", 45, 12, 18, Weapon("Arco Elfico", 4, 8, "ranged"))

poz_cura = Potion("Pozione di Cura Minore", "heal", 15)
poz_forza = Potion("Pozione di Forza", "buff_str", 5, 3)

gimli._Player__potions = [poz_cura]
legolas._Player__potions = [poz_forza]

print("=== INIZIO COMBATTIMENTO ===  ")
print(gimli)
print(legolas)

# --- TURNO 1 ---
print("\n--- Turno 1 ---")
try:
    print(f"{gimli.name} (HP {gimli.health}/{gimli.max_health}) decide di usare '{poz_cura.name}'")
    effetto = poz_cura.apply_to(gimli)
    print(f"{gimli.name} usa la pozione: {effetto}")
except ValueError as e:
    print(f"Azione fallita: {e}")

tipo, dmg = gimli.attack(legolas)
print(f"{gimli.name} attacca {legolas.name} [{tipo}, STR eff={gimli.effective_strength()}]: infligge {dmg} danni!")
print(f"{legolas.name} (HP: {legolas.health}/{legolas.max_health})")

# --- TURNO 2 ---
print("\n--- Turno 2 ---")
try:
    print(f"{legolas.name} (HP {legolas.health}/{legolas.max_health}) decide di usare '{poz_forza.name}'")
    effetto = poz_forza.apply_to(legolas)
    print(f"{legolas.name} usa la pozione: {effetto}")
except ValueError as e:
    print(f"Azione fallita: {e}")

tipo, dmg = legolas.attack(gimli)
print(f"{legolas.name} attacca {gimli.name} [{tipo}, DEX eff={legolas.effective_dexterity()}]: infligge {dmg} danni!")
print(f"{gimli.name} (HP: {gimli.health}/{gimli.max_health})")

# --- TURNO 3 ---
print("\n--- Turno 3 ---")
try:
    print(f"{gimli.name} (HP {gimli.health}/{gimli.max_health}) decide di usare 'Pozione di Cura Minore'")
    effetto = poz_cura.apply_to(gimli)
    print(f"{gimli.name} usa la pozione: {effetto} -> {gimli.name} (HP: {gimli.health}/{gimli.max_health})")
except ValueError as e:
    print(f"Azione fallita: {e}")
