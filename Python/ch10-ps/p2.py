class calculator:

    def __init__(self, number):
        self.n=number

    def Square(self):
        result=self.n**2
        print(f"Square is {result}")

    def Cube(self):
        result=self.n**3
        print(f"cube is {result}")

    def SquareRoot(self):
        result=self.n**0.5
        print(f"Square is {result}")


C = calculator(9)
C.Square()
C.Cube()
C.SquareRoot()