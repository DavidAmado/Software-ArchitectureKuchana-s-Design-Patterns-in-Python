from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, ID, name):
        self._ID = ID
        self._name = name

    def __repr__(self):
        return("Emp Name:: "+self._name+" Emp ID:: "+str(self._ID))

    def save(self):
        file = open("emp.txt","w")
        file.write(self.__repr__()+"\n")
        file.close()
    @abstractmethod
    def computeCompensation(self):
        pass

class Consultant(Employee):
    def __init__(self, ID, name):
        super().__init__(ID, name)
    def computeCompensation(self):
        return("consultant salary is this")

class SalesRep(Employee):
    def __init__(self, ID, name):
        super().__init__(ID, name)
    def computeCompensation(self):
        return("SalesRep salary is that")