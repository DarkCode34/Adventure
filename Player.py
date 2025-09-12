class Player:
    def __init__(self, name, leben, angriff, verteidigung, positionX, positionY):
        self.name = name
        self.leben = leben
        self.angriff = angriff
        self.verteidigung = verteidigung
        self.positionX = positionX
        self.positionY = positionY

    def angreifen(self, verteidiger):

        verteidiger.leben = (int(verteidiger.leben) + (verteidiger.verteidigung + 1) - self.angriff)
        # TODO muss noch verbessert / feingetun werden
