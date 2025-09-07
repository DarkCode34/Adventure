class Battle:

    def Battle_Sequenz(self, ziel, angreifer):
            print("\n" * 50)
            print(f"Ein Kampf mit {ziel.name} hat begonnen")


    def Encounter(self, is_Encounter, ziel, angreifer):
            if is_Encounter:
                EntscheidungKampf = input(f"Möchtest du angreifen? y/n")
                if EntscheidungKampf == "y":
                    self.Battle_Sequenz(ziel, angreifer)
                else:
                        print(f"Du bist entkommen")
            else:
                print(f"Du gehst weg")



