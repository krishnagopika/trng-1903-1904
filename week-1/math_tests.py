import unittest
from package import fact, multiply


class TestMath(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply.multiply(2,3), 6)
    def test_factorial(self):
        self.assertEqual(fact.factorial(4), 24)
        self.assertTrue(5!=5)



if __name__ == "__main__":
    unittest.main()