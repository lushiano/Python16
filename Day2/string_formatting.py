#String formatting

x = 10
y = 5
z = x+y

print("My numbers are " + str(x) + " and " + str(y))

print("Again my numbers are {} and {}".format(x,y))

print("The sum of {} and {} is equal to {}".format(x,y,z))

color = "red"
license_plate = 541926

print(f"The car is {color} and its license plate is {license_plate}")