class Player:
    def __init__(self, name, leben, angriff, verteidigung):
        self.name = name
        self.leben = leben
        self.angriff = angriff
        self.verteidigung = verteidigung

    def angreifen(self, verteidiger):

        verteidiger.leben = (int(verteidiger.leben) + (verteidiger.verteidigung + 1) - self.angriff)
        # TODO muss noch verbessert / feingetun werden
