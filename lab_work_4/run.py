import math

from lab_work_4.lab_work_4.integral_by_QF import QFIntegralContainer


def input_int(message):
    while True:
        try:
            int_value = int(input(message))
            if int_value <= 0:
                print("Значение должно быть больше 0")
                continue
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


def print_qf_method(method_name, approximate_value, true_value):
    print(method_name)
    print("Приближённое значение: {}".format(approximate_value))
    print("Абсолютная фактическая погрешность: {}\n".format(abs(true_value - approximate_value)))


def function_factory(function_type):
    if function_type == "main":
        print("Вид фукнции: f(x) = 2*sin(x) - x/2")
        return lambda x: 2 * math.sin(x) - x / 2, lambda x: -2 * math.cos(x) - x ** 2 / 4
    elif function_type == "x":
        print("Вид функции: f(x) = x")
        return lambda x: x, lambda x: x ** 2 / 2
    elif function_type == "x**2":
        print("Вид функции: f(x) = x^2")
        return lambda x: x ** 2, lambda x: x ** 3 / 3


def error(start, end, m, Md, const, d_plus):
    return const * (end - start) * ((end - start) / m) ** d_plus * Md


def main():
    print("Лабораторная работа № 4")
    print("Приближённое вычисление интеграла по составным квадратурным формулам")

    # def function(x):
    #     return 2 * math.sin(x) - x / 2
    #
    # def antiderivative(x):
    #     return -2 * math.cos(x) - x ** 2 / 4

    function, antiderivative = function_factory("main")

    while True:
        start = input_float("Введите начало отрезка: ")
        end = input_float("Введите конец отрезка: ")
        print("A= {}, B= {}\n".format(start, end))

        true_value = antiderivative(end) - antiderivative(start)
        print("Значение интеграла от функции f по отрезку [A; B]= {}\n".format(true_value))

        m = input_int("Введите m: ")
        qf_integral_container = QFIntegralContainer(function, (start, end), m)

        print_qf_method("Метод левых прямоугольников", qf_integral_container.calculate_by_left_rec(), true_value)
        print_qf_method("Метод правых прямоугольников", qf_integral_container.calculate_by_right_rec(), true_value)
        print_qf_method("Метод средних прямоугольников", qf_integral_container.calculate_by_average_rec(), true_value)
        print_qf_method("Метод трапеций", qf_integral_container.calculate_by_trap(), true_value)
        print_qf_method("Метод Симпсона", qf_integral_container.calculate_by_simpson(), true_value)


if __name__ == "__main__":
    main()
