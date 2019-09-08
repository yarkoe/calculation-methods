import unittest

from ..section_separator import separate_segment
from ..search_methods import search_root_bisection, search_root_newton


class TestQuadraticEquation(unittest.TestCase):

    def setUp(self):
        self.quadratic_function = lambda x: x ** 2 - 1
        self.derivative = lambda x: 2 * x

        self.test_segment = (-2, 2)
        self.test_step = (self.test_segment[1] - self.test_segment[0]) / 100
        self.test_eps = 0.001

        self.segments = separate_segment(self.quadratic_function, self.test_step, *self.test_segment)

        self.assertEqual(len(self.segments), 2)

    def test_bisection_method(self):
        roots = []
        for segment in self.segments:
            roots.append(search_root_bisection(self.quadratic_function, self.test_eps, *segment)[0])

        self.assertAlmostEqual(roots[0], -1, delta=self.test_eps)
        self.assertAlmostEqual(roots[1], 1, delta=self.test_eps)

    def test_newton_method(self):

        roots = []
        for segment in self.segments:
            roots.append(search_root_newton(self.quadratic_function, self.derivative, self.test_eps, *segment)[0])

        self.assertAlmostEqual(roots[0], -1, delta=self.test_eps)
        self.assertAlmostEqual(roots[1], 1, delta=self.test_eps)


if __name__ == '__main__':
    unittest.main()
