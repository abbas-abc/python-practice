class Vehicle:
    def __init__(self,brand):
        self.brand=brand
    def general_info(self):
        print(f"This is a {self.brand} vehicle.")

class car(Vehicle):
    def honk(self):
        print("Beep beep!")    

veh1=car("Toyota")
veh1.general_info()
veh1.honk()
        
