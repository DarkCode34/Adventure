from Enemy import *
from Player import *

ork = Gegner(20, 20, 20)

print(f"Der Gegner Ork hat einen Angriff von {ork.angriff}")


while True:
    print(f'''***********************************************************
    HERZLICH WILLKOMMEN BEI MEINEN ERSTEN INTERAKTIVEN DUNGEON-CRAWLER!!!
    Ich hoffe dass er euch gefällt!
    ***********************************************************''')
    break

Spielername = (str(input("Bitte gebe nun deinen Namen ein: ")))
User = Player(Spielername, 50, 50, 50)
print(f"Du heißt {User.name} und hast einen Lebenswert von {User.leben}")

ork.angreifen(User)
print(f"Der Spieler hat nurnoch {User.leben} nach dem Angriff des Orks.")
#print(f"Der Spieler heißt {Player.name} und hat einen Angrifff von {Player.angriff} und eine Verteidung von {Player.verteidigung}")



