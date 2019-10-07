import math

from .table_operations import create_table, sort_table, change_columns, segment_between_value
from .lagrangian_form import create_lagrangian_form
from .section_separator import separate_segment
from .bisection_method import search_root_bisection


def print_table(table):
    print("Номер: Узел | Значение функции в узле")
    for i in range(len(table)):
        print("{}: {} | {}".format(i, table[i][0], table[i][1]))


def display_first_method(math_function, table, function_value, polynomial_degree):
    print("Способ № 1: обмен столбцов таблицы местами.\n")

    changed_table = change_columns(table)

    if polynomial_degree < len(table) - 1:
        changed_table = sort_table(change_columns(table), function_value)
        print("Отсортированная изменённая таблица: ")
        print_table(changed_table)
        print("")

    inverse_lagrangian_form = create_lagrangian_form(changed_table, polynomial_degree)
    argument = inverse_lagrangian_form(function_value)

    print("Значение аргумента по заданному параметру F: {}".format(argument))
    print("Значение модуля невязки: {}".format(abs(math_function(argument) - function_value)))


def display_second_method(math_function, table, function_value, polynomial_degree, epsilon, start, end):
    print("Способ № 2: нахождение корней уравнения Pn(x) - F.\n")

    a, b = segment_between_value(table, function_value)
    print("Аргументы отрезка, в котором находится значение функции F: {}, {}\n".format(a, b))

    if polynomial_degree < len(table) - 1:
        table = sort_table(table, (a + b) / 2.)
        print("Отсортированная таблица: ")
        print_table(table)

    lagrangian_form = create_lagrangian_form(table, polynomial_degree)

    def diff_function(x):
        return lagrangian_form(x) - function_value

    segments = separate_segment(diff_function, (end - start) / 100, start, end)

    for segment in segments:
        print("")
        print("Рассматриваемый отрезок, где находится корень Pn(x) - F: [{}, {}]".format(*segment))
        approximate_node = search_root_bisection(diff_function, epsilon, *segment)[0]

        print("Приближённый узел: {}".format(approximate_node))
        print("Модуль невязки: {}".format(abs(math_function(approximate_node) - function_value)))


def display_inverse_interpolation():
    """
    Displays inverse interpolation exercise interactively to console.
    @return: void.
    """

    def function(x):
        return 2 * math.sin(x) - x / 2

    start = 0
    end = 1
    print("Вид фукнции: f(x) = 2*sin(x) - x/2")
    print("A= {}, B= {}\n".format(start, end))

    while True:
        try:
            m_plus = int(input("Введите число значений в таблице: "))
            break
        except ValueError:
            print("Неверный формат")

    print("")
    print("Исходная таблица значений функции:")
    table = create_table(function, m_plus - 1, start, end)
    print_table(table)
    print("")

    while True:
        try:
            function_value = float(input("Введите параметр задачи F: "))
            break
        except ValueError:
            print("Неверный формат")

    while True:
        try:
            n = int(input("Введите степень интерполяции многочлена (число, не превосходящее {}): ".format(m_plus - 1)))

            if n < m_plus:
                break

            print("Введено недопустимое значение n")
        except ValueError:
            print("Неверный формат")

    display_first_method(function, table, function_value, n)

    while True:
        try:
            epsilon = float(input("Введите значение ε: "))
            break
        except ValueError:
            print("Неверный формат")

    step = 1. / (m_plus - 1)
    display_second_method(function, table, function_value, n, epsilon, start, end)


def display():
    print("Лабораторная работа № 3.1")
    print("Вариант № 7")
    print("Задача обратного интерполирования.")

    while True:
        display_inverse_interpolation()
        print("\n\n")


