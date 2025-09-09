from Enemy import *
from Player import *
from Battle import *

while True:
    print(f'''***********************************************************
    HERZLICH WILLKOMMEN BEI MEINEN ERSTEN INTERAKTIVEN DUNGEON-CRAWLER!!!
    Ich hoffe dass er euch gefällt!
    ***********************************************************''')
    break

Spielername = (str(input("Bitte gebe nun deinen Namen ein: ")))

ork = Gegner(200, 50, 20, 'Ork')
User = Player(Spielername, 200, 50, 20)
Kampf = Battle()

Kampf.Encounter(True, User, ork)


