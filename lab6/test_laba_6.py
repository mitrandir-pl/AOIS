import unittest
from laba_6 import HeshTable


class TestLaba(unittest.TestCase):

    def setUp(self):
        self.hesh_table_test = HeshTable()

    def test_get_value(self):
        self.assertEqual(self.hesh_table_test.get_value("Трепонемы"), 1452)
        self.assertEqual(self.hesh_table_test.get_value("Рапс"), 1188)
        self.assertEqual(self.hesh_table_test.get_value("Аброзавр"), 693)
        self.assertEqual(self.hesh_table_test.get_value("Кешью"), 1452)
        self.assertEqual(self.hesh_table_test.get_value("Гигроцибе"), 594)

    def test_get_hesh(self):
        self.assertEqual(self.hesh_table_test.get_hesh(1452, 0), 2)
        self.assertEqual(self.hesh_table_test.get_hesh(1188, 1), 9)
        self.assertEqual(self.hesh_table_test.get_hesh(693, 2), 5)
        self.assertEqual(self.hesh_table_test.get_hesh(1452, 5), 7)
        self.assertEqual(self.hesh_table_test.get_hesh(594, 6), 10)

    def test_add_element_True(self):
        self.assertTrue(self.hesh_table_test.add_element("Трепонемы", "Бактерии"))
        self.assertTrue(self.hesh_table_test.add_element("Гигроцибе", "Грибы"))
        self.assertTrue(self.hesh_table_test.add_element("Адский вампир", "Животные"))
        self.assertTrue(self.hesh_table_test.add_element("Блюдцевик", "Грибы"))
        self.assertTrue(self.hesh_table_test.add_element("Спирохеты", "Бактерии"))
        self.assertTrue(self.hesh_table_test.add_element("Кешью", "Растения"))

    def test_add_element_False(self):
        self.assertFalse(self.hesh_table_test.add_element("123123", "hello"))
        self.assertFalse(self.hesh_table_test.add_element("     ", "world"))
        self.assertFalse(self.hesh_table_test.add_element("F F G", "!!!"))
        self.assertFalse(self.hesh_table_test.add_element("_Клюква", "frfrfr"))
        self.assertFalse(self.hesh_table_test.add_element("C/ыр", "vkjrj"))

    def test_del_element_True(self):
        self.assertTrue(self.hesh_table_test.del_element("Трепонемы"))
        self.assertTrue(self.hesh_table_test.del_element("Гигроцибе"))
        self.assertTrue(self.hesh_table_test.del_element("Адский вампир"))
        self.assertTrue(self.hesh_table_test.del_element("Блюдцевик"))
        self.assertTrue(self.hesh_table_test.del_element("Спирохеты"))
        self.assertTrue(self.hesh_table_test.del_element("Кешью"))

    def test_add_element_False(self):
        self.assertFalse(self.hesh_table_test.del_element("123123"))
        self.assertFalse(self.hesh_table_test.del_element("     "))
        self.assertFalse(self.hesh_table_test.del_element("F F G"))
        self.assertFalse(self.hesh_table_test.del_element("_Клюква"))
        self.assertFalse(self.hesh_table_test.del_element("C/ыр"))


if __name__ == "__main__":
    unittest.main()