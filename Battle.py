from GUI import *

Menue = GUI()

class Battle:

    def rundenbasiert(self, angreifer, verteidiger):
        while verteidiger.leben > 0 and angreifer.leben > 0:
            self.battle_sequenz_angriff(verteidiger, angreifer)
            Menue.lebenAngreiferOffen(angreifer)
            self.battle_sequenz_angriff(angreifer, verteidiger)
            Menue.lebenVerteidigerOffen(verteidiger)
            if verteidiger.leben <= 0:
                Menue.verteidigerBesiegt(verteidiger)
                break
            elif angreifer.leben <= 0:
                Menue.angreiferBesiegt(angreifer)
                break
            User_Entscheidung_Runde = Menue.kampfmenue()
            if User_Entscheidung_Runde == '1':
                self.rundenbasiert(angreifer, verteidiger)
            elif User_Entscheidung_Runde == '2':
                Menue.entkommen()
            break

    def battle_sequenz_angriff(self, angreifer, verteidiger):
        angreifer.angreifen(verteidiger)

    def Battle_Sequenz(self, angreifer, verteidiger):
            Menue.kampfbeginn(verteidiger)
            while True:
                        self.rundenbasiert(angreifer, verteidiger)
                        break

    def Encounter(self, is_Encounter, angreifer, verteidiger):
            if is_Encounter: #kann über die Parameter übergeben werden
                EntscheidungKampf = Menue.kampfencounter()
                if EntscheidungKampf == "y":
                    self.Battle_Sequenz(angreifer, verteidiger)
                else:
                        Menue.entkommen()
            else:
                Menue.entkommen()



