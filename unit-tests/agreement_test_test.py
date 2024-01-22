import unittest
from uncertainties import ufloat
from pylib.DataAnalysis import *


class agreement_test_test(unittest.TestCase):
    def test_agreement_test_1(self):
        output = agreement_test(ufloat(0, 0), ufloat(0, 0))
        self.assertTrue(output)

    def test_agreement_test_2(self):
        output = agreement_test(ufloat(0, 0), ufloat(1, 0))
        self.assertFalse(output)

    def test_agreement_test_3(self):
        output = agreement_test(ufloat(0, 1), ufloat(1, 1))
        self.assertTrue(output)

    def test_agreement_test_4(self):
        output = agreement_test(ufloat(0, 10), ufloat(10000, 10))
        self.assertFalse(output)
