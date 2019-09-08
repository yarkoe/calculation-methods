# _*_ coding: utf-8 _*_
""" This file contains methods to search roots on the given segment.
"""


def search_root_bisection(math_function, epsilon, start, end):
    """
    This function searches root within given epsilon. Bisection method is used here.
    @param math_function: source function.
    @param epsilon: precision of found root.
    @param start: start of segment where root would be found.
    @param end: end of segment.
    @return: tuple that contains the root, a count of steps that would be needed to find the root,
    distance between the root and previous approximation, residual modulus.
    """

    a = start
    b = end

    counter = 1
    while (2 * epsilon) < abs(b - a):
        c = (a + b) / 2
        if math_function(a) * math_function(c) <= 0:
            b = c
        else:
            """ If math_function(current_segment_mid) * math_function(current_segment_end) <= 0
            """
            a = c

        counter += 1

    approximate_root = (a + b) / 2
    final_distance = abs(a - approximate_root)
    residual_modulus = abs(math_function(approximate_root))

    return approximate_root, counter, final_distance, residual_modulus


def search_root_newton(math_function, derivative, epsilon, start, end):
    """
    This function searches root within given epsilon. Newton method is used here.
    @param math_function: source function.
    @param derivative: derivative of math_function.
    @param epsilon: precision of found root.
    @param start: start of segment where root would be found.
    @param end: end of segment.
    @return: tuple that contains the root, a count of steps that would be needed to find the root,
    distance between the root and previous approximation, residual modulus.
    """

    first_point = end
    while derivative(first_point) == 0.:
        first_point = (start - first_point) / 2

    root_multiplicity = 0
    while True:
        root_multiplicity += 1

        approximate_root = first_point
        cur_function_value = math_function(approximate_root)

        counter = 1
        while cur_function_value > epsilon:
            cur_derivative_value = derivative(approximate_root)

            if cur_derivative_value == 0.:
                break

            approximate_root = approximate_root - (cur_function_value / cur_derivative_value) * root_multiplicity

            cur_function_value = math_function(approximate_root)
            counter += 1
        else:
            residual_modulus = abs(cur_function_value)

            return approximate_root, counter, residual_modulus


# TODO: realize methods: Newton method, modifiable Newton method and method of secants.
