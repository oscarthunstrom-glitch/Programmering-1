import random

class Fälla:
    def __init__(self):
        pass

    def aktivera(self, player):
       print("\n💥 DU TRAMPAR PÅ EN FÄLLA! 💥")

       fälla_typ = random.choice(["djupt_hål", "björnfälla", "giftpilar"])

       if fälla_typ == "djupt_hål":
           print("Du föll ner i ett djupt hål och skadade dig!")
           if player.level > 1:
               player.level -= 1
               print(f"Du förlorade en level på grund av skadan! Nu är du level {player.level}...")
           else:
                print("Du är reda på level 1, men fallet gjorde ont!")
                player.take_damage(20)
                print("Du tog 20 skada från fallet.")
        
       elif fälla_typ == "björnfälla":
              print("En björnfälla klämmer åt ditt ben!")
              player.take_damage(30)
              player.level += 1
              print("Du går upp en level trots skadan!")
              print(f"Du är nu level {player.level}.")
              print("... men du tog 30 skada från björnfällan!")

       else:
            print("En giftpil träffar dig rakt  i bröstet!")
            player.take_damage(40)
            player.level += 1
            print("Du går upp en level trots skadan!")
            print("Du är nu level {player.level}.")
            print("... men du tog 40 skada från giftpilen!")
        
