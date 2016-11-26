import config
import stats
import sys
class Reports:
    @staticmethod
    def analyze_report(report_filename, output_stream) :
        values = {}
        report_file = open(report_filename, "r")
        for line in report_file:
            if len(line) > 0:
                contents = line.split(",")
                z = values.get(contents[0], [])
                z.append(float(contents[1]))
                values[contents[0]] = z
        stats.skottknott( [ [k] + v for k,v in values.items() ], output_stream)

        @staticmethod
        def generate_reports():
            op_file = open(config.skott_knott, "w")
            if config.ar :
                op_file.write("Absolute Residual Error\n")
                Reports.analyze_report(config.error_metrics + "_ar", op_file)
            if config.mr :
                op_file.write("\nMagnitude Relative Error\n")
                Reports.analyze_report(config.error_metrics + "_mr", op_file)
            if config.pred:
                op_file.write("\nPred-25\n")
                Reports.analyze_report(config.error_metrics + "_pred", op_file)
