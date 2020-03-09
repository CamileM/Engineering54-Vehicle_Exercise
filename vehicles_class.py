
# === DEFINE CLASS HERE: ===

class Vehicle():


    # === THE CHARACTERISTICS FOR A VEHICLE ===
    def __init__(self, number_passengers, cargo_size, brand, horse_power, max_speed):
        self.number_passengers = number_passengers
        self.cargo_size = cargo_size


    # === THE METHODS / BEHAVIOURS FOR A VEHICLE ===
    def accelerate(self):
        return('VROOM VROOOM VROOOOOOM!!')

    def brake(self):
        return('EEEUUUCCCHHH!!!')