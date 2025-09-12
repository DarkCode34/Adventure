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

    def setPlayer(self, x, y):
        self.karte[x][y] = self.Spieler
        #x ist die länge
        #y die breite

    def movePlayer(self, User):
        User_Decide = input("Möchtest du ihn bewegen?")
        if User_Decide == "y":
            self.karte[User.positionX][User.positionY] = self.leeresFeld
            User.positionX = User.positionX
            User.positionY = User.positionY-1
            self.karte[User.positionX][User.positionY] = self.Spieler


'''
#Gegner bewegen (move_enemies)
c
Prüfen, ob ein Feld frei ist

Spielfeld darstellen (draw_map)

Koordination von Spieler & Gegner

Die Map-Klasse kennt die Positionen von allem.

Wenn sich der Spieler oder ein Gegner bewegt, wird die Map aktualisiert.

Kollisionen oder Kämpfe werden hier ausgelöst.
'''