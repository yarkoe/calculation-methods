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

    step_counter = 1
    while abs(b - a) > (2 * epsilon):
        c = (a + b) / 2
        if math_function(a) * math_function(c) <= 0:
            b = c
        else:
            """ If math_function(current_segment_mid) * math_function(current_segment_end) <= 0
            """
            a = c

        step_counter += 1

    approximate_root = (a + b) / 2
    final_distance = abs(a - approximate_root)
    residual_modulus = abs(math_function(approximate_root))

    return approximate_root, step_counter, final_distance, residual_modulus


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

        pred_approximate_root = first_point
        new_approximate_root = pred_approximate_root - \
                               (math_function(pred_approximate_root) / derivative(pred_approximate_root)) * \
                               root_multiplicity

        step_counter = 1
        while abs(new_approximate_root - pred_approximate_root) > epsilon:
            pred_approximate_root = new_approximate_root

            pred_derivative_value = derivative(pred_approximate_root)

            if pred_derivative_value == 0.:
                break

            new_approximate_root = pred_approximate_root - \
                                   (math_function(pred_approximate_root) / pred_derivative_value) *\
                                   root_multiplicity

            step_counter += 1
        else:
            residual_modulus = abs(math_function(new_approximate_root))
            final_distance = abs(new_approximate_root - pred_approximate_root)

            return new_approximate_root, step_counter, final_distance, residual_modulus, first_point


def search_root_modifiable_newton(math_function, derivative, epsilon, start, end):
    """
    This function searches root within given epsilon. Modifiable newton method is used here.
    @param math_function: source function.
    @param derivative: derivative of math_function.
    @param epsilon: precision of found root.
    @param start: start of segment where root would be found.
    @param end: end of segment.
    @return: tuple that contains the root, a count of steps that would be needed to find the root,
    distance between the root and previous approximation, residual modulus.
    """

    first_point = end
    first_derivative_value = derivative(first_point)
    while first_derivative_value == 0.:
        first_point = (start - first_point) / 2

        first_derivative_value = derivative(first_point)

    root_multiplicity = 0
    while True:
        root_multiplicity += 1

        pred_approximate_root = first_point
        new_approximate_root = pred_approximate_root - \
                               (math_function(pred_approximate_root) / first_derivative_value) * \
                               root_multiplicity

        step_counter = 1
        while abs(new_approximate_root - pred_approximate_root) > epsilon:
            pred_approximate_root = new_approximate_root

            new_approximate_root = pred_approximate_root - \
                                   (math_function(pred_approximate_root) / first_derivative_value) * \
                                   root_multiplicity

            step_counter += 1
        else:
            final_distance = abs(new_approximate_root - pred_approximate_root)
            residual_modulus = abs(math_function(new_approximate_root))

            return new_approximate_root, step_counter, final_distance, residual_modulus, first_point


def search_root_secants_method(math_function, epsilon, start, end):
    """
    This function searches root within given epsilon. Modifiable newton method is used here.
    @param math_function: source function.
    @param epsilon: precision of found root.
    @param start: start of segment where root would be found.
    @param end: end of segment.
    @return: tuple that contains the root, a count of steps that would be needed to find the root,
    distance between the root and previous approximation, residual modulus.
    """

    pred_approximate_root = start
    new_approximate_root = end

    step_counter = 1
    while abs(new_approximate_root - pred_approximate_root) > epsilon:
        new_function_value = math_function(new_approximate_root)

        temp_new_approximate_root = new_approximate_root
        new_approximate_root = new_approximate_root - new_function_value * \
                               (new_approximate_root - pred_approximate_root) / \
                               (new_function_value - math_function(pred_approximate_root))

        pred_approximate_root = temp_new_approximate_root

        step_counter += 1

    final_distance = abs(new_approximate_root - pred_approximate_root)
    residual_modulus = abs(math_function(new_approximate_root))

    return new_approximate_root, step_counter, final_distance, residual_modulus
