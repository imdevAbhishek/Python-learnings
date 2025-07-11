class Employee:
    name="Abhishek"
    language="Python"

    @property
    def name1(self):
        print(f"The name is {self.name}")

    @property
    def language1(self):
        print(f"The Language he choose {self.language}")

e=Employee()
e.name1
e.language1