
# === IMPORT ALL THE CLASSES HERE ===

from car_class import *
from plane_class import *
from vehicles_class import *

# === VEHICLE TEST ===

test_vehicle = Vehicle('NUMBER OF PASSENGERS', 'CARGO SIZE')
print('VEHICLE CHARACTERISTICS:')
print(test_vehicle.number_passengers)
print(test_vehicle.cargo_size)

print('')

print('VEHICLE METHODS:')
print(test_vehicle.accelerate())
print(test_vehicle.brake())


print('')

# === CAR 1 AKA BMW X6 M SPORT ===

# 1. MAKE CAR 1 ACCELERATE AND BRAKE

run_car1 = Car('5 Seats', 'CargoSize', 'BMW X6 M SPORT', '195 to 460 kW', '142 mph')
print('CAR 1 CHARACTERISTICS:')
print(run_car1.number_passengers)
print(run_car1.cargo_size)

print('')

print('CAR 1 METHODS:')
print(run_car1.accelerate())
print(run_car1.brake())
print(run_car1.brand)
print(run_car1.horse_power)
print(run_car1.max_speed)

print('')

# === CAR 2 AKA MERCEDES-BENZ GLE COUPE ===

# 2. MAKE CAR 2 BRAKE AND PARK
run_car2 = Car('4 Seats', 'CargoSize', 'MERCEDES-BENZ GLE COUPE', '180 to 320 kW', '155 mph')
print('CAR 2 CHARACTERISTICS:')
print(run_car2.number_passengers)
print(run_car2.cargo_size)

print('')

print('CAR 2 METHODS:')
print(run_car2.brake())
print(run_car2.park())
print(run_car2.brand)
print(run_car2.horse_power)
print(run_car2.max_speed)

print('')

# === PLANE 1 AKA RYAN-AIR ===

# 1. MAKE PLANE 1 ACCELERATE AND BRAKE
run_plane1 = Plane('197 Seats', 'CargoSize', 'RYAN-AIR', 'HORSE POWER', 'MAX SPEED')
print('PLANE 1 CHARACTERISTICS:')
print(run_plane1.number_passengers)
print(run_plane1.cargo_size)

print('')

print('PLANE 1 METHODS:')
print(run_plane1.accelerate())
print(run_plane1.brake())
print(run_plane1.brand)
print(run_plane1.horse_power)
print(run_plane1.max_speed)

print('')

# === PLANE 2 AKA EASY JET ===

# 2. MAKE PLANE 2 FLY AND LAND
run_plane2 = Plane('180 Seats', 'CargoSize','EASY JET', 'HORSE POWER', 'MAX SPEED')
print('PLANE 2 CHARACTERISTICS:')
print(run_plane2.number_passengers)
print(run_plane2.cargo_size)

print('')

print('PLANE 2 METHODS:')
print(run_plane2.take_off())
print(run_plane2.land())
print(run_plane2.brand)
print(run_plane2.horse_power)
print(run_plane2.max_speed)



