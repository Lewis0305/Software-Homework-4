import unittest
import average

class TestStringMethods(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(average.average([10,14,12]), 12)
        self.assertEqual(average.average([1, 2, 5, 6]), 3.5)
        self.assertEqual(average.average([1, 1, 1]), 1)


    def test_types(self):
        self.assertEqual(average.average([10, "11", 12]), 0)
        self.assertEqual(average.average([9.5, 14.5, 12]), 12)
        self.assertEqual(average.average([10, "kjad", 12]), 0)


    def test_empty(self):
        self.assertEqual(average.average([]), 0)



if __name__ == '__main__':
    unittest.main()
