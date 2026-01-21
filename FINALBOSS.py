import random    
import sys,time,random

class THEFINALBOSS:   
    def __init__(self):
        self.name = "THEFINALBOSS"
        self.hp = 200
        self.strength = 99
    
        self.art = """     
                                 
                                ______
          /\\    /\\           /     \\
     .--.(  \\_/   ).--.      /       \\
     `._ `          ' _.'    /    _    \\
        `| 👁️  👁️ |'       /    |=|    \\
         |   o-o   |       /     |=|     \\
          \\ ~~~  /       |      |=|      |
          |\\    /|        \\    |=|     /
          |\\ _ / |         \\   |=|    /
      ___/         \\___     \\ _|=|__ /
    /                   \\    ___|=|
   |                     \\  /   (__)
   |       *     *        \\/    (__)
   |   ||           |            (__)
   |   ||           |\\       .--|(_)
   |   ||   _____   | `.   _.'   |=|
   |   ||  |  |  |  |   `-'      |=|
   |   ||  |__|__|  |            |=|
   |   ||  |  |  |  |            |=|
   |   ||  |__|__|  |            |=|
   |   ||  |  |  |  |            |=|
   |   ||  |__|__|  |\\           |=|
   ||||||___________|\\           |=|
    |||||           | \\          |=|
        |           | ||\\        |=|
        |           | |\\|        |=|
        |     _     |  \\|        |=|
        |    | |    |  |||      |=|
        |    | |    |  |//       
        |    | |    |  //
        |    | |    |
        |    | |    |
        |    | |    |
        |    | |    |
        |    | |    |
        |    | |    | 
        /    | |    |_
       /     / \\     \\
      /_|___/   \\___|_\\ """


    def show(self):
        print(self.art)

    def attack(self):    #slumpskadan
        damage = random.randint(44, self.strength)
        print_slow(f"{self.name} Ödslar ingen tid. Med ett hårt grepp om sin yxa gör han {damage} i skada!")
        return damage

    def take_damage(self, damage):
        self.hp -= damage
        print_slow(f"{self.name} ger ifrån sig ett grsoteskt vrål!\n{self.name} Blev träffad och tog {damage} i skada! {self.hp} återstår...hur ska fortsättningen gå!?")
        return self.hp

    def is_alive(self):    #ifall bossen lever
        alive = self.hp > 0
        if not alive:
            print_slow(f"{self.name} faller till marken med ett öronbedövande vrål!")
        return alive

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
