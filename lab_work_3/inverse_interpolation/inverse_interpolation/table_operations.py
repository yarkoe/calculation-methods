def create_table(function, nodes_number, start, end):
    """
    Creates a table. Row of the table is a pair (point, function(point)).
    @param function: source function.
    @param nodes_number: amount of elements in the table.
    @param start: start of a segment where the table should be created.
    @param end: end of the segment.
    @return: list of the table's elements.
    """

    table_list = []

    for j in range(0, nodes_number + 1):
        # calculate a new point.
        x_j = start + j * (end - start) / nodes_number

        table_list.append((x_j, function(x_j)))

    return table_list


def sort_table(table, node):
    """
    Sorts a table by the given node.
    @param table: list of (node, function_value) tuples.
    @param node: point of a segment.
    @return: sorted table.
    """

    return sorted(table, key=lambda element: abs(element[0] - node))


def reverse_table(table):
    """
    Reverses columns of the table.
    @param table: list of (node, function_value) tuples.
    @return: a reversed table: list of (function_value, node) tuples.
    """

    return [(item[1], item[0]) for item in table]


def segment_between_value(table, function_value):
    start = table[0][1]
    end = table[len(table) - 1][1]


