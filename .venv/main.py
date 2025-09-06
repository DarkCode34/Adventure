from Enemy import Gegner
from Player import Player

ork = Gegner(20, 20, 20)

print(f"Der Gegner Ork hat einen Angriff von {ork.angriff}")


while True:
    print(f'''***********************************************************
    HERZLICH WILLKOMMEN BEI MEINEN ERSTEN INTERAKTIVEN DUNGEON-CRAWLER!!!
    Ich hoffe dass er euch gefällt!
    ***********************************************************''')
    break

Spielername = (str(input("Bitte gebe nun deinen Namen ein: ")))
Player = Player(Spielername, 50, 50, 50)

#print(f"Der Spieler heißt {Player.name} und hat einen Angrifff von {Player.angriff} und eine Verteidung von {Player.verteidigung}")
.


