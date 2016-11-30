class Error:
    @staticmethod
    def absolute_residual_error(output_tuples):
        errors = [abs(tup[1] - tup[0]) for tup in output_tuples]
        errors = sorted(errors)
        n = len(errors)
        median = errors[n//2] if n % 2 == 1 else (errors[(n-1)//2] + errors[(n+1)//2]) / 2
        mean = sum(errors) / n
        return mean

    @staticmethod
    def magnitude_relative_error(output_tuples):
        errors = [abs(tup[1] - tup[0])/float(tup[1])  for tup in output_tuples]
        errors = sorted(errors)
        n = len(errors)
        median = errors[n//2] if n % 2 == 1 else (errors[(n-1)//2] + errors[(n+1)//2]) / 2
        mean = sum(errors) / n
        return mean

    @staticmethod
    def pred(output_tuples, x = 25):
        count = 0
        for tup in output_tuples:
            rel_error = abs(tup[1] - tup[0])/float(tup[1])
            if (rel_error * 100) <= x:
                count += 1
        return (count *100.0 / len(output_tuples))
