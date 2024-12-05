from module import computed_property


class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    @computed_property("radius", "area")
    def diameter(self):
        """Circle diameter from radius"""
        print("computing diameter")
        return self.radius * 2


help(Circle)
