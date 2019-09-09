import unittest
import math

from ..section_separator import separate_segment
from ..search_methods import search_root_bisection, search_root_newton, \
                             search_root_modifiable_newton, search_root_secants_method


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

    def test_modifiable_newton_method(self):

        roots = []
        for segment in self.segments:
            roots.append(search_root_modifiable_newton(self.quadratic_function,
                                                       self.derivative, self.test_eps, *segment)[0])

        self.assertAlmostEqual(roots[0], -1, delta=self.test_eps)
        self.assertAlmostEqual(roots[1], 1, delta=self.test_eps)

    def test_secants_method(self):

        roots = []
        for segment in self.segments:
            roots.append(search_root_secants_method(self.quadratic_function, self.test_eps, *segment)[0])

        self.assertAlmostEqual(roots[0], -1, delta=self.test_eps)
        self.assertAlmostEqual(roots[1], 1, delta=self.test_eps)


class TestTrigonometricEquation(unittest.TestCase):

    def setUp(self):
        self.trigonometric_function = lambda x: x * math.sin(x) - 1
        self.derivative = lambda x: math.sin(x) + x * math.cos(x)

        self.test_segment = (-10, 2)
        self.test_step = (self.test_segment[1] - self.test_segment[0]) / 100
        self.test_eps = 10 ** (-5)

        self.segments = separate_segment(self.trigonometric_function, self.test_step, *self.test_segment)

        self.assertEqual(len(self.segments), 5)

    def test_bisection_method(self):
        roots = []
        for segment in self.segments:
            roots.append(search_root_bisection(self.trigonometric_function, self.test_eps, *segment)[0])

        self.assertAlmostEqual(roots[0], -9.31724, delta=self.test_eps)
        self.assertAlmostEqual(roots[1], -6.43911, delta=self.test_eps)

    def test_newton_method(self):
        roots = []
        for segment in self.segments:
            roots.append(search_root_newton(self.trigonometric_function, self.derivative, self.test_eps, *segment)[0])

        self.assertAlmostEqual(roots[0], -9.31724, delta=self.test_eps)
        self.assertAlmostEqual(roots[1], -6.43911, delta=self.test_eps)

    def test_modifiable_newton_method(self):

        roots = []
        for segment in self.segments:
            roots.append(search_root_modifiable_newton(self.trigonometric_function,
                                                       self.derivative, self.test_eps, *segment)[0])

        self.assertAlmostEqual(roots[0], -9.31724, delta=self.test_eps)
        self.assertAlmostEqual(roots[1], -6.43911, delta=self.test_eps)

    def test_secants_method(self):

        roots = []
        for segment in self.segments:
            roots.append(search_root_secants_method(self.trigonometric_function, self.test_eps, *segment)[0])

        self.assertAlmostEqual(roots[0], -9.31724, delta=self.test_eps)
        self.assertAlmostEqual(roots[1], -6.43911, delta=self.test_eps)


if __name__ == '__main__':
    unittest.main()
