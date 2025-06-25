from abc import ABC, abstractmethod
from src.car_hierarchy import Car, LuxuryCar, NonLuxuryCar
from src.suv_hierarchy import SUV, LuxurySUV, NonLuxurySUV

class Singleton:
    _instances = {}
    """Singleton class to keep traking of the instances already created. this is implemented like that for dont have more that one instance of each factory"""
    def __new__(cls):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
            print("nueva instancia",cls)
        return(cls._instances[cls])

class VehicleFactory(ABC,Singleton):
    """abstract vechicle factory"""
    LUXURY_VEHICLE = "Luxury"
    NON_LUXURY_VEHICLE = "Non-Luxury"
    @abstractmethod
    def getCar(self) -> Car:
        pass
    @abstractmethod
    def getSUV(self) -> SUV:
        pass
    def getVehicleFactory(type:str) -> "VehicleFactory":
        """method for create the factory required. The singleton inheritance allows to retrieve always the first instance created for each type"""
        if (type == __class__.LUXURY_VEHICLE):
            return (LuxuryVehicleFactory())
        elif (type == __class__.NON_LUXURY_VEHICLE):
            return (NonLuxuryVehicleFactory())


class LuxuryVehicleFactory(VehicleFactory):
    """concrete vechicle factory"""
    def getCar(self):
        return (LuxuryCar("L-C"))
    def getSUV(self):
        return (LuxurySUV("L-S"))
    
class NonLuxuryVehicleFactory(VehicleFactory):
    """another concrete vechicle factory"""
    def getCar(self):
        return (NonLuxuryCar("NL-C"))
    def getSUV(self):
        return (NonLuxurySUV("NL-S"))