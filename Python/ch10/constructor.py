class Employee:
    language="Python"
    salary=120000

    def __init__(self, name, language, salary):
        self.name = name
        self.language =language
        self.salary = salary
        print("I am creating a object.")

Abhi = Employee("abhi", "JavaScript", 130000)
print(Abhi.name, Abhi.language, Abhi.salary)
