#import car
from car import Car, ElectricCar

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

used_car = Car("Subaru","Outback",2019)
print(used_car.get_descriptive_name())
used_car.update_odometer(25_300)
used_car.read_odometer()
used_car.increment_odometer(100)
used_car.read_odometer()

my_leaf = ElectricCar("Nissan","Leaf",2026)
print(my_leaf.get_descriptive_name())
print(my_leaf.describe_battery())
# used_car.update_odometer(25_300)
my_leaf.read_odometer()
my_leaf.increment_odometer(100)
my_leaf.read_odometer()