from abc import ABC, abstractmethod
# Beginning of Car hierarchy
class Car(ABC):
    """abstract class for car hierarchy"""
    def __init__(self, name):
        self._name = name
    @abstractmethod
    def getName(self) -> str:
        pass
    @abstractmethod
    def getFeatures(self) -> str:
        pass

class LuxuryCar(Car):
    """concrete class for car hierarchy"""
    def __init__(self, name):
        super().__init__(name)
    def getName(self):
        return (self._name)
    def getFeatures(self):
        return ("Luxury Car Features")
    
class NonLuxuryCar(Car):
    """another concrete class for car hierarchy"""
    def __init__(self, name):
        super().__init__(name)
    def getName(self):
        return (self._name)
    def getFeatures(self):
        return ("Non Luxury Car Features")
# End of Car hierarchy