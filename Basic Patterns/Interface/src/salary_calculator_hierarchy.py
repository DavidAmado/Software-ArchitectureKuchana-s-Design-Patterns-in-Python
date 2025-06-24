from abc import ABC, abstractmethod
class SalaryCalculatorInterface(ABC):
    @abstractmethod
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