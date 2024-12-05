from math import sqrt
from module import computed_property


class Vector:
    def __init__(self, x, y, z, color=None):
        self.x, self.y, self.z = x, y, z
        self.color = color

    @computed_property("x", "y", "z")
    def magnitude(self):
        """Vector magnitude"""
        print("computing magnitude")
        return sqrt(self.x**2 + self.y**2 + self.z**2)


v = Vector(9, 2, 6)
print(v.magnitude)
v.color = "red"
print(v.magnitude)
v.y = 18
print(v.magnitude)
