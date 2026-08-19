# ----------------------------------------------------
# Description:
# This program demonstrates inheritance, polymorphism,
# encapsulation, composition, and system design using
# a vehicle rental system.
# ----------------------------------------------------


class Vehicle:

    def __init__(self, vehicle_id, brand):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self._is_rented = False

    def calculate_rent(self, days):
        return 0

    def rent(self):

        if self._is_rented:
            return False

        self._is_rented = True

        return True

    def return_vehicle(self):

        if not self._is_rented:
            return False

        self._is_rented = False

        return True

    def get_status(self):

        if self._is_rented:
            return "Rented"

        return "Available"

    def display(self):

        print(f"ID: {self.vehicle_id}")
        print(f"Brand: {self.brand}")
        print(f"Status: {self.get_status()}")


class Car(Vehicle):

    def calculate_rent(self, days):

        return days * 1500


class Bike(Vehicle):

    def calculate_rent(self, days):

        return days * 700


class Truck(Vehicle):

    def calculate_rent(self, days):

        return days * 2500


class RentalSystem:

    def __init__(self):

        self.vehicles = []

    def add_vehicle(self, vehicle):

        if self.find_vehicle(vehicle.vehicle_id):

            print("Vehicle ID already exists.")
            return

        self.vehicles.append(vehicle)

        print("Vehicle added successfully.")

    def find_vehicle(self, vehicle_id):

        for vehicle in self.vehicles:

            if vehicle.vehicle_id == vehicle_id:
                return vehicle

        return None

    def display_vehicles(self):

        if not self.vehicles:

            print("No vehicles available.")
            return

        print("\n====== Vehicles ======")

        for vehicle in self.vehicles:

            vehicle.display()

            print("----------------------")

    def rent_vehicle(self, vehicle_id, days):

        vehicle = self.find_vehicle(vehicle_id)

        if vehicle is None:

            print("Vehicle not found.")
            return

        if days <= 0:

            print("Rental days must be greater than zero.")
            return

        if vehicle.rent():

            cost = vehicle.calculate_rent(days)

            print("\nVehicle rented successfully.")
            print(f"Vehicle: {vehicle.brand}")
            print(f"Days: {days}")
            print(f"Total Cost: ₹{cost:.2f}")

        else:

            print("Vehicle is already rented.")

    def return_vehicle(self, vehicle_id):

        vehicle = self.find_vehicle(vehicle_id)

        if vehicle is None:

            print("Vehicle not found.")
            return

        if vehicle.return_vehicle():

            print("Vehicle returned successfully.")

        else:

            print("Vehicle was not rented.")


rental_system = RentalSystem()


rental_system.add_vehicle(
    Car("C101", "Toyota")
)

rental_system.add_vehicle(
    Car("C102", "Honda")
)

rental_system.add_vehicle(
    Bike("B101", "Yamaha")
)

rental_system.add_vehicle(
    Bike("B102", "Royal Enfield")
)

rental_system.add_vehicle(
    Truck("T101", "Tata")
)


while True:

    print("\n====== Vehicle Rental System ======")
    print("1. Display Vehicles")
    print("2. Rent Vehicle")
    print("3. Return Vehicle")
    print("4. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:

        rental_system.display_vehicles()

    elif choice == 2:

        vehicle_id = input("Enter vehicle ID: ")
        days = int(input("Enter rental days: "))

        rental_system.rent_vehicle(
            vehicle_id,
            days
        )

    elif choice == 3:

        vehicle_id = input("Enter vehicle ID: ")

        rental_system.return_vehicle(
            vehicle_id
        )

    elif choice == 4:

        print("Thank you for using the rental system.")
        break

    else:

        print("Invalid choice.")