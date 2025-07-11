class vector:

    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z

    def __add__(self, c2):
        return vector(self.x+c2.x, self.y+c2.y, self.z+c2.z)
    
    def __mul__(self, c2):
        a=(self.x*c2.x)
        b=(self.y*c2.y)
        c=(self.z*c2.z)
        return a + b + c
    
    def __str__(self):
        return f"Vector: {self.x}i + {self.y}j + {self.z}k"
    
c1=vector(2,3,4)
c2=vector(4,5,5)

print(c1+c2)
print(c1*c2)

