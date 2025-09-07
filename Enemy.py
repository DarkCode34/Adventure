class Gegner:
    def __init__(self, leben, angriff, verteidigung, name):
        self.leben = leben
        self.angriff = angriff
        self.verteidigung = verteidigung
        self.name = name

    def angreifen (self, ziel):

        ziel.leben = ziel.leben + (ziel.verteidigung* 0.5) - self.angriff
        #TODO muss noch verbessert / feingetun werden
        
        if ziel.leben <= 0:
            print(f"Du wurdest von {self.name} besiegt.")
        else:
            print(f"Du hast noch {ziel.leben} Lebenspunkte offen")




#def angreifen (self, verteidung):
#        return self.verteidigung
    #muss noch definiert werden

