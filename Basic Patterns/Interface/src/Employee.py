from src.salary_calculator_hierarchy import SalaryCalculatorInterface

class Employee:
    def __init__(self, name: str, empType: SalaryCalculatorInterface):
        self._name = name
        self._empType = empType
    def display(self):
        print("Name:",self._name)
        print("Salary:",self._empType._getSalary())