import os

class GUI:
    def __init__(self):
        return

    def Abstandshalter(self):
        print("\n" * 500)

    def hauptmenue(self):
        hauptmenue_entscheidung = input(str(f"(1) Nach Vorn, (2) Nach Hinten, (3) Nach Rechts, (4) Nach Links"))
        return hauptmenue_entscheidung

    def kampfmenue(self):
        kampfmenue_entscheidung = input(str(f"(1) Angreifen, (2) Flucht"))
        return kampfmenue_entscheidung

    def spielernameAbfrage(self):
        Spielername = input(str("Bitte gebe nun deinen Namen ein: "))
        return Spielername

    def Startscreen(self):
            print(f'''

                ░░      ░░░       ░░░  ░░░░  ░░        ░░   ░░░  ░░        ░░  ░░░░  ░░       ░░░        ░
        ▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒    ▒▒  ▒▒▒▒▒  ▒▒▒▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒
        ▓  ▓▓▓▓  ▓▓  ▓▓▓▓  ▓▓▓  ▓▓  ▓▓▓      ▓▓▓▓  ▓  ▓  ▓▓▓▓▓  ▓▓▓▓▓  ▓▓▓▓  ▓▓       ▓▓▓      ▓▓▓
        █        ██  ████  ████    ████  ████████  ██    █████  █████  ████  ██  ███  ███  ███████
        █  ████  ██       ██████  █████        ██  ███   █████  ██████      ███  ████  ██        █
                                                                                                  ''')


    def fehlerhafteEingabe(self):
        print(f"Diese Eingabe war ungültig")

    def bildschirmLöschen(self):
        os.system('cls')  # Windows#

    def lebenAngreiferOffen(self, angreifer):
        print(f"Du hast noch {angreifer.leben} Lebenspunkte offen.")

    def lebenVerteidigerOffen(self, verteidiger):
        print(f"{verteidiger.name} hat noch {verteidiger.leben} Lebenspunkte offen")

    def verteidigerBesiegt(self, verteidiger):
        print(f"Du hast den Kampf gewonnen. Du hast den {verteidiger.name} besiegt")

    def angreiferBesiegt(self, angreifer):
        print(f"Du wurdest besiegt, Game Over")

    def entkommen(self):
        print(f"Du bist entkommen!")

    def kampfbeginn(self, verteidiger):
        print("\n" * 50)
        print(f"Ein Kampf mit {verteidiger.name} hat begonnen")

    def kampfencounter(self):
        entscheidungKampf = input(f"Möchtest du angreifen? y/n")
        return entscheidungKampf