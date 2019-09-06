# _*_ coding: utf-8 _*_
""" This file realize methods to separate
a section by several. Each separated section contains
an one root.
"""


def separate_section(math_function, step_length, start, end):
    """

    Divide section by several. The rule of partition is f(a)*f(b) < 0
    where a and b are start and end of the new sections. If this rule is true
    the [a; b] will be a new separated section.
    @param math_function: source function.
    @param step_length: length of one step.
    @param start: start of section.
    @param end: end of section
    @return: the new sections that contain roots.
    """

    a = start
    b = start + step_length

    new_sections = []

    while b <= end:
        if math_function(a) * math_function(b) <= 0:
            new_sections.append((a, b))

        a = b
        b = a + step_length

    return new_sections
