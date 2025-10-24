from weapon import Weapon
from potion import Potion
from player import Player
import time


sword = Weapon("Spada", 5, 10, "melee")
bow = Weapon("Arco", 3, 8, "ranged")


heal_potion = Potion("Pozione Cura", "heal", 15)
buff_str_potion = Potion("Pozione Forza", "buff_str", 5, 3)
buff_dex_potion = Potion("Pozione Destrezza", "buff_dex", 5, 3)


player1 = Player("Arthur", 50, 12, 8, sword)
player2 = Player("Robin", 45, 9, 13, bow)


player1.potions = [heal_potion, buff_str_potion]
player2.potions = [buff_dex_potion]


turn = 1
print("\n=== INIZIO SIMULAZIONE ===\n")

while player1.is_alive() and player2.is_alive():
    print(f"\n--- Turno {turn} ---")

   
    for player, enemy in [(player1, player2), (player2, player1)]:
        potion = player.should_use_potion(enemy)
        if potion:
            result = player.use_potion(potion)
            print(f"{player.name} usa {potion.name}: {result}")

   
    dmg1 = player1.attack(player2)
    print(f"{player1.name} infligge {dmg1} danni a {player2.name} ({player2.health}/{player2.max_health} HP)")

    if not player2.is_alive():
        print(f"{player2.name} è stato sconfitto!")
        break

    dmg2 = player2.attack(player1)
    print(f"{player2.name} infligge {dmg2} danni a {player1.name} ({player1.health}/{player1.max_health} HP)")

    if not player1.is_alive():
        print(f"{player1.name} è stato sconfitto!")
        break

  
    player1.tick_buffs()
    player2.tick_buffs()

    turn += 1
    time.sleep(0.5)

print("\n=== FINE SIMULAZIONE ===")
if player1.is_alive():
    print(f"Vincitore: {player1.name}")
else:
    print(f"Vincitore: {player2.name}")
