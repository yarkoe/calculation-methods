from .differentiation_methods import *


def create_table(function, nodes_number, start, step):
    """
    Creates a new table. View of the table's row is a pair (node, function(node))
    @param function: source function.
    @param nodes_number: amount of nodes in the table.
    @param start: the first node in the table.
    @param step: step between two nodes in the table.
    @return: the new table: list of (node, function(node)) tuples.
    """

    table = []
    for i in range(nodes_number):
        new_node = start + i * step
        table.append((new_node, function(new_node)))

    return table


def create_differentiation_table(function, derivative, second_derivative, nodes_number, start, step):
    """
    Creates a new differentiation table with columns: node, function(node), approximate_deriv(node) and others
    @param function: source function.
    @param derivative: derivative of the function.
    @param second_derivative: second derivative of the function.
    @param nodes_number: amount of nodes in the table.
    @param start: the first node in the table.
    @param step: step between two nodes in the table.
    @return: extended table.
    """

    table = create_table(function, nodes_number, start, step)  # creates table of (node, function(node)) tuples.

    differentiation_table = []

    if len(table) < 3:
        return differentiation_table

    # creating the first row of the extended table.
    first_approximate_derivative = differentiate_first(table[0][1], table[1][1], table[2][1], step)
    first_derivative_diff = abs(derivative(table[0][0]) - first_approximate_derivative)

    # creating the last row of the extended table.
    last_approximate_derivative = differentiate_last(table[nodes_number-1][1], table[nodes_number-2][1],
                                                     table[nodes_number-3][1], step)
    last_derivative_diff = abs(derivative(table[nodes_number-1][0]) - last_approximate_derivative)

    # creating the center rows of the extended table.
    center_table = []
    for i in range(1, nodes_number - 1):
        approximate_derivative = differentiate_center(table[i+1][1], table[i-1][1], step)
        derivative_diff = abs(derivative(table[i][0]) - approximate_derivative)

        approximate_second_derivative = differentiate_center_twice(table[i][1], table[i+1][1], table[i-1][1], step)
        second_derivative_diff = abs(second_derivative(table[i][0]) - approximate_second_derivative)

        center_table.append((*table[i], approximate_derivative, derivative_diff, approximate_second_derivative,
                             second_derivative_diff))

    # results assembling.
    differentiation_table.append((*table[0], first_approximate_derivative, first_derivative_diff))
    differentiation_table.extend(center_table)
    differentiation_table.append((*table[nodes_number-1], last_approximate_derivative, last_derivative_diff))

    return differentiation_table
