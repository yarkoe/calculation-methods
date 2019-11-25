import math

import matplotlib.pyplot as plt
import numpy as np

from lab_work_5.lab_work_5 import bisection_method
from lab_work_5.lab_work_5.orthogonal_polynomials.legendre_polynomial import create_legendre_polynomial
from lab_work_5.lab_work_5.orthogonal_polynomials.сhebyshev_polynomial import create_chebyshev_polynomial, \
    create_chebyshev_reduced_polynomial
from lab_work_5.lab_work_5.orthogonal_polynomials.chebyshev_hermite_polynomial \
    import create_chebyshev_hermite_polynomial
from lab_work_5.lab_work_5.orthogonal_polynomials.chebyshev_lagerr_polynomial import create_chebyshev_lagerr_polynomial
from lab_work_5.lab_work_5.section_separator import separate_segment


length_step = 1. / 100
epsilon = 10 ** -5


def input_int(message):
    while True:
        try:
            int_value = int(input(message))
            if int_value < 0:
                print("Значение должно быть больше или равен 0")
                continue
            break
        except ValueError:
            print("Неверный формат")

    return int_value


def show_polynomial(polynomial_name, polynomial, section):
    polynomial_roots_segments = separate_segment(polynomial, length_step, *section)

    print("Приблизительные корни многочлена на отрезке [{}, {}]".format(*section))
    for i in range(len(polynomial_roots_segments)):
        cur_root = bisection_method.search_root_bisection(polynomial, epsilon, *polynomial_roots_segments[i])[0]
        print(cur_root)

    x = np.linspace(*section, 200)
    y = np.array([polynomial(xi) for xi in x])

    plt.plot(x, y, label=polynomial_name)
    plt.title(polynomial_name)
    plt.legend()


def show_legendre_polynomial(n):
    print("Многочлен Лежандра\n")

    section = [-1, 1]

    legendre_polynomial = create_legendre_polynomial(n)

    show_polynomial('Многочлен Лежандра', legendre_polynomial, section)
    plt.show()


def show_chebyshev_polynomial(n):
    print("Многочлен Чебышёва первого рода\n")
    section = [-1, 1]

    chebyshev_polynomial = create_chebyshev_polynomial(n)

    print("Точки экстремума:")
    for l in range(n + 1):
        print(math.cos(math.pi * l / n))

    show_polynomial("Многочлен Чебышёва первого рода", chebyshev_polynomial, section)


def show_chebyshev_reduced_polynomial(n):
    print("Приведённый многочлен Чебышёва первого рода\n")
    section = [-1, 1]

    chebyshev_reduced_polynomial = create_chebyshev_reduced_polynomial(n)
    x = np.linspace(*section, 200)
    y = np.array([chebyshev_reduced_polynomial(xi) for xi in x])
    plt.plot(x, y, label="Приведённый многочлен Чебышёва первого рода")
    plt.legend()
    plt.show()


def show_chebyshev_hermite_polynomial(n):
    print("Многочлен Чебышёва-Эрмита\n")
    section = [-5, 5]

    chebyshev_hermite_polynomial = create_chebyshev_hermite_polynomial(n)
    show_polynomial("Многочлен Чебышёва-Эрмита", chebyshev_hermite_polynomial, section)
    plt.show()


def show_chebyshev_lagerr_polynomial(alpha, n):
    print("Многочлен Чебышёва-Лагерра\n")
    section = [0, 20]

    chebyshev_lagerr_polynomial = create_chebyshev_lagerr_polynomial(alpha, n)
    show_polynomial("Многочлен Чебышёва-Лагерра", chebyshev_lagerr_polynomial, section)
    plt.show()


if __name__ == "__main__":
    print("Лабораторная работа № 5\n")
    print("Классические ортогональные многочлены\n")
    n = input_int("Введите степень многочлена: ")

    show_legendre_polynomial(n)
    print()
    show_chebyshev_polynomial(n)
    print()
    show_chebyshev_reduced_polynomial(n)
    print()
    show_chebyshev_hermite_polynomial(n)
    print()
    alpha = input_int("Введите занчение alpha: ")
    show_chebyshev_lagerr_polynomial(alpha, n)
