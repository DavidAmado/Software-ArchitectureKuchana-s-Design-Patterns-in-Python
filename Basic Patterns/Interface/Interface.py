class SalaryCalculatorInterface:
    def _getSalary(self) -> float:
        pass

class CategoryA(SalaryCalculatorInterface):
    def __init__(self, baseSalary, salesAmt):
        self._baseSalary = baseSalary
        self._salesAmt = salesAmt
    def _getSalary(self):
        return(self._baseSalary + self._salesAmt)

class CategoryB(SalaryCalculatorInterface):
    def __init__(self, baseSalary, salesAmt):
        self._baseSalary = baseSalary
        self._salesAmt = salesAmt
        self._commission = 0.02
    def _getSalary(self):
        return(self._baseSalary + (self._commission * self._salesAmt))


class Employee:
    def __init__(self, name: str, empType: SalaryCalculatorInterface):
        self._name = name
        self._empType = empType
    def display(self):
        print("Name:",self._name)
        print("Salary:",self._empType._getSalary())

def init():
    emp1=CategoryA(10000,200)
    c1=CategoryA(10000,200)
    c2=CategoryB(20000,800)
    e1=Employee("Pedro",c1)
    e2=Employee("Pablo",c2)
    e1.display()
    e2.display()

init()
