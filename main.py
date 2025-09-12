import os

from Battle import *
from Enemy import *
from Map import *
from Player import *
from GUI import *

print(f'''***********************************************************
HERZLICH WILLKOMMEN BEI MEINEN ERSTEN INTERAKTIVEN DUNGEON-CRAWLER!!!
Ich hoffe dass er euch gefällt!
***********************************************************''')

Spielername = (str(input("Bitte gebe nun deinen Namen ein: ")))
ork = Gegner(200, 50, 20, 'Ork')
Kampf = Battle()
Menue = GUI()
User = Player(Spielername, 100, 10, 20, 2, 4)
Spielfeld = Map(30, " P", " G", " _", " W", " I")
Menue.Abstandshalter()

while 1 == 1:

    Spielfeld.setPlayer(User.positionX,User.positionY)
    Spielfeld.zeigeKarte()
    Menue.hauptmenue()
    Spielfeld.movePlayer(User)
    os.system('cls')  # Windows
#   break


Kampf.Encounter(True, User, ork)


