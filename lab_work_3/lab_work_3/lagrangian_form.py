def create_lagrangian_form(table, polynomial_degree):
    """
    Creates polynomial in the Lagrangian form.
    @param table: list of (node, function_value) tuples.
    @param polynomial_degree: the degree of the polynomial that should be created.
    @return: approximating polynomial function.
    """

    def z(x, k):
        result = 1
        for i in range(polynomial_degree + 1):
            if i == k:
                continue

            result *= x - table[i][0]

        return result

    def l(x, k):
        return z(x, k) / z(table[k][0], k)

    def p(x):
        sum = 0
        for k in range(polynomial_degree + 1):
            sum += l(x, k) * table[k][1]

        return sum

    return p