from src.Employee import Employee
from src.salary_calculator_hierarchy import CategoryA, CategoryB

if __name__ == "__main__":
    cat1 = CategoryA(10000,200)
    cat2 = CategoryB(20000,800)
    employee = Employee("Pedro",cat1)
    employee.display()
    employee = Employee("Pablo",cat2)
    employee.display()
