# _*_ coding: utf-8 _*_
""" This file contains method to show search methods.
"""

import math
from .section_separator import separate_segment
from .search_methods import *


def show_search_methods():
    print("Лабораторная работа № 1")
    print("ЧИСЛЕННЫЕ МЕТОДЫ РЕШЕНИЯ НЕЛИНЕЙНЫХ УРАВНЕНИЙ\n")

    def trigonometric_function(x):
        return x * math.sin(x) - 1

    def derivative(x):
        return math.sin(x) + x * math.cos(x)

    test_segment = (-10, 2)
    test_step = (test_segment[1] - test_segment[0]) / 100
    test_eps = 10 ** (-5)

    print("Параметры задачи:")
    print("A= {}, B= {}".format(test_segment[0], test_segment[1]))
    print("Вид функции f(x)= x*sin(x) - 1")
    print("Эпсилон: ε= {}\n".format(test_eps))

    print("ШАГ 1: ОТДЕЛЕНИЕ КОРНЕЙ УРАВНЕНИЯ НА ОТРЕЗКЕ [A, B]\n")
    segments = separate_segment(trigonometric_function, test_step, *test_segment)

    print("Количество отрезков перемены знака функции: {}".format(len(segments)))

    print("Отрезки:")
    results = []
    for segment in segments:
        print(list(segment))
        search_results = [search_root_bisection(trigonometric_function, test_eps, *segment),
                          search_root_newton(trigonometric_function, derivative,
                                             test_eps, *segment), search_root_modifiable_newton(trigonometric_function,
                                                                                                derivative, test_eps,
                                                                                                *segment),
                          search_root_secants_method(trigonometric_function, test_eps,
                                                     *segment)]
        results.append((list(segment), search_results))

    print("")
    print("ШАГ 2: УТОЧНЕНИЕ КОРНЕЙ\n")

    for result in results:
        print("Отрезок: {}\n".format(result[0]))

        bisection_results = result[1][0]
        newton_results = result[1][1]
        modifiable_newton_results = result[1][2]
        secants_results = result[1][3]

        print("МЕТОД ПОЛОВИННОГО ДЕЛЕНИЯ")
        print("Количество шагов N= {}".format(bisection_results[1]))
        print("Приближённое решение = {}".format(bisection_results[0]))
        print("Длина последнего отрезка = {}".format(bisection_results[2]))
        print("Абсолютная величина невязки = {}\n".format(bisection_results[3]))

        print("МЕТОД НЬЮТОНА")
        print("Начальное приближение к корню:".format(newton_results[4]))
        print("Количество шагов N= {}".format(newton_results[1]))
        print("Приближённое решение = {}".format(newton_results[0]))
        print("Длина последнего отрезка = {}".format(newton_results[2]))
        print("Абсолютная величина невязки = {}\n".format(newton_results[3]))

        print("МОДИФИЦИРОВАННЫЙ МЕТОД НЬЮТОНА")
        print("Начальное приближение к корню:".format(modifiable_newton_results[4]))
        print("Количество шагов N= {}".format(modifiable_newton_results[1]))
        print("Приближённое решение = {}".format(modifiable_newton_results[0]))
        print("Длина последнего отрезка = {}".format(modifiable_newton_results[2]))
        print("Абсолютная величина невязки = {}\n".format(modifiable_newton_results[3]))

        print("МЕТОД СЕКУЩИХ")
        print("Количество шагов N= {}".format(secants_results[1]))
        print("Приближённое решение = {}".format(secants_results[0]))
        print("Длина последнего отрезка = {}".format(secants_results[2]))
        print("Абсолютная величина невязки = {}\n".format(secants_results[3]))

