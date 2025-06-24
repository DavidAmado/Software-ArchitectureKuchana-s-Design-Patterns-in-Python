from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, ID):
        self._name = name
        self._ID = ID

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
    def __init__(self, name, ID):
        super().__init__(name, ID)
    def computeCompensation(self):
        return("consultant salary is this")

class SalesRep(Employee):
    def __init__(self, name, ID):
        super().__init__(name, ID)
    def computeCompensation(self):
        return("SalesRep salary is that")


def main():
    c=Consultant("Pedro", 1)
    print(c)
    print(c.computeCompensation())
    s=SalesRep("Pablo", 2)
    print(s)
    print(s.computeCompensation())

main()
