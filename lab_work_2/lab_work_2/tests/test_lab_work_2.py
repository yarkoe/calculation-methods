import unittest
import math

from ..table_operations import create_table, sort_table
from ..polynomial_functions import create_lagrangian_form, create_newton_form


class TestPolynomialFunctions(unittest.TestCase):
    def setUp(self):
        self.test_set_1 = {
            "function": lambda x: 2 * math.sin(x) - x / 2,
            "start": 0.2,
            "end": 0.7,
            "x": 0.35,
            "n": 7,
            "m": 15
        }

        self.test_table_1 = create_table(*(self.test_set_1[el] for el in ("function", "m", "start", "end")))
        self.test_table_1 = sort_table(self.test_table_1, self.test_set_1["x"])

    def test_lagrangian_form(self):
        lagrangian_form = create_lagrangian_form(self.test_table_1, self.test_set_1["n"])

        for i in range(self.test_set_1["n"] + 1):
            self.assertAlmostEqual(self.test_table_1[i][1], lagrangian_form(self.test_table_1[i][0]))

    def test_newton_form(self):
        newton_form = create_newton_form(self.test_table_1, self.test_set_1["n"])

        for i in range(self.test_set_1["n"] + 1):
            self.assertAlmostEqual(self.test_table_1[i][1], newton_form(self.test_table_1[i][0]))
