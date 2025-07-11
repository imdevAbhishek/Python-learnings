class vector2D:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    @property
    def show(self):
        print(f"2D vector: ({self.x},{self.y})")

class vector3D(vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z=z

    @property
    def show2(self):
         print(f"3D vector: ({self.x},{self.y},{self.z})")

v=vector3D(2,3,4)
v.show
v.show2

