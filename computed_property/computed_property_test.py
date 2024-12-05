import unittest
from vector import Vector
from circle import Circle


class TestComputedProperty(unittest.TestCase):

    def test_vector_magnitude(self):
        v = Vector(3, 4, 0)
        self.assertEqual(v.magnitude, 5.0)
        v.x = 6
        self.assertEqual(v.magnitude, 7.211102550927978)
        v.y = 8
        self.assertEqual(v.magnitude, 10.0)

    def test_vector_magnitude_change_color(self):
        v = Vector(3, 4, 0)
        self.assertEqual(v.magnitude, 5.0)
        v.x = 6
        self.assertEqual(v.magnitude, 7.211102550927978)
        v.color = "blue"
        self.assertEqual(v.magnitude, 7.211102550927978)
        v.y = 8
        self.assertEqual(v.magnitude, 10.0)

    def test_circle_diameter(self):
        circle = Circle()
        self.assertEqual(circle.diameter, 2)
        circle.radius = 5
        self.assertEqual(circle.diameter, 10)
        circle.diameter = 12
        self.assertEqual(circle.radius, 6)


if __name__ == "__main__":
    unittest.main()
