def create_legendre_polynomial(n):
    """
    Creates Legendre polynomial of degree n recursively.
    @param n: degree of polynomial.
    @return: Legendre polynomial.
    """

    if n == 0:
        return lambda x: 1
    elif n == 1:
        return lambda x: x
    else:
        # Pn = (2n-1)/n * x * Pn-1(x) - (n-1)/n * Pn-2(x)
        return lambda x: (2 * n - 1) / n * x * create_legendre_polynomial(n - 1)(x) - \
                         (n - 1) / n * create_legendre_polynomial(n - 2)(x)
