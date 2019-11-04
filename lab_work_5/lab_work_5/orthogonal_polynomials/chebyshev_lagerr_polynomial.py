def create_chebyshev_lagerr_polynomial_coefficients(alpha, n):
    """
    Creates x^(-alpha) * e^x * d^n(x^(alpha + n) * e^(-x))/d(x^n) polynomial coefficients and returns it.
    @param alpha: Chebyshev-Lagerr polynomial value.
    @param n: degree of derivative.
    @return: list of polynomial coefficients.
    """

    coefficients_list = [0] * (alpha + n + 1)
    coefficients_list[-1] = 1

    for i in range(1, n + 1):
        pred_coefficients_list = coefficients_list.copy()

        coefficients_list = [0] * (alpha + n + 1)
        for j in range(alpha, alpha + n + 1):
            if j != 0:
                coefficients_list[j - 1] += pred_coefficients_list[j] * j

            coefficients_list[j] += pred_coefficients_list[j] * (-1)

    # divide by x^alpha
    for i in range(n + 1):
        coefficients_list[i] = coefficients_list[i + alpha]

    coefficients_list = coefficients_list[:n + 1]

    return coefficients_list
