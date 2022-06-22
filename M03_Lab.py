from msilib.schema import Class

class Automobile:
    def __init__(car, type, year, make, model, doors, roof):
        car.type = type
        car.year = year
        car.make = make
        car.model = model
        car.doors = doors
        car.roof = roof

car1 = Automobile
car1.type = input("Type of vehicle? ")
car1.year = int(input("What is the Year? "))
car1.make = input("What is the Make? ")
car1.model = input("What is the Model? ")
car1.doors = int(input("How many doors? "))
car1.roof = input("Roof is convertiable, Has sun roof, or solid? ")

print ("\nCar 1 Made:")
print ("\nVehicle Type: " + car1.type)
print ("Year: " + str(car1.year))
print ("Make: " + car1.make)
print ("Model: " + car1.model)
print ("Number of doors: " + str(car1.doors))
print ("Roof Type: " + car1.roof + "\n")