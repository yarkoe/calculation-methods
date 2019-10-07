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
        table.append(new_node, function(new_node))

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

    table = create_table(function, nodes_number - 1, start, step)  # creates table of (node, function(node)) tuples.

    extended_table = []

    if len(table) < 3:
        return extended_table

    
