class Animals:
    def __init__(self,name):
        self.name=name

class Mammals(Animals):
    def __init__(self,name,fur_color):
        super().__init__(name)
        self.fur_color=fur_color

class Dog(Mammals):
    def __init__(self,name, fur_color, breed):
        super().__init__(name,fur_color)
        self.breed=breed

anm=Dog("Rex", "Brown", "Labrador")
print(f"Dog name: {anm.name}, Color: {anm.fur_color}, Breed:{anm.breed}.")
