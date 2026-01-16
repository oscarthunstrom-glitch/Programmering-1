import random

class Fälla:
    def __init__(self):
        pass

    def aktivera(self, player):
       print("\n💥 DU TRAMPAR PÅ EN FÄLLA! 💥")

       fälla_typ = random.choice(["djupt_hål", "björnfälla", "giftpilar"])

       if fälla_typ == "djupt_hål":
           print("Du föll ner i ett djupt hål och skadade dig!")
           player.take_damage(20)
        
       elif fälla_typ == "björnfälla":
              print("En björnfälla klämmer åt ditt ben!")
              player.take_damage(30)
              
       else:
            print("En giftpil träffar dig rakt i bröstet!")
            player.take_damage(40)
        
