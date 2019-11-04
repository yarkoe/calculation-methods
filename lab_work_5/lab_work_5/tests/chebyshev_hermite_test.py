import unittest

from ..orthogonal_polynomials.chebyshev_hermite_polynomial import create_chebyshev_hermite_polynomial_coefficients


class TestChebyshevHermitePolynomial(unittest.TestCase):
    def setUp(self):
        self.test_set = {
            "coefficients_0degree": [1, ],
            "coefficients_2degree": [-2, 0, 4],
            "coefficients_5degree": [0, -120, 0, 160, 0, -32]
        }

    def test_polynomial_coefficients_creation_0degree(self):
        coefficients_list = create_chebyshev_hermite_polynomial_coefficients(0)

        self.assertEqual(self.test_set["coefficients_0degree"], coefficients_list)

    def test_polynomial_coefficients_creation_2degree(self):
        coefficients_list = create_chebyshev_hermite_polynomial_coefficients(2)

        self.assertEqual(self.test_set["coefficients_2degree"], coefficients_list)

    def test_polynomial_coefficients_creation_5degree(self):
        coefficients_list = create_chebyshev_hermite_polynomial_coefficients(5)

        self.assertEqual(self.test_set["coefficients_5degree"], coefficients_list)
