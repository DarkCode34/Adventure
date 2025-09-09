class Gegner:
    def __init__(self, leben, angriff, verteidigung, name):
        self.leben = leben
        self.angriff = angriff
        self.verteidigung = verteidigung
        self.name = name

    def angreifen (self, verteidiger):

        verteidiger.leben = verteidiger.leben + (verteidiger.verteidigung* 0.5) - self.angriff
        #TODO muss noch verbessert / feingetun werden
        

