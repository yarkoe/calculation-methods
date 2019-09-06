# _*_ coding: utf-8 _*_
""" This file contains methods to search roots on the given segment.
"""


def find_root_bisection(math_function, eps, start, end):
    """
    This function finds root to within given epsilon.
    @param math_function: source function.
    @param eps: precision of found root.
    @param start: start of segment when root would be found.
    @param end: end of segment.
    @return: tuple that contains the root, a count of steps that would be needed to find the root,
    distance between the root and previous approximation, residual modulus.
    """

    current_segment_start = start
    current_segment_end = end

    counter = 0
    while abs(current_segment_end - current_segment_start) < 2 * eps:
        current_segment_mid = (current_segment_end - current_segment_start) / 2
        if math_function(current_segment_start) * math_function(current_segment_mid) <= 0:
            current_segment_end = current_segment_mid
        else:
            """ If math_function(current_segment_mid) * math_function(current_segment_end) <= 0
            """
            current_segment_start = current_segment_mid

        counter += 1

    approximate_root = (current_segment_end - current_segment_start) / 2
    final_distance = abs(current_segment_start - approximate_root)
    residual_modulus = abs(math_function(approximate_root))
 
    return approximate_root, (counter + 1), final_distance, residual_modulus


# TODO: realize methods: Newton method, modifiable Newton method and method of secants.
