# ----------------------------------------------------
# Description:
# This program demonstrates method overriding where
# child classes provide their own implementation
# of a parent class method.
# ----------------------------------------------------

class Vehicle:

    def start(self):
        print("Vehicle is starting.")


class Car(Vehicle):

    def start(self):
        print("Car starts using an engine.")


class ElectricCar(Vehicle):

    def start(self):
        print("Electric car starts using an electric motor.")


car = Car()
electric_car = ElectricCar()

print("Car:")
car.start()

print("\nElectric Car:")
electric_car.start()