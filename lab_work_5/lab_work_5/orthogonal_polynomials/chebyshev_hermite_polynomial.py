def create_chebyshev_hermite_polynomial(n):
    """
    Creates Chebyshev-Hermite polynomial of degree on recursively.
    @param n: degree of polynomial.
    @return: Chebyshev-Hermite polynomial.
    """

    coefficient_list = create_chebyshev_hermite_polynomial_coefficients(n)
    additive = 1 if n % 2 == 0 else -1

    # returns function Hn(x) = (-1)^n * (coeff[0]*1 + coeff[1]*x + coeff[2]*x**2 + ... + coeff[n+1]*x**(n+1))
    return lambda x: additive * sum((x ** j * coefficient_list[j] for j in range(n + 1)))


def create_chebyshev_hermite_polynomial_coefficients(n):
    """
    Creates e^(x^2) * d^n(e ^ (-x^2))/d(x^n) polynomial coefficients and returns it.
    @param n: degree of derivative.
    @return: list of polynomial coefficients.
    """

    coefficients_list = [1, ]
    for i in range(1, n + 1):
        pred_coefficients_list = coefficients_list.copy()
        pred_coefficients_list.append(0)

        coefficients_list = [0] * len(pred_coefficients_list)
        for j in range(1, len(coefficients_list)):
            coefficients_list[j - 1] += pred_coefficients_list[j] * j
            coefficients_list[j] += pred_coefficients_list[j - 1] * -2

    return coefficients_list


