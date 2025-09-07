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

ork = Gegner(20, 30, 20, 'Peter')
User = Player(Spielername, 50, 50, 50)

ork.angreifen(User)

Battle = Battle

Battle.Encounter("true", User)
