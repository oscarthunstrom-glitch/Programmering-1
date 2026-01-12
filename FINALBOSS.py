import random

class THEFINALBOSS:
    def __init__(self):
        self.name = "THEFINALBOSS"
        self.hp = 150
        self.strength = 30
    
        self.art = """     
                                 / \
                                /   \
          /\     /\            /     \
     .--.(  \__/   ).--.      /       \
     `._ `          ' _.'    /    _    \
        `| 👁️  👁️ |'       /    |=|    \
         |   o-o   |       /     |=|     \
          \  ~~~  /       |      |=|      |
          |\     /|        \     |=|     /
          | \ _ / |         \    |=|    /
      ___/         \___      \ __|=|__ /
    /                   \     ___|=|
   |                     \   /   (__)
   |       *     *        \_/    (__)
   |   ||           |            (__)
   |   ||           |\        .--|(_)
   |   ||   _____   | `.   _.'   |=|
   |   ||  |  |  |  |   `-'      |=|
   |   ||  |__|__|  |            |=|
   |   ||  |  |  |  |            |=|
   |   ||  |__|__|  |            |=|
   |   ||  |  |  |  |            |=|
   |   ||  |__|__|  |\           |=|
   ||||||___________|\\          |=|
    |||||           | \\         |=|
        |           | ||\        |=|
        |           | |\\|       |=|
        |     _     |  \\|       |=|
        |    | |    |  |||       |=|
        |    | |    |  |//       
        |    | |    |  //
        |    | |    |
        |    | |    |
        |    | |    |
        |    | |    |
        |    | |    |
        |    | |    | 
        /    | |    |
       /     /  \     \
      /_|___/    \___|_\ """






    def show(self):
        print(self.art)

    def attack(self):
        damage = random.randint(10, self.strength)
        print(f"{self.name} Ödslar ingen tid. Med ett hårt grepp om sin yxa gör han {damage} i skada!")
        return damage

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} ger ifrån sig ett grsoteskt vrål!\n{self.name} Blev träffad och tog {damage} i skada! {self.hp} återstår...hur ska fortsättningen gå!?")
        return self.hp
    
    def is_alive(self):
        alive = self.hp > 0
        if not alive:
            print(f"{self.name} faller till marken med ett öronbedövande vrål!")
        return alive
    
