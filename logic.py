import os #todo kann noch später in die gui klasse eingebaut werden

from Battle import *
from Enemy import *
from Map import *
from Player import *
from GUI import *

class logic:
    def __init__(self):
        return

    def start(self):

        print(f'''
        
        ░░      ░░░       ░░░  ░░░░  ░░        ░░   ░░░  ░░        ░░  ░░░░  ░░       ░░░        ░
▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒    ▒▒  ▒▒▒▒▒  ▒▒▒▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒
▓  ▓▓▓▓  ▓▓  ▓▓▓▓  ▓▓▓  ▓▓  ▓▓▓      ▓▓▓▓  ▓  ▓  ▓▓▓▓▓  ▓▓▓▓▓  ▓▓▓▓  ▓▓       ▓▓▓      ▓▓▓
█        ██  ████  ████    ████  ████████  ██    █████  █████  ████  ██  ███  ███  ███████
█  ████  ██       ██████  █████        ██  ███   █████  ██████      ███  ████  ██        █
                                                                                          ''')

        Spielername = (str(input("Bitte gebe nun deinen Namen ein: ")))
        ork = Gegner(200, 50, 20, 'Ork')
        Kampf = Battle()
        Menue = GUI()
        User = Player(Spielername, 100, 10, 20, 2, 4)
        Spielfeld = Map(30, " P", " G", " _", " W", " I")
        Menue.Abstandshalter()

        while True:

            Spielfeld.setPlayer(User.positionX,User.positionY)
            Spielfeld.zeigeKarte()
            Menue.hauptmenue()
            Spielfeld.movePlayer(User)
            os.system('cls')  # Windows

        #Kampf.Encounter(True, User, ork)
