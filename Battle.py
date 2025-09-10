class Battle:

    def rundenbasiert(self, angreifer, verteidiger):
        while verteidiger.leben > 0 and angreifer.leben > 0:
            self.battle_sequenz_angriff(verteidiger, angreifer)
            print(f"Du hast noch {angreifer.leben} Lebenspunkte offen")
            self.battle_sequenz_angriff(angreifer, verteidiger)
            print(f"{verteidiger.name} hat noch {verteidiger.leben} Lebenspunkte offen")
            if verteidiger.leben <= 0:
                print(f"Spiel gewonnen, {verteidiger.name} besiegt")
                break
            elif angreifer.leben <= 0:
                print(f"Du wurdest besiegt, Game Over")
                break
            User_Entscheidung_Runde = int(input(f"(1) Angreifen, (2) Flucht"))
            if User_Entscheidung_Runde == 1:
                self.rundenbasiert(angreifer, verteidiger)
            elif User_Entscheidung_Runde == 2:
                print(f"Du bist entkommen")
            break

    def battle_sequenz_angriff(self, angreifer, verteidiger):
        angreifer.angreifen(verteidiger)

    def Battle_Sequenz(self, angreifer, verteidiger):
            print("\n" * 50)
            print(f"Ein Kampf mit {verteidiger.name} hat begonnen")
            while True:
                        self.rundenbasiert(angreifer, verteidiger)
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



