class Employee:
    a=1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e=Employee()
e.a=45
print(f"a = {e.a}")
e.show()