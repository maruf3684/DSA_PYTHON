from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def getType(self) -> str:
        pass

class Car(Vehicle):
    def getType(self) -> str:
        return "Car"

class Bike(Vehicle):
    def getType(self) -> str:
        return "Bike"

class Truck(Vehicle):
    def getType(self) -> str:
        return "Truck"



###########################################################
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        pass

class CarFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Car()

class BikeFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Bike()

class TruckFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Truck()


if __name__ == "__main__":
    factories = [CarFactory(), BikeFactory(), TruckFactory()]

    for factory in factories:
        vehicle = factory.create_vehicle()
        print(vehicle.getType())