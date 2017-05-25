# Vaule of the car
cars = 100
# How many seats have a car
space_in_a_car = 4.0
# Number of Drivers
drivers = 30
# Number of passenegers
passengers = 90
# Account how many car was not driven 
cars_not_driven = cars - drivers
# How many cars are driven
cars_driven = drivers
# Capacity of the car 
carpool_capacity = float(cars_driven * space_in_a_car)
#average passenger per car 
average_passengers_per_car = passengers / cars_driven


print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")