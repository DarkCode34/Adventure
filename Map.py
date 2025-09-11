class Map:
    def __init__(self, kartengroesse, Spieler, Enemy, leeresFeld, Wand, Items):
        self.kartengroesse = kartengroesse
        self.Spieler = Spieler
        self.Gegner = Enemy
        self.leeresFeld = leeresFeld
        self.Wand = Wand
        self.Item = Items

        # Ein 2D-Array erstellen (Liste von Listen), gefüllt mit leeren Feldern
        self.karte = [[self.leeresFeld for _ in range(kartengroesse)] for _ in range(kartengroesse)]

    def zeigeKarte(self):
        for zeile in self.karte:
            print("".join(zeile))




'''#
#Spielfeld-Methoden
#
#Spieler bewegen (move_player)
#
Gegner bewegen (move_enemies)
c
Prüfen, ob ein Feld frei ist

Spielfeld darstellen (draw_map)

Koordination von Spieler & Gegner

Die Map-Klasse kennt die Positionen von allem.

Wenn sich der Spieler oder ein Gegner bewegt, wird die Map aktualisiert.

Kollisionen oder Kämpfe werden hier ausgelöst.
'''