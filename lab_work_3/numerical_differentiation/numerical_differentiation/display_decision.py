import math

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
    print("Номер: Узел | Значение функции в узле | Производная | Разница первой производной | Вторая производная | "
          "Разница второй производной")

    # printing first row of diff table.
    print("{}: {} | {} | {} | {}".format(0, *differentiation_table[0]))

    for i in range(1, len(differentiation_table) - 1):
        print("{}: {} | {} | {} | {} | {} | {}".format(i, *differentiation_table))

    # printing last row of diff table.
    print("{}: {} | {} | {} | {}".format(len(differentiation_table) - 1,
                                         *differentiation_table[len(differentiation_table - 1)]))


def display_numerical_differentiation():
    print("Лабораторная работа № 3.2")
    print("Вариант № 7")
    print("Нахождение производных таблично-заданной функции")
    print("по формулам численного дифференцирования.\n")

    def function(x):
        return math.exp(4.5 * x)

    def derivative(x):
        return 4.5 * math.exp(4.5 * x)

    def second_derivative(x):
        return 20.25 * math.exp(4.5 * x)

    print("Вид фукнции: f(x) = e^(4.5 * x)\n")
    m_plus = input_int("Введите число значений в таблице: ")
    a = input_float("Введите начальное значение a: ")
    h = input_float("Введите шаг h: \n")

    differentiation_table = create_differentiation_table(function, derivative, second_derivative, m_plus, a, h)

    print_differentiation_table(differentiation_table)
