class Employee:
    company="ITC"

    def show(self):
        print(f"The company name is {self.company}.")

class cooder(Employee):
    language="Default language"
    def printlanguage(self):
        print(f"Out of all the language here is your {self.language}. ")


class programmer(cooder):
    company="ITC infotech"
    def showLanguage(self):
        print(f"The company name is {self.company} and he is good with Pyhton")

a=Employee()
c=cooder()
b=programmer()

b.show()
b.printlanguage()
b.showLanguage()


