def differentiate_first(f_a, f_a_n, f_a_nn, h):
    """
    Returns approximate differentiation of first value.
    @param f_a: function(a).
    @param f_a_n: function(a + h).
    @param f_a_nn: function(a + 2h).
    @param h: step between two args.
    @return: approximate differentiation of the first value (function'(a)).
    """

    return (-3 * f_a + 4 * f_a_n - f_a_nn) / (2 * h)


def differentiate_center(f_a_n, f_a_p, h):
    """
    Returns approximate differentiation of center values.
    @param f_a_n: function(a + h).
    @param f_a_p: function(a - h).
    @param h: step between two args.
    @return: approximate differentiation of the center values (function'(a))
    """

    return (f_a_n - f_a_p) / (2 * h)


def differentiate_last(f_a, f_a_p, f_a_pp, h):
    """
    Returns approximate differentiation of last value.
    @param f_a: function(a).
    @param f_a_p: function(a - h).
    @param f_a_pp: function(a - 2h).
    @param h: step between two args.
    @return: approximate differentiation of the last value (function'(a)).
    """

    return (3 * f_a - 4 * f_a_p + f_a_pp) / (2 * h)


def differentiate_center_twice(f_a, f_a_n, f_a_p, h):
    """
    Returns approximate twin differentiation of center values.
    @param f_a: function(a).
    @param f_a_n: function(a + h).
    @param f_a_p: function(a - h).
    @param h: step between two args.
    @return: approximate twin differentiation of the center values (function''(a)).
    """

    return (f_a_n - 2 * f_a + f_a_p) / h**2


