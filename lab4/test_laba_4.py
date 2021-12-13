import unittest
from laba_4 import gluing, calculation_tabular_method, summator, preobrazovatel, addition, to_SDNF


class TestLaba(unittest.TestCase):

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

    def test_summator(self):
        self.assertEqual(summator(),
            [[0, 0, 0, 0, 0], [0, 0, 1, 1, 0],
            [0, 1, 0, 1, 0], [0, 1, 1, 0, 1],
            [1, 0, 0, 1, 0], [1, 0, 1, 0, 1],
            [1, 1, 0, 0, 1], [1, 1, 1, 1, 1]]
    )

    def test_preobrazovatel(self):
        self.assertEqual(preobrazovatel(),
            [[0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 1, 0, 1, 1, 0],
            [0, 0, 1, 0, 0, 1, 1, 1], [0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 1], [0, 1, 0, 1, 1, 0, 1, 0],
            [0, 1, 1, 0, 1, 0, 1, 1], [0, 1, 1, 1, 1, 1, 0, 0],
            [1, 0, 0, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 1], [1, 0, 1, 1, '-', '-', '-', '-'],
            [1, 1, 0, 0, '-', '-', '-', '-'], [1, 1, 0, 1, '-', '-', '-', '-'],
            [1, 1, 1, 0, '-', '-', '-', '-'], [1, 1, 1, 1, '-', '-', '-', '-']]
        )

    def test_addition(self):
        self.assertEqual(addition([0,0,0,0], [0,0,0,0]), [0,0,0,0])
        self.assertEqual(addition([0,1,0,0], [0,1,0,0]), [1,0,0,0])
        self.assertEqual(addition([0,0,0,0,0,0,0,1], [0,0,0,0,0,1,0,1]), [0,0,0,0,0,1,1,0])
        self.assertEqual(addition([0], [1]), [1])
        self.assertEqual(addition([1,1,1,1], [0,0,0,0]), [1,1,1,1])

    def test_to_SDNF(self):
        self.assertEqual(to_SDNF(3,
            [[0, 0, 0, 0, 0], [0, 0, 1, 1, 0],
            [0, 1, 0, 1, 0], [0, 1, 1, 0, 1],
            [1, 0, 0, 1, 0], [1, 0, 1, 0, 1],
            [1, 1, 0, 0, 1], [1, 1, 1, 1, 1]]),
            '!a*!b*c + !a*b*!c + a*!b*!c + a*b*c'
        )
        self.assertEqual(to_SDNF(4,
            [[0, 0, 0, 0, 0], [0, 0, 1, 1, 0],
            [0, 1, 0, 1, 0], [0, 1, 1, 0, 1],
            [1, 0, 0, 1, 0], [1, 0, 1, 0, 1],
            [1, 1, 0, 0, 1], [1, 1, 1, 1, 1]]),
            '!a*b*c + a*!b*c + a*b*!c + a*b*c'
        )


if __name__ == '__main__':
    unittest.main()