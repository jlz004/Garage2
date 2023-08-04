#Jose Zaragoza
#7//29/2023
class Vehicle:

    def setMake(self, make):
        self.make = make

    def setModel(self, model):
        self.model = model

    def getMake(self):
        print(f"The make is: {self.make}")

    def getModel(self):
        print(f"The model is: {self.model}")



class Car(Vehicle):
    def setCarDoor(self, cardoor):
        self.car_door = cardoor

    def getCarDoor(self):
        print(f"The number of doors is: {self.car_door}")


class Truck(Vehicle):
    def setBedLength(self, bedlength):
        self.bed_length = bedlength

    def getBedLength(self):
        print(f"The bed length is: {self.bed_length}")

print("Welcome to Jose's Virtual Garage.")
choice = input("Enter 1 to make a Car, 2 to make a Truck, or 3 to Quit: ")

if choice == "1":
    new_car = Car()
    new_car.setMake(input("Please enter the car make: "))
    new_car.setModel(input("Please enter the car model: "))
    new_car.setCarDoor(input("PLease enter the amount of doors: "))
    new_car.getCarDoor()
    new_car.getMake()
    new_car.getModel()
    print("Your car has been added to the garage!")

elif choice == "2":
    new_truck = Truck()
    new_truck.setMake(input("Please enter the truck make: "))
    new_truck.setModel(input("Please enter the truck model: "))
    new_truck.setBedLength(input("Please enter the bed length: "))
    new_truck.getBedLength()
    new_truck.getMake()
    new_truck.getModel()
    print("Your truck has been added to the garage!")

elif choice == "3":
    quit()
else:
    print("Please enter a valid response.")
