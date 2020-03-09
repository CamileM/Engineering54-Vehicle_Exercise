
# === IMPORT ALL THE CLASSES HERE ===

from vehicles_class import *
from car_class import *
from plane_class import *

# === CREATE 2 VEHICLES INSTANCES (2 FOR CARS AND 2 FOR PLANE)


# === CAR 1 AKA BMW ===

# 1. MAKE CAR 1 ACCELERATE AND BRAKE
run_car1 = Vehicle('5 Seats', 'CargoSize', 'BMW', '195 to 460 kW', '142 mph')
print('CAR 1 CHARACTERISTICS:')
print(run_car1.number_passengers)
print(run_car1.cargo_size)
print(run_car1.brand)
print(run_car1.horse_power)
print(run_car1.max_speed)

print('CAR 1 METHODS:')
print(run_car1.accelerate())
print(run_car1.brake())

print('')

# === CAR 2 AKA MERCEDES-BENZ ===

# 2. MAKE CAR 2 BRAKE AND PARK
run_car2 = Vehicle('4 Seats', 'CargoSize', 'MERCEDES-BENZ GLE COUPE', '180 to 320 kW', '155 mph')
print(run_car2)
print(run_car2.brake())
print(run_car2.park())

print('')

# === PLANE 1 AKA RYAN-AIR ===

# 1. MAKE PLANE 1 ACCELERATE AND BRAKE
run_plane1 = Vehicle('197 Seats', 'CargoSize', 'RYAN-AIR', '', '')
print(run_plane1)
print(run_plane1.accelerate())
print(run_plane1.brake())

print('')

# === PLANE 2 AKA EASY JET ===

# 2. MAKE PLANE 2 FLY AND LAND
run_plane2 = Vehicle('180 Seats', 'CargoSize','EASY JET', '', '')
print(run_plane2)
print(run_plane2.fly())
print(run_plane2.land())
