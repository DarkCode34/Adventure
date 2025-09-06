class Gegner:
    def __init__(self, leben, angriff, verteidigung):
        self.leben = leben
        self.angriff = angriff
        self.verteidigung = verteidigung

    def angreifen (self, angriff):
        return self.angriff

    # muss noch definiert werden

    def angreifen (self, verteidung):
        return self.verteidigung
    #muss noch definiert werden

.
