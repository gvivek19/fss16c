import config
import stats
import sys, math
import matplotlib.pyplot as plt
from error import Error

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
            line = line[:-1]
            print line
        print "\n\n"

    @staticmethod
    def __plot_graph(error_values, colors, filename):
        plt.close('all')

        _, axarr = plt.subplots(3, 4, figsize = (20, 20))
        axes = [item for sublist in axarr for item in sublist]

        datasets = error_values.keys()
        learners = colors.keys()
        lines = [0 for _ in xrange(len(datasets))]

        for i, dataset in enumerate(datasets):
            for j, learner in enumerate(learners):
                errors = sorted(error_values[dataset][learner])
                errors = [math.log(k, 10) if k != 0 else math.log(10**-32, 10) for k in errors]
                lines[j],  = axes[i].plot(errors, label=learner, color=colors[learner])

            axes[i].set_title(dataset)
            # plt.legend(loc="best", shadow=True, title=error_names[em], fancybox=True), bbox_to_anchor=(0.5, 1.05)
        plt.figlegend(lines, learners, loc = 'lower center', ncol=6, fancybox=True, shadow=True)
        plt.tight_layout(0, 1, 0, (0.03, 0.07, 0.97, 0.97))
        # plt.show()
        plt.savefig(filename)
        plt.close()

    @staticmethod
    def generate_error_charts(datasets):
        colors = {'teak_2_2' : "#000000", 'teak2' : "#FFB500", 'teak0' : "#1CE6FF", 'nnet' : "#FF34FF", \
                    'abe_2' : "#FF4A46", 'abe_16' : "#008941", 'abe_1' : "#B79762", 'teak_4_5' : "#A30059", \
                    'abe_4' : "#006FA6", 'lr' : "#7A4900", 'abe_8' : "#0000A6", 'teak_9' : "#004D43"}

        error_names = {"ar" : "Absolute Residual Error", "mr" : "Magnitude Relative Error"}


        error_values = {'ar' : {}, 'mr' : {}}

        for i, dataset in enumerate(datasets):
            dataset_name = dataset.split("/")[-1].split(".")[0]

            error_values['ar'][dataset_name] = {}
            error_values['mr'][dataset_name] = {}

            for learner in colors :
                effort_filename = config.base_dir + config.efforts + "_" + dataset_name + "_run_" + learner
                _file = open(effort_filename, "r")
                _errors = []
                for line in _file:
                    if len(line) > 0:
                        actual = float(line.split(",")[0])
                        predicted = float(line.split(",")[1])
                        _errors.append((actual, predicted))
                ar = Error.absolute_residual_error_all(_errors)
                mr = Error.magnitude_relative_error_all(_errors)

                error_values['ar'][dataset_name][learner] = ar
                error_values['mr'][dataset_name][learner] = mr

        Reports.__plot_graph(error_values['ar'], colors, config.base_dir + config.skott_knott[:-2] + "/ar.png")
        Reports.__plot_graph(error_values['mr'], colors, config.base_dir + config.skott_knott[:-2] + "/mre.png")
