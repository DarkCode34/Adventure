from Battle import *
from Enemy import *
from Map import *
from Player import *
from GUI import *

class logic:
    def __init__(self):
        return

    Kampf = Battle()
    Menue = GUI()
    Menue.Startscreen()
    Spielername = Menue.spielernameAbfrage()

    Spielfeld = Map(30, " P", " G", " _", " W", " I")
    ork = Gegner(200, 50, 20, 'Ork')

    User = Player(Spielername, 100, 10, 20, 2, 4)

    Menue.Abstandshalter()

    while True: #todo muss noch gemacht werden

        Spielfeld.setPlayer(User.positionX,User.positionY)
        Spielfeld.zeigeKarte()
        entscheidung_User = Menue.hauptmenue()
        if entscheidung_User == '1':
            Spielfeld.movePlayerUp(User)
        elif entscheidung_User == '2':
            Spielfeld.movePlayerDown(User)
        elif entscheidung_User == '3':
            Spielfeld.movePlayerRight(User)
        elif entscheidung_User == '4':
            Spielfeld.movePlayerLeft(User)
        else:
            Menue.fehlerhafteEingabe()

        Menue.bildschirmLöschen()


        #Kampf.Encounter(True, User, ork)
