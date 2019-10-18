import math
from prettytable import PrettyTable

from .table_operations import create_differentiation_table


def input_int(message):
    while True:
        try:
            int_value = int(input(message))
            break
        except ValueError:
            print("Неверный формат")

    return int_value


def input_float(message):
    while True:
        try:
            float_value = float(input(message))
            break
        except ValueError:
            print("Неверный формат")

    return float_value


def print_differentiation_table(differentiation_table):
    pretty_table = PrettyTable()
    pretty_table.field_names = ["Номер", "Узел", "Значение функции в узел", "Производная", "Разница первой производной",
                                "Вторая производная", "Разница второй производной"]

    pretty_table.add_row([0, *differentiation_table[0], "", ""])

    for i in range(1, len(differentiation_table) - 1):
        pretty_table.add_row([i, *differentiation_table[i]])

    pretty_table.add_row([len(differentiation_table) - 1, *differentiation_table[len(differentiation_table) - 1],
                          "", ""])

    print(pretty_table)


def display_numerical_differentiation():
    def function(x):
        return math.exp(4.5 * x)

    def derivative(x):
        return 4.5 * math.exp(4.5 * x)

    def second_derivative(x):
        return 20.25 * math.exp(4.5 * x)

    print("Вид фукнции: f(x) = e^(4.5 * x)\n")
    m_plus = input_int("Введите число значений в таблице: ")
    a = input_float("Введите начальное значение a: ")
    h = input_float("Введите шаг h: ")
    print()

    differentiation_table = create_differentiation_table(function, derivative, second_derivative, m_plus, a, h)

    print_differentiation_table(differentiation_table)


def display():
    print("Лабораторная работа № 3.2")
    print("Вариант № 7")
    print("Нахождение производных таблично-заданной функции")
    print("по формулам численного дифференцирования.")

    while True:
        print("\n\n")
        display_numerical_differentiation()
