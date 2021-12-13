import unittest
from laba_8 import AsocMemory


class TestLaba(unittest.TestCase):

    def setUp(self):
        self.table = AsocMemory()

    def test_print_table(self):
        self.assertTrue(self.table.print_table())
        self.assertTrue(self.table.print_table())
        self.assertTrue(self.table.print_table())


    def test_add_element_true(self):
        self.assertTrue(self.table.add_element("1111111111111111"))
        self.assertTrue(self.table.add_element("0011111111001111"))
        self.assertTrue(self.table.add_element("0000000000000000"))
        self.assertTrue(self.table.add_element("1111111100000000"))
        self.assertTrue(self.table.add_element("1010110111011010"))


    def test_add_element_false(self):
        self.assertFalse(self.table.add_element("qfojnqofn"))
        self.assertFalse(self.table.add_element(12121212121))
        self.assertFalse(self.table.add_element("wfnkfwjwfjjfebfjjefjefwj"))
        self.assertFalse(self.table.add_element(11111111111111111))
        self.assertFalse(self.table.add_element("mfkmfkmfkmfkm"))


    def test_ariphmetics(self):
        self.assertTrue(self.table.ariphmetics())
        self.assertTrue(self.table.ariphmetics())
        self.assertTrue(self.table.ariphmetics())


if __name__ == '__main__':
    unittest.main()
