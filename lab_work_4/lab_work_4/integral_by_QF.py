class QFIntegralContainer:
    """
    Class is used to present some methods of a integral's approximate calculations.
    """

    def __init__(self, func, segment, interval_number):
        self.func = func
        self.segment = segment
        self.interval_number = interval_number
        self.step = (segment[1] - segment[0]) / interval_number  # (B - A) / num, num -- interval_number

        # Class initializes sums when meets their for the first time.
        self.support_sum = None    # f(x_1) + ... + f(x_(num-1))
        self.support_sum_plus_half = None    # f(x_1 + h/2) + ... + f(x_(num-1) + h/2)

    def calculate_by_left_rec(self):
        """
        Calculates integral by the left rectangle QF method. The main formula is step * sum_{k=0}^{num-1} f(x_k).
        @return: calculation result.
        """

        if self.support_sum is None:
            self.support_sum = 0

            cur_x = self.segment[0] + self.step  # x value starts with x_1 = A + step and ends with x_(num-1)
            for i in range(1, self.interval_number):
                self.support_sum += self.func(cur_x)
                cur_x += self.step

        start_value = self.func(self.segment[0])

        return start_value + self.support_sum



