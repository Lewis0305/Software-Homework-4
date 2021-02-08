import unittest
import cube

import unittest

class TestStringMethods(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(cube.cube(1,2,3), 6)
        self.assertEqual(cube.cube(1, 7, 1), 7)
        self.assertEqual(cube.cube(2, 2, 2), 8)

    def test_negative(self):
        self.assertEqual(cube.cube(1, 2, -3), 0)
        self.assertEqual(cube.cube(-1, 2, -3), 0)
        self.assertEqual(cube.cube(-11, 32, -31), 0)

    def test_string(self):
        self.assertEqual(cube.cube("dsf", 2, -3), 0)
        self.assertEqual(cube.cube("dsf", "adkkjd", -3), 0)
        self.assertEqual(cube.cube("dsf", "", ""), 0)

if __name__ == '__main__':
    unittest.main()
