import unittest
import math

from ..table_operations import create_table, sort_table
from ..polynomial_functions import create_lagrangian_form


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

    def test_lagrangian_form(self):
        table = create_table(*(self.test_set_1[el] for el in ("function", "m", "start", "end")))
        table = sort_table(table, self.test_set_1["x"])

        lagrangian_form = create_lagrangian_form(table, self.test_set_1["n"])

        for i in range(self.test_set_1["n"] + 1):
            self.assertAlmostEqual(table[i][1], lagrangian_form(table[i][0]))
