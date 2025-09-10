from Enemy import *
from Player import *
from Battle import *
from Map import *


while True:
    print(f'''***********************************************************
    HERZLICH WILLKOMMEN BEI MEINEN ERSTEN INTERAKTIVEN DUNGEON-CRAWLER!!!
    Ich hoffe dass er euch gefällt!
    ***********************************************************''')
    break

Spielername = (str(input("Bitte gebe nun deinen Namen ein: ")))

ork = Gegner(200, 50, 20, 'Ork')
User = Player(Spielername, 100, 10, 20)
Spielfeld = Map(10, "User", "ork", "_", "#", "I")

Spielfeld.zeigeKarte(Spielfeld)

Kampf = Battle()

Kampf.Encounter(True, User, ork)


