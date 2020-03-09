
# === IMPORT VEHICLE CLASS ===

from vehicles_class import *

# === PLANE CLASS BEING DEFINE WHILE INHERITED FROM VEHICLE CLASS

class Plane(Vehicle):


    # === THE CHARACTERISTICS  FOR A PLANE: ===

    def __init__(self, number_passengers, cargo_size, brand, horse_power, max_speed):
        super().__init__(number_passengers, cargo_size)
        self.brand = brand
        self.horse_power = horse_power
        self.max_speed = max_speed


    # === THE METHODS / BEHAVIOURS FOR A PLANE: ===

    def take_off(self):
        return ('3 2 1 AND TAKE OFF!!')


    def land(self):
        return ('EUSTON, WE ARE READY TO LAND!!!')