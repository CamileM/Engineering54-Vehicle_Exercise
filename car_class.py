
# === IMPORT VEHICLE CLASS ===

from vehicles_class import *

# === CAR CLASS BEING DEFINE WHILE INHERITED FROM VEHICLE CLASS ===

class Car(Vehicle):


    # === THE CHARACTERISTICS  FOR A CAR: ===

    def __init__(self, number_passengers, cargo_size, brand, horse_power, max_speed):
        super().__init__(number_passengers, cargo_size)
        self.brand = brand
        self.horse_power = horse_power
        self.max_speed = max_speed


    # === THE METHODS / BEHAVIOURS FOR A CAR: ===

    def park(self):
        return('AUTOMATED SELF PARKING!')

    def honk(self):
        return('BEEP! BEEP! BEEEP!')