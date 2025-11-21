class Car():
    def __init__ (self, model, color):
        self.model = model
        self.color = color
    
    def crash(self):
        return f"Den röda {Bil1.model}:an krockar in i den mörkgröna {Bil2.model}:an's bak\n Den mörkgröna {Bil2.model}an blir rearendad av den röda{Bil1.model}:an"

Bil1 = Car("Mazda MX5", "Röd")
Bil2 = Car("Audi R8", "Mörkgrön")

print(Bil1.crash())
print(Bil2.crash())


