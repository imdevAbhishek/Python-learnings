class Employee:
    company="ITC"

    def show(self):
        print(f"The name is {self.company}.")

class programmer(Employee):
    company="ITC infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with Pyhton")

a=Employee("Abhi")
b=programmer("Abhi")

print(a.company, b.company)
a.show()
b.showLanguage()