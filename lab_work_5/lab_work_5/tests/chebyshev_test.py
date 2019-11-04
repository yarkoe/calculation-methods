import unittest
import math

from ..orthogonal_polynomials.сhebyshev_polynomial import create_chebyshev_polynomial


class TestChebyshevPolynomial(unittest.TestCase):
    def setUp(self):
        self.test_set = {
            "test1": {"n": 2, "x": 1, "value": 1},
            "test2": {"n": 5, "x": -1, "value": -1},
            "test3": {"n": 4, "x": math.cos(math.pi / 2), "value": 1}
        }

    def test_polynomial_creation1(self):
        polynomial = create_chebyshev_polynomial(self.test_set["test1"]["n"])

        polynomial_value = polynomial(self.test_set["test1"]["x"])
        self.assertAlmostEqual(self.test_set["test1"]["value"], polynomial_value)

    def test_polynomial_creation2(self):
        polynomial = create_chebyshev_polynomial(self.test_set["test2"]["n"])

        polynomial_value = polynomial(self.test_set["test2"]["x"])
        self.assertAlmostEqual(self.test_set["test2"]["value"], polynomial_value)

    def test_polynomial_creation3(self):
        polynomial = create_chebyshev_polynomial(self.test_set["test3"]["n"])

        polynomial_value = polynomial(self.test_set["test3"]["x"])
        self.assertAlmostEqual(self.test_set["test3"]["value"], polynomial_value)
