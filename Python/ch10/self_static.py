class Employee:
    language="Python"
    Salary=120000

    def getinfo(self):
        print(f"The Language is {self.language}. The salary is {self.Salary}.")
    
    @staticmethod
    def greet():
        print("Good Morning.")

Abhi = Employee()
Abhi.language="JavaScript"
Abhi.greet()
Abhi.getinfo()
