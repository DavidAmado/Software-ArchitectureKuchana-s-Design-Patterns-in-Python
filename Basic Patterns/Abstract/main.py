from src.employee_hierarchy import Consultant, SalesRep

if __name__ == "__main__":
    employee = Consultant(1, "Pedro")
    print(employee.computeCompensation())
    employee = SalesRep(2, "Pablo")
    print(employee.computeCompensation())