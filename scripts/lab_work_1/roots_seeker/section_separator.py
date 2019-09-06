# _*_ coding: utf-8 _*_
""" This file realize methods to separate
a segment by several. Each separated segment contains
an one root.
"""


def separate_segment(math_function, step_length, start, end):
    """

    Divide segment by several. The rule of partition is f(a)*f(b) < 0
    where a and b are start and end of the new segments. If this rule is true
    the [a; b] will be a new separated segment.
    @param math_function: source function.
    @param step_length: length of one step.
    @param start: start of segment.
    @param end: end of segment
    @return: the new segments that contain roots.
    """

    current_segment_start = start
    current_segment_end = start + step_length

    new_segments = []

    while current_segment_end <= end:
        if math_function(current_segment_start) * math_function(current_segment_end) <= 0:
            new_segments.append((current_segment_start, current_segment_end))

        current_segment_start = current_segment_end
        current_segment_end = current_segment_start + step_length

    return new_segments
