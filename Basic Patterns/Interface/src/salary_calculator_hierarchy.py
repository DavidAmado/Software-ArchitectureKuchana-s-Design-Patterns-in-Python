from abc import ABC, abstractmethod
# Beginningof  Salaries hierarchy
class SalaryCalculatorInterface(ABC):
    """Abstract class that performs the funtion of a 'java interface'"""
    @abstractmethod
    def _getSalary(self) -> float:
        pass

class CategoryA(SalaryCalculatorInterface):
    """Class that implements the Salary Calculator Interface"""
    def __init__(self, baseSalary, salesAmt):
        self._baseSalary = baseSalary
        self._salesAmt = salesAmt
    def _getSalary(self):
        return(self._baseSalary + self._salesAmt)

class CategoryB(SalaryCalculatorInterface):
    """Another class that implements the Salary Calculator Interface"""
    def __init__(self, baseSalary, salesAmt):
        self._baseSalary = baseSalary
        self._salesAmt = salesAmt
        self._commission = 0.02
    def _getSalary(self):
        return(self._baseSalary + (self._commission * self._salesAmt))