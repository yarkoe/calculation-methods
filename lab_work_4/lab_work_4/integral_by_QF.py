class QFIntegralContainer:
    """
    Class is used to present some Quadrature Functions (QF) methods of integral's approximate calculations.
    """

    def __init__(self, func, segment, interval_number):
        """
        @param func: source math function.
        @param segment: [A; B] segment.
        @param interval_number: number of intervals (subsegments) in the segment.
        """

        self.func = func
        self.segment = segment
        self.interval_number = interval_number
        self.step = (segment[1] - segment[0]) / interval_number  # (B - A) / num, num -- interval_number

        # Class initializes sums when meets their for the first time. Using this sums allows to speed up
        # the calculations methods.
        self.support_sum = None    # f(x_1) + ... + f(x_(num-1))
        self.support_sum_plus_half = None    # f(x_1 + h/2) + ... + f(x_(num-1) + h/2)

    def __init_support_sum(self):
        self.support_sum = 0

        cur_x = self.segment[0] + self.step  # x value starts with x_1 = A + step and ends with x_(num-1)
        for i in range(1, self.interval_number):
            self.support_sum += self.func(cur_x)
            cur_x += self.step

    def __init_support_sum_plus_half(self):
        self.support_sum_plus_half = 0

        # x value starts with x_0 + step/2 = A + step/2 and ends with x_(num-1) + step/2
        cur_x = self.segment[0] + self.step / 2
        for i in range(0, self.interval_number):
            self.support_sum_plus_half += self.func(cur_x)
            cur_x += self.step

    def calculate_by_left_rec(self):
        """
        Calculates integral by the left rectangle QF method. This method is based on
        formula step * sum_{k=0}^{num-1} f(x_k).
        @return: calculation result.
        """

        if self.support_sum is None:
            self.__init_support_sum()

        start_value = self.func(self.segment[0])  # f(x_0)

        return self.step* (start_value + self.support_sum)

    def calculate_by_right_rec(self):
        """
        Calculates integral by the right rectangle QF method. This method is based on
        formula step * sum_{k=0}^{num-1} f(x_k+1)
        @return: calculation result.
        """

        if self.support_sum is None:
            self.__init_support_sum()

        end_value = self.func(self.segment[1])  # f(x_num)

        return self.step * (self.support_sum() + end_value)

    def calculate_by_average_rec(self):
        """
        Calculates integral by the average rectangle QF method. This method is based on
        formula step * sum_{k=0}^{num-1} f(x_k + step/2)
        @return: calculation result.
        """

        if self.support_sum_plus_half is None:
            self.__init_support_sum_plus_half()

        return self.step * self.support_sum_plus_half

    def calculate_by_trap(self):
        """
        Calculates integral by the trapezoid QF method. This method is based on
        formula step/2 * sum_{k=0}^{num-1} [f(x_k) + f(x_k+1)]
        @return: calculation result.
        """

        if self.support_sum is None:
            self.__init_support_sum()

        start_value, end_value = self.func(self.segment[0]), self.func(self.segment[1])  # f(x_0), f(x_num)

        return self.step * (start_value / 2 + self.support_sum + end_value / 2)

    def calculate_by_simpson(self):
        """
        Calculates integral by the simpson's QF method.
        @return: calculation result.
        """

        start_value, end_value = self.func(self.segment[0]), self.func(self.segment[1])  # f(x_0), f(x_num)

        return self.step * (start_value / 6 + self.support_sum / 3 + 2 * self.support_sum_plus_half / 3 + end_value / 6)
