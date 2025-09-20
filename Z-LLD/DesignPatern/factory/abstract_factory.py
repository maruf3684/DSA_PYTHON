from abc import ABC, abstractmethod

# ========= Abstract Products =========
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

class Bus(Vehicle):
    def getType(self) -> str:
        return "Bus"


# ========= Abstract Factory =========
class VehicleFactory(ABC):
    @abstractmethod
    def create_light_vehicle(self) -> Vehicle:
        pass

    @abstractmethod
    def create_heavy_vehicle(self) -> Vehicle:
        pass


# ========= Concrete Factories =========
class LandVehicleFactory(VehicleFactory):
    def create_light_vehicle(self) -> Vehicle:
        return Car()

    def create_heavy_vehicle(self) -> Vehicle:
        return Bike()   # treat Bike as "heavier" than Car in this family


class HeavyVehicleFactory(VehicleFactory):
    def create_light_vehicle(self) -> Vehicle:
        return Truck()  # relatively lighter in this family

    def create_heavy_vehicle(self) -> Vehicle:
        return Bus()


# ========= Client Code =========
if __name__ == "__main__":
    factories = [LandVehicleFactory(), HeavyVehicleFactory()]

    for factory in factories:
        light = factory.create_light_vehicle()
        heavy = factory.create_heavy_vehicle()

        print(f"Light: {light.getType()}, Heavy: {heavy.getType()}")