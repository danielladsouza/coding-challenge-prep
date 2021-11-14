import functools
import unittest

"""
  [0,1,2,3,4,5,6]
  0 1 1  2 3 5 8
  https://docs.python.org/3/library/functools.html
"""

class Compute():
    @functools.cache
    def fibonacci(self, n):
        return self.fibonacci(n-1) + self.fibonacci(n-2) if n > 1 else n

def fibonacci(n, memo=dict()):
    """
        T.C. first call to fibonacci
        fib(4) - 4 recursive calls - 3 2 1 0
        fib(5) - no calls just lookup value result
    """
    result = 0
    if n in memo:
        return memo[n]

    if n < 2:
        result = n
    else:
        result = fibonacci(n-1, memo) + fibonacci(n-2, memo)

    memo[n] = result  # memoize

    return result


class TestCompute(unittest.TestCase):
    def setUp(self):
        self._compute = Compute()

    def test_fibonacci_0_returns_0(self):
        self.assertEqual(self._compute.fibonacci(0), 0)

    def test_fibonacci_1_returns_1(self):
        self.assertEqual(self._compute.fibonacci(1), 1)

    def test_fibonacci_2_returns_1(self):
        self.assertEqual(self._compute.fibonacci(2), 1)

    def test_fibonacci_3_returns_2(self):
        self.assertEqual(self._compute.fibonacci(3), 2)

print(fibonacci(2))
print(fibonacci(3))
if __name__ == '__main__':
    unittest.main()
