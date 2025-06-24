from src.salary_calculator_hierarchy import SalaryCalculatorInterface

class Employee:
    """Employee class, requires a SalaryCalculatorInterface which means that a CategoryA or CatogoryB should be passed"""
    def __init__(self, name: str, empType: SalaryCalculatorInterface):
        self._name = name
        self._empType = empType
    def display(self):
        """Method for displaying employee info"""
        print("Name:",self._name)
        print("Salary:",self._empType._getSalary())