import unittest
import math
from ulps import ulps

class TestUlpsFunction(unittest.TestCase):
    def test_one(self):
        self.assertEqual(ulps(-1.0, -1.0000000000000003), 1.0)

    def test_two(self):
        self.assertEqual(ulps(1.0, 1.0000000000000003), 1.0)

    def test_three(self):
        self.assertEqual(ulps(1.0, 1.0000000000000004), 2.0)

    def test_four(self):
        self.assertEqual(ulps(1.0, 1.0000000000000005), 2.0)

    def test_five(self):
        self.assertEqual(ulps(1.0, 1.0000000000000006), 3.0)

    def test_six(self):
        self.assertEqual(ulps(0.9999999999999999, 1.0), 1.0)

    def test_seven(self):
        self.assertEqual(ulps(0.4999999999999995, 2.0), 9007199254741001)

    def test_eight(self):
        self.assertEqual(ulps(0.5000000000000005, 2.0), 9007199254740987)

    def test_nine(self):
        self.assertEqual(ulps(0.5, 2.0), 9007199254740992)

    def test_ten(self):
        self.assertEqual(ulps(1.0, 2.0), 4503599627370496)

    def test_eleven(self):
        self.assertEqual(ulps(-1.0, 1.0), float('inf'))

    def test_twelve(self):
        self.assertEqual(ulps(-1.0, 0.0), float('inf'))

    def test_thirteen(self):
        self.assertEqual(ulps(0.0, 1.0), float('inf'))

    def test_fourteen(self):
        self.assertEqual(ulps(5.0, math.inf), float('inf'))

    def test_fifteen(self):
        self.assertEqual(ulps(15.0, 100.0), 12103423998558208)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)