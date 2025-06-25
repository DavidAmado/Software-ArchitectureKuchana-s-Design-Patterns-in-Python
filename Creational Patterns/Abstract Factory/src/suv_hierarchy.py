from abc import ABC, abstractmethod
# Beginning of SUV hierarchy
class SUV(ABC):
    """abstract class for SUV hierarchy"""
    def __init__(self, name):
        self._name = name
    @abstractmethod
    def getName(self) -> str:
        pass
    @abstractmethod
    def getFeatures(self) -> str:
        pass

class LuxurySUV(SUV):
    """concrete class for SUV hierarchy"""
    def __init__(self, name):
        super().__init__(name)
    def getName(self):
        return (self._name)
    def getFeatures(self):
        return ("Luxury SUV Features")
    
class NonLuxurySUV(SUV):
    """another concrete class for SUV hierarchy"""
    def __init__(self, name):
        super().__init__(name)
    def getName(self):
        return (self._name)
    def getFeatures(self):
        return ("Non Luxury SUV Features")
# End of SUV hierarchy