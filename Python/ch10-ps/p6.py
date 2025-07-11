class calculator:

    def __init__(slf, number):
        slf.n=number

    def Square(slf):
        result=slf.n**2
        print(f"Square is {result}")

    def Cube(slf):
        result=slf.n**3
        print(f"cube is {result}")

    def SquareRoot(slf):
        result=slf.n**0.5
        print(f"Square root is {result}")

    @staticmethod
    def greet():
        print("Hello!")


C = calculator(2)
C.greet()
C.Square()
C.greet()
C.Cube()
C.greet()
C.SquareRoot()