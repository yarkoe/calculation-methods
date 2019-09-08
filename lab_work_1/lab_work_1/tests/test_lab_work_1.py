import unittest

from ..section_separator import separate_segment
from ..search_methods import find_root_bisection


class RootsSeekerTest(unittest.TestCase):

    def setUp(self):
        self.__test_function = lambda x: x ** 2 - 1

        self.__test_segment = (-2, 2)
        self.__test_step = (self.__test_segment[1] - self.__test_segment[0]) / 100
        self.__test_eps = 0.001

    def test_bisection_method(self):
        segments = separate_segment(self.__test_function, self.__test_step, *self.__test_segment)

        self.assertEqual(len(segments), 2)

        roots = []
        for segment in segments:
            roots.append(find_root_bisection(self.__test_function, self.__test_eps, *segment)[0])

        self.assertAlmostEqual(roots[0], -1, delta=self.__test_eps)


if __name__ == '__main__':
    unittest.main()
