import math

from .table_operations import create_table, sort_table, reverse_table
from .lagrangian_form import create_lagrangian_form
from .section_separator import separate_segment
from .bisection_method import search_root_bisection


def print_table(table):
    print("Номер: Узел | Значение функции в узле")
    for i in range(len(table)):
        print("{}: {} | {}".format(i, table[i][0], table[i][1]))


def display_first_method(math_function, table, function_value, polynomial_degree):
    print("Способ № 1: обмен столбцов таблицы местами.")

    sorted_reversed_table = sort_table(reverse_table(table), function_value)

    print("Отсортированная изменённая таблица: ")
    print_table(sorted_reversed_table)

    inverse_lagrangian_form = create_lagrangian_form(sorted_reversed_table, polynomial_degree)
    argument = inverse_lagrangian_form(function_value)

    print("Значение аргумента по заданному параметру F: {}".format(argument))
    print("Значение модуля невязки: {}".format(abs(math_function(argument) - function_value)))


def display_second_method(math_function, table, function_value, polynomial_degree, epsilon, start, end, step):
    print("Способ № 2: нахождение корней уравнения Pn(x) - F.")
    segments = separate_segment(math_function, step, start, end)

    lagrangian_form = create_lagrangian_form()

    for segment in segments:
        arg = search_root_bisection(lambda x: math_function(x) - function_value, epsilon, start, end)


def display_inverse_interpolation():
    """
    Displays inverse interpolation exercise interactively to console.
    @return: void.
    """

    print("Лабораторная работа № 3.1")
    print("Вариант № 7")
    print("Задача обратного интерполирования.")

    def function(x):
        return 2 * math.sin(x) - x / 2

    start = 0
    end = 1
    print("Вид фукнции: f(x) = x*sin(x) - x/2")
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
    display_second_method(function, table, function_value, n, epsilon, step)

