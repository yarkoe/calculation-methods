def create_chebyshev_polynomial(n):
    """
    Creates Chebyshev polynomial of degree n recursively.
    @param n: degree of polynomial.
    @return: Chebyshev polynomial.
    """

    if n == 0:
        return lambda x: 1
    elif n == 1:
        return lambda x: x
    else:
        # Tn(x) = 2 * x * Tn-1(x) - Tn-2(x), n = 2, 3, ...
        return lambda x: 2 * x * create_chebyshev_polynomial(n - 1)(x) - create_chebyshev_polynomial(n - 2)(x)


def create_chebyshev_reduced_polynomial(n):
    """
    Creates Chebyshev reduced polynomial of degree n recursively.
    @param n: degree of polynomial.
    @return: Chebyshev reduced polynomial.
    """

    return lambda x: create_chebyshev_polynomial(n)(x) / (2 ** n)
