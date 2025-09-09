class Battle:

    def Battle_Sequenz(self, ziel, angreifer):
            print("\n" * 50)
            print(f"Ein Kampf mit {ziel.name} hat begonnen")
            while True:
                menuauswahl = int(input(f"(1)Angriff, (2)Items, (3)Flucht"))
                if menuauswahl == 1:
                        print("Angriff")
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


    def Encounter(self, is_Encounter, ziel, angreifer):
            if is_Encounter: #TODO MUSS NOCH GEMASCHT WERDEN. AKTUELL IST ES IMMER TRUE
                EntscheidungKampf = input(f"Möchtest du angreifen? y/n")
                if EntscheidungKampf == "y":
                    self.Battle_Sequenz(ziel, angreifer)
                else:
                        print(f"Du bist entkommen")
            else:
                print(f"Du gehst weg")



