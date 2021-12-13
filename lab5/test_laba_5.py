import unittest
from laba_5 import init_table, addition, to_SDNF, gluing, calculation_tabular_method


class TestLaba(unittest.TestCase):
    table = init_table()

    def test_init_table(self):
        self.assertEqual(init_table(), self.table)

    def test_addition(self):
        self.assertEqual(addition([0,0,0,0], [0,0,0,0]), [0,0,0,0])
        self.assertEqual(addition([0,1,0,0], [0,1,0,0]), [1,0,0,0])
        self.assertEqual(addition([0,0,0,0,0,0,0,1], [0,0,0,0,0,1,0,1]), [0,0,0,0,0,1,1,0])
        self.assertEqual(addition([0], [1]), [1])
        self.assertEqual(addition([1,1,1,1], [0,0,0,0]), [1,1,1,1])

    def test_to_SDNF(self):
        self.assertEqual(to_SDNF(0, self.table), '!a*b*c*d + a*b*c*d')
        self.assertEqual(to_SDNF(1, self.table), '!a*!b*c*d + !a*b*c*d + a*!b*c*d + a*b*c*d')
        self.assertEqual(to_SDNF(2, self.table), '!a*!b*!c*d + !a*!b*c*d + !a*b*!c*d + !a*b*c*d + a*!b*!c*d + a*!b*c*d + a*b*!c*d + a*b*c*d')

    def test_gluing(self):
        self.assertEqual(gluing([
            ['!a', '!b', 'c', 'd'], ['!a', 'b', '!c', '!d'],
            ['!a', 'b', '!c', 'd'], ['!a', 'b', 'c', '!d'],
            ['!a', 'b', 'c', 'd'], ['a', '!b', '!c', '!d'],
            ['a', '!b', '!c', 'd'], ['a', '!b', 'c', '!d']], 3),
            [['!a', 'c', 'd'], ['!a', 'b', '!c'],
            ['!a', 'b', '!d'], ['!a', 'b', 'd'],
            ['!a', 'b', 'c'], ['a', '!b', '!c'],
            ['a', '!b', '!d']]
        )
        self.assertEqual(gluing([
            ['!a', 'c', 'd'], ['!a', 'b', '!c'], 
            ['!a', 'b', '!d'], ['!a', 'b', 'd'],
            ['!a', 'b', 'c'], ['a', '!b', '!c'],
            ['a', '!b', '!d']], 2),
            [['!a', 'b'], ['!a', 'b']]
        )
        self.assertEqual(gluing([['!a', 'b'], ['!a', 'b']], 1), [])

    def test_calculation_tabular_method(self):
        self.assertEqual(calculation_tabular_method(
            [['!a', 'b'], ['!a', 'c', 'd'], ['a', '!b', '!c'], ['a', '!b', '!d']],
            [['!a', '!b', 'c', 'd'], ['!a', 'b', '!c', '!d'],
            ['!a', 'b', '!c', 'd'], ['!a', 'b', 'c', '!d'],
            ['!a', 'b', 'c', 'd'], ['a', '!b', '!c', '!d'],
            ['a', '!b', '!c', 'd'], ['a', '!b', 'c', '!d']]),
            [['!a', 'c', 'd'], ['!a', 'b'], ['a', '!b', '!c'], ['a', '!b', '!d']]
        )
        self.assertEqual(calculation_tabular_method(
            [['!b', '!c'], ['!b', '!d'], ['!a', 'b', 'c', 'd']],
            [['!a', '!b', '!c', '!d'], ['!a', '!b', '!c', 'd'],
            ['!a', '!b', 'c', '!d'], ['!a', 'b', 'c', 'd'],
            ['a', '!b', '!c', '!d'], ['a', '!b', '!c', 'd'],
            ['a', '!b', 'c', '!d']]),
            [['!b', '!c'], ['!b', '!d'], ['!a', 'b', 'c', 'd']]
        )
        self.assertEqual(calculation_tabular_method(
            [['!a', '!c', 'd'], ['!b', '!c', 'd'], ['!a', 'c', '!d'], ['!b', 'c', '!d']],
            [['!a', '!b', '!c', 'd'], ['!a', '!b', 'c', '!d'],
            ['!a', 'b', '!c', 'd'], ['!a', 'b', 'c', '!d'],
            ['a', '!b', '!c', 'd'], ['a', '!b', 'c', '!d']]),
            [['!a', '!c', 'd'], ['!a', 'c', '!d'], ['!b', '!c', 'd'], ['!b', 'c', '!d']]
        )


if __name__ == '__main__':
    unittest.main()