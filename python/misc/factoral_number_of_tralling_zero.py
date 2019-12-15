#!/usr/bin/python

import unittest

class FactorialTrallingZeroCalculation:
    def zeros(self, n):
        if n == 0:
            return n
        val, z_num = n, 0
        while val > 1:
            val = val//5
            z_num += val
        return z_num

class ZeroCalculationTest(unittest.TestCase):
    def test_the_factorial_of_0(self):
        fc = FactorialTrallingZeroCalculation()
        self.assertEquals(fc.zeros(0), 0, "Testing with n = 0")

    def test_the_factorial_of_6(self):
        fc = FactorialTrallingZeroCalculation()
        self.assertEquals(fc.zeros(6), 1, "Testing with n = 6")

    def test_the_factorial_of_30(self):
        fc = FactorialTrallingZeroCalculation()
        self.assertEquals(fc.zeros(30), 7, "Testing with n = 30")

if __name__ == "__main__":
    unittest.main()
