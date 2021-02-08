import unittest
import names

class TestStringMethods(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(names.name("sam", "lewis"), "sam lewis")
        self.assertEqual(names.name("one", "two"), "one two")
        self.assertEqual(names.name("first", "last"), "first last")


    def test_types(self):
        self.assertEqual(names.name("sam", 1), "sam 1")
        self.assertEqual(names.name("sam", 2.31), "sam 2.31")
        self.assertEqual(names.name("", 2.31), "")


    def test_empty(self):
        self.assertEqual(names.name("sam", ""), "")
        self.assertEqual(names.name("", ""), "")
        self.assertEqual(names.name(" ", " "), "   ")


if __name__ == '__main__':
    unittest.main()
