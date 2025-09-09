class Battle:

    def rundenbasiert(self, angreifer, verteidiger):
        User_Entscheidung_Runde = (int(input(f"(1) Weiter angreifen, (2) Flucht")))
        if User_Entscheidung_Runde == 1:
            while verteidiger.leben != 0:
                self.battle_sequenz_angriff(verteidiger, angreifer)
                print(f"Du hast noch {angreifer.leben} Lebenspunkte offen")
                self.battle_sequenz_angriff(angreifer, verteidiger)
                print(f"Der Verteidiger hat noch {verteidiger.leben} Lebenspunkte offen")
                self.rundenbasiert(angreifer, verteidiger)
                break
            if verteidiger.leben == 0:
                print(f"Spiel gewonnen, Gegner besiegt")

        else:
            print("Nix")

    def battle_sequenz_angriff(self, angreifer, verteidiger):
        angreifer.angreifen(verteidiger)

    def Battle_Sequenz(self, angreifer, verteidiger):
            print("\n" * 50)
            print(f"Ein Kampf mit {verteidiger.name} hat begonnen")
            while True:
                menuauswahl = int(input(f"(1)Angriff, (2)Items, (3)Flucht"))
                if menuauswahl == 1:
                        print("Angriff")
                        #self.battle_sequenz_angriff(angreifer, verteidiger)
                        if verteidiger.leben <= 0:
                            print(f"Du hast {verteidiger.name} besiegt.")
                            print(f"Spiel gewonnen") #todo ist noch zu machen, bzw. hier kann weitergearbeitet werden.
                        else:
                            self.rundenbasiert(angreifer, verteidiger)
                            print(f"{verteidiger.name} hat noch {verteidiger.leben} Lebenspunkte offen")
                        break
                elif menuauswahl == 2:
                        print("Items")
                        break
                elif menuauswahl == 3:
                        print("Flucht")
                        break
                else:
                        print("Ungültige Auswahl")
                        break


    def Encounter(self, is_Encounter, angreifer, verteidiger):
            if is_Encounter: #kann über die Parameter übergeben werden
                EntscheidungKampf = input(f"Möchtest du angreifen? y/n")
                if EntscheidungKampf == "y":
                    self.Battle_Sequenz(angreifer, verteidiger)
                else:
                        print(f"Du bist entkommen")
            else:
                print(f"Du gehst weg")



