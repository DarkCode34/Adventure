class Gegner:
    def __init__(self, leben, angriff, verteidigung):
        self.leben = leben
        self.angriff = angriff
        self.verteidigung = verteidigung

    def angreifen (self, ziel):

        ziel.leben = ziel.leben- self.angriff
        print(f"Das ZIel in der klasse hat {ziel.leben}")

    # muss noch definiert werden


#def angreifen (self, verteidung):
#        return self.verteidigung
    #muss noch definiert werden

