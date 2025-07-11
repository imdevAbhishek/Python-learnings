class Programmer:
    company = "Microsoft"
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary
        print("Programmer details:- ")

emp1 = Programmer("Abhishek", "Manager", 1300000)
print(emp1.company)
print(emp1.name)
print(emp1.role)
print(emp1.salary)

emp2 = Programmer("Rohan", "intern", 1300000)
print(emp2.company)
print(emp2.name)
print(emp2.role)
print(emp2.salary)
