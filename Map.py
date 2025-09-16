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

        self.zieheWände()

    def zieheWände(self):
        # Obere und untere Zeile
        for x in range(self.kartengroesse):
            self.karte[0][x] = self.Wand  # Obere Zeile
            self.karte[self.kartengroesse - 1][x] = self.Wand  # Untere Zeile

        # Linke und rechte Spalte
        for y in range(self.kartengroesse):
            self.karte[y][0] = self.Wand  # Linke Spalte
            self.karte[y][self.kartengroesse - 1] = self.Wand  # Rechte Spalte

    def zeigeKarte(self):
        for zeile in self.karte:
            print("".join(zeile))

    def setPlayer(self, x, y):
        self.karte[x][y] = self.Spieler
        #x ist die länge
        #y die breite

    def istBegehbar(self, x, y):
        if self.karte[x][y] == self.Wand:
            return False
        else:
            return True

    def movePlayerLeft(self, User):
        istBegehbar = self.istBegehbar(User.positionX, User.positionY-1)
        if istBegehbar == True:
            self.karte[User.positionX][User.positionY] = self.leeresFeld
            User.positionX = User.positionX
            User.positionY = User.positionY-1
            self.karte[User.positionX][User.positionY] = self.Spieler

    def movePlayerRight(self, User):
        self.karte[User.positionX][User.positionY] = self.leeresFeld
        User.positionX = User.positionX
        User.positionY = User.positionY+1
        self.karte[User.positionX][User.positionY] = self.Spieler

    def movePlayerUp(self, User):
        self.karte[User.positionX][User.positionY] = self.leeresFeld
        User.positionX = User.positionX-1
        User.positionY = User.positionY
        self.karte[User.positionX][User.positionY] = self.Spieler

    def movePlayerDown(self, User):
        self.karte[User.positionX][User.positionY] = self.leeresFeld
        User.positionX = User.positionX+1
        User.positionY = User.positionY
        self.karte[User.positionX][User.positionY] = self.Spieler
'''

Kollisionen oder Kämpfe werden hier ausgelöst.
'''