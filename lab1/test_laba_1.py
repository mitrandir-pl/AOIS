import unittest
from laba_1 import to_straight, addition, multiplication, division


class TestLaba(unittest.TestCase):

    def test_to_straight(self):
        self.assertEqual(to_straight(14), '0000000000001110')
        self.assertEqual(to_straight(25), '0000000000011001')
        self.assertEqual(to_straight(-8), '1000000000001000')


    def test_addition(self):
        self.assertEqual(addition(to_straight(14), to_straight(25)), '0000000000100111')
        self.assertEqual(addition(to_straight(8), to_straight(8)), '0000000000010000')
        self.assertEqual(addition(to_straight(12), to_straight(20)), '0000000000100000')


    def test_multiplication(self):
        self.assertEqual(multiplication(to_straight(14), to_straight(25)), '0000000101011110')
        self.assertEqual(multiplication(to_straight(10), to_straight(10)), '0000000001100100')
        self.assertEqual(multiplication(to_straight(8), to_straight(13)), '0000000001101000')

    def test_divisional(self):
        self.assertEqual(division(to_straight(10), to_straight(18)), '0000000000000000,01010')
        self.assertEqual(division(to_straight(14), to_straight(25)), '0000000000000000,01110')
        self.assertEqual(division(to_straight(50), to_straight(4)), '0000000000001100,00010')


if __name__ == '__main__':
    unittest.main()

