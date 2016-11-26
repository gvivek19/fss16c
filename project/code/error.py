class Error:
    def __init__( output_tuples):
        self.output_tuples = output_tuples

    def absolute_residual_error(self):
        return [abs(tup[1] - tup[0]) for tup in output_tuples]

    def magnitude_relative_error(self):
        return [abs(tup[1] - tup[0])/float(tup[1])  for tup in output_tuples]

    def pred(self, x):
        count = 0
        for tup in self.output_tuples:
            rel_error = abs(tup[1] - tup[0])/float(tup[1])
            if (rel_error * 100) <= x:
                count += 1
        return (count / len(output_tuples)) * 100
