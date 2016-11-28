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
    def generate_reports(dataset):
        dataset_name = dataset.split("/")[-1].split(".")[0]
        op_file = open(config.base_dir + config.skott_knott + "_" + dataset_name, "w")
        if config.ar :
            op_file.write("Absolute Residual Error\n")
            Reports.analyze_report(config.base_dir + config.error_metrics + "_" + dataset_name + "_ar", op_file)
        if config.mr :
            op_file.write("\nMagnitude Relative Error\n")
            Reports.analyze_report(config.base_dir + config.error_metrics + "_" + dataset_name + "_mr", op_file)
        if config.pred:
            op_file.write("\nPred-25\n")
            Reports.analyze_report(config.base_dir + config.error_metrics + "_" + dataset_name + "_pred", op_file)

    @staticmethod
    def print_output(dataset):
        dataset_name = dataset.split("/")[-1].split(".")[0]
        print dataset_name
        fileobject = open(config.base_dir + config.skott_knott + "_" + dataset_name, "r")
        for line in fileobject :
            print line
        print "\n\n"
