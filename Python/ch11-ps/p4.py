class complex:

    def __init__(self, r, i):
        self.r=r
        self.i=i

    def __add__(self, c2):
        return complex(self.r+c2.r, self.i+c2.i)
    
    def __mul__(self, c2):
        real=(self.r*c2.r - self.i*c2.i)
        img=(self.r*c2.i + self.i*c2.r)
        return complex(real,img)
    
    def __str__(self):
        return f"{self.r}+{self.i}i"
    
c1=complex(2,3)
c2=complex(4,5)

print(c1+c2)
print(c1*c2)

