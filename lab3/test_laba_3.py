import unittest
from laba_3 import gluing, calculation_method, calculation_tabular_method, tabular_method


class TestLaba(unittest.TestCase):

    def test_gluing(self):
        # SDNF
        self.assertEqual(gluing([["!a", "b", "c"], ["a", "!b", "!c"], ["a", "!b", "c"], ["a", "b", "c"]]), [['b', 'c'], ['a', '!b'], ['a', 'c']])
        self.assertEqual(gluing([["!a", "!b", "!c"], ["a", "!b", "!c"], ["a", "b", "!c"], ["a", "b", "c"]]), [['!b', '!c'], ['a', '!c'], ['a', 'b']])
        # # SKNF
        self.assertEqual(gluing([["a", "b", "c"], ["a", "b", "!c"], ["a", "!b", "c"], ["!a", "!b", "c"]]), [['a', 'b'], ['a', 'c'], ['!b', 'c']])
        self.assertEqual(gluing([["a", "b", "!c"], ["a", "!b", "c"], ["a", "!b", "!c"], ["!a", "b", "!c"]]), [['a', '!c'], ['b', '!c'], ['a', '!b']])

    def test_calculation_method(self):
        # SDNF
        self.assertEqual(calculation_method([['b', 'c'], ['a', '!b'], ['a', 'c']], "dnf"), [["b", "c"], ["a", "!b"]])
        self.assertEqual(calculation_method([['!b', '!c'], ['a', '!c'], ['a', 'b']], "dnf"), [['!b', '!c'], ['a', 'b']])
        # # SKNF
        self.assertEqual(calculation_method([['a', 'b'], ['a', 'c'], ['!b', 'c']], "knf"), [["a", "b"], ["!b", "c"]])
        self.assertEqual(calculation_method([['a', '!c'], ['b', '!c'], ['a', '!b']], "knf"), [['b', '!c'], ['a', '!b']])

    def test_calculation_tabular_method(self):
        # SDNF
        self.assertEqual(calculation_tabular_method(
            [["b", "c"], ["a", "!b"], ["a", "c"]],
            [["!a", "b", "c"], ["a", "!b", "!c"], ["a", "!b", "c"], ["a", "b", "c"]],
            "dnf"),
            [["b", "c"], ["a", "!b"]])
        # SKNF
        self.assertEqual(calculation_tabular_method([['a', 'b'], ['a', 'c'], ['!b', 'c']],
            [["a", "b", "c"], ["a", "b", "!c"], ["a", "!b", "c"], ["!a", "!b", "c"]],
            "knf"),
            [["a", "b"], ["!b", "c"]])

    def test_tabular_method(self):
        # SDNF
        self.assertEqual(tabular_method(
            [["!a", "b", "c"], ["a", "!b", "!c"], ["a", "!b", "c"], ["a", "b", "c"]],),
            [["b", "c"], ["a", "!b"]])
        # # SKNF
        self.assertEqual(tabular_method(
            [["a", "b", "c"], ["a", "b", "!c"], ["a", "!b", "c"], ["!a", "!b", "c"]]),
            [["!b", "c"], ["a", "b"]])


if __name__ == "__main__":
    unittest.main()