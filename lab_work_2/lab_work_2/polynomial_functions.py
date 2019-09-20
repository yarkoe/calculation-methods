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


def create_newton_form(table, polynomial_degree):
    """
    Creates polynomial in the Newton form.
    @param table: list of (node, function_value) tuples.
    @param polynomial_degree: the degree of the polynomial that should be created.
    @return: approximating polynomial function.
    """

    divided_differences_table = [tuple(table[i][1] for i in range(polynomial_degree + 1)), ]

    for i in range(1, polynomial_degree + 1):
        divided_differences_table.append(
            tuple((divided_differences_table[i-1][j + 1] - divided_differences_table[i-1][j]) /
                  (table[j + i][0] - table[j][0]) for j in range(polynomial_degree + 1 - i)))

    def w(x, k):
        result = 1
        for i in range(k):
            result *= x - table[i][0]

        return result

    def p(x):
        sum = 0
        for i in range(polynomial_degree + 1):
            sum += divided_differences_table[i][0] * w(x, i)

        return sum

    return p
