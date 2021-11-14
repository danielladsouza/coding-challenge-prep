import functools
import unittest

class Compute():
    @functools.cache
    def factorial(self, n):
        return n * self.factorial(n-1) if n else 1

class TestCompute(unittest.TestCase):
    def setUp(self):
        self._compute = Compute()

    def test_factorial_0_returns_1(self):
        self.assertEqual(self._compute.factorial(0), 1)

    def test_factorial_1_returns_1(self):
        self.assertEqual(self._compute.factorial(1), 1)

    def test_factorial_2_returns_1(self):
        self.assertEqual(self._compute.factorial(2), 2)

if __name__ == "__main__":
    unittest.main()