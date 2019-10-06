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