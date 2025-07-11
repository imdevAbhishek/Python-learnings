class Animal:
    def A():
        print("It is animal class.")

class Pets(Animal):
    def P():
        print("It is pets class.")

class Dog(Pets):
    def D():
        print("It is dog class.")


an=Dog()
an.D