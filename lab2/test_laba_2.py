import unittest
from laba_2 import LogicFunction


class TestLaba(unittest.TestCase):

    def setUp(self):
        self.A = LogicFunction("!((!a+b)*!(b*c))")
        self.B = LogicFunction("!((!a+!b)*!(!b*!c))")
        self.C = LogicFunction("!((!a+b)*!(b*!c))")
        self.D = LogicFunction("!((a+b)*!(b*!c))")
        self.E = LogicFunction("!((a+b)*!(!b*c))")

    def test_init(self):
        self.assertEqual(self.A.sdnf, "!a*b*c + a*!b*!c + a*!b*c + a*b*c")
        self.assertEqual(self.A.sknf, "(a+b+c) * (a+b+!c) * (a+!b+c) * (!a+!b+c)")
        self.assertEqual(self.A.bin_num_sdnf, "011+100+101+111")
        self.assertEqual(self.A.bin_num_sknf, "111*110*101*001")

        self.assertEqual(self.B.sdnf, "!a*!b*!c + a*!b*!c + a*b*!c + a*b*c")
        self.assertEqual(self.B.sknf, "(a+b+!c) * (a+!b+c) * (a+!b+!c) * (!a+b+!c)")
        self.assertEqual(self.B.bin_num_sdnf, "000+100+110+111")
        self.assertEqual(self.B.bin_num_sknf, "110*101*100*010")

        self.assertEqual(self.C.sdnf, "!a*b*!c + a*!b*!c + a*!b*c + a*b*!c")
        self.assertEqual(self.C.sknf, "(a+b+c) * (a+b+!c) * (a+!b+!c) * (!a+!b+!c)")
        self.assertEqual(self.C.bin_num_sdnf, "010+100+101+110")
        self.assertEqual(self.C.bin_num_sknf, "111*110*100*000")

        self.assertEqual(self.D.sdnf, "!a*!b*!c + !a*!b*c + !a*b*!c + a*b*!c")
        self.assertEqual(self.D.sknf, "(a+!b+!c) * (!a+b+c) * (!a+b+!c) * (!a+!b+!c)")
        self.assertEqual(self.D.bin_num_sdnf, "000+001+010+110")
        self.assertEqual(self.D.bin_num_sknf, "100*011*010*000")

        self.assertEqual(self.E.sdnf, "!a*!b*!c + !a*!b*c + a*!b*c")
        self.assertEqual(self.E.sknf, "(a+!b+c) * (a+!b+!c) * (!a+b+c) * (!a+!b+c) * (!a+!b+!c)")
        self.assertEqual(self.E.bin_num_sdnf, "000+001+101")
        self.assertEqual(self.E.bin_num_sknf, "101*100*011*001*000")
