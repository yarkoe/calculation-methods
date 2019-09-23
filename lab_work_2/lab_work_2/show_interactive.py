import math

from .table_operations import create_table, sort_table
from .polynomial_functions import create_lagrangian_form, create_newton_form


def show_table(table):
    print("Номер: Узел | Значение функции в узле")
    for i in range(len(table)):
        print("{}: {} | {}".format(i, table[i][0], table[i][1]))


def show_algebraic_interpolation():
    """
    Show program functions.
    @return: void
    """

    print("Лабораторная работа № 2")
    print("Вариант № 7")
    print("Задача алгебраического интерполирования.")
    print("Интерполяционный многочлен в форме Ньютона и в форме Лагранжа.\n")

    # def function(x):
    #     return 2 * math.sin(x) - x / 2

    def function(x):
        return math.sqrt(1 + x ** 2)

    start = 0.
    end = 0.7

    print("Вид фукнции: f(x) = x*sin(x) - x/2")
    print("A= {}, B= {}\n".format(start, end))

    while True:
        try:
            m_plus = int(input("Введите число значений в таблице: "))
            break
        except ValueError:
            print("Неверный формат")

    while True:
        try:
            x = float(input("Введите точку интерполирования: "))
            break
        except ValueError:
            print("Неверный формат")

    while True:
        try:
            n = int(input("Введите степень интерполяции многочлена: "))

            if n < m_plus:
                break

            print("Введено недопустимое значение n")
        except ValueError:
            print("Неверный формат")

    print("")
    print("Число значений в таблице: {}".format(m_plus))
    print("Исходная таблица значений функции:")
    table = create_table(function, m_plus, start, end)
    show_table(table)
    print("")

    print("Точка интерполирования: {}".format(x))
    print("Степень многочлена: {}".format(n))

    if n < (m_plus - 1):
        table = sort_table(table, x)

    print("Отсортированная таблица:")
    show_table(table)
    print("")

    lagrangian_form = create_lagrangian_form(table, n)
    lagrangian_form_x = lagrangian_form(x)
    print("Значение интерполяционного многочлена, найденное при помощи представления в форме Лагранжа:")
    print("{}".format(lagrangian_form_x))
    print("Значение абсолютной фактической погрешности для формы Лагранжа:")
    print("{}\n".format(abs(lagrangian_form_x - function(x))))

    newton_form = create_newton_form(table, n)
    print("Значение интерполяционного многочлена, найденное при помощи представления в форме Ньютона:")
    newton_form_x = newton_form(x)
    print("{}".format(newton_form_x))
    print("Значение абсолютной фактической погрешности для формы Ньютона:")
    print("{}".format(abs(newton_form_x - function(x))))

