class Employee:
    def __init__(self, salary):
        self.salary=salary
        self.increment=0.10

    @property
    def salaryafterincrement(self):
        return self.salary + (self.salary * self.increment)
    
    @salaryafterincrement.setter
    def salaryafterincrement(self, nsalary):
        self.increment=(nsalary-self.salary)/self.salary
    
e=Employee(50000)
print(e.salaryafterincrement)

e.salaryafterincrement=60000

print(e.increment)
