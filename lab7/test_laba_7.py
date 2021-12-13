import unittest
from laba_7 import get_random_word, nearest, recursive_find


class TestCase(unittest.TestCase):

    def test_recursive_find(self):
        self.assertEqual(recursive_find("11111111", "11111111", 0, 0), {"trigger_left" : False, "trigger_right" : False})
        self.assertEqual(recursive_find("11111110", "11111111", 0, 0), {"trigger_left" : False, "trigger_right" : True})
        self.assertEqual(recursive_find("10000000", "01111111", 0, 7), {"trigger_left" : True, "trigger_right" : False})
        self.assertEqual(recursive_find("11111110", "11111111", 0, 0), {"trigger_left" : False, "trigger_right" : True})
        self.assertEqual(recursive_find("11111110", "11111111", 0, 0), {"trigger_left" : False, "trigger_right" : True})
        self.assertEqual(recursive_find("11111111", "11111111", 0, 0), {"trigger_left" : False, "trigger_right" : False})
        self.assertEqual(recursive_find("11111110", "11111111", 0, 0), {"trigger_left" : False, "trigger_right" : True})
        self.assertEqual(recursive_find("10000000", "01111111", 0, 7), {"trigger_left" : True, "trigger_right" : False})
        self.assertEqual(recursive_find("11111110", "11111111", 0, 0), {"trigger_left" : False, "trigger_right" : True})
        self.assertEqual(recursive_find("11111110", "11111111", 0, 0), {"trigger_left" : False, "trigger_right" : True})
        self.assertEqual(recursive_find("11111111", "11111111", 0, 0), {"trigger_left" : False, "trigger_right" : False})
        self.assertEqual(recursive_find("11111110", "11111111", 0, 0), {"trigger_left" : False, "trigger_right" : True})
        self.assertEqual(recursive_find("10000000", "01111111", 0, 7), {"trigger_left" : True, "trigger_right" : False})
        self.assertEqual(recursive_find("11111110", "11111111", 0, 0), {"trigger_left" : False, "trigger_right" : True})
        self.assertEqual(recursive_find("11111110", "11111111", 0, 0), {"trigger_left" : False, "trigger_right" : True})
        self.assertEqual(recursive_find("11111111", "11111111", 0, 0), {"trigger_left" : False, "trigger_right" : False})
        self.assertEqual(recursive_find("11111110", "11111111", 0, 0), {"trigger_left" : False, "trigger_right" : True})
        self.assertEqual(recursive_find("10000000", "01111111", 0, 7), {"trigger_left" : True, "trigger_right" : False})
        self.assertEqual(recursive_find("11111110", "11111111", 0, 0), {"trigger_left" : False, "trigger_right" : True})
        self.assertEqual(recursive_find("11111110", "11111111", 0, 0), {"trigger_left" : False, "trigger_right" : True})

    
    