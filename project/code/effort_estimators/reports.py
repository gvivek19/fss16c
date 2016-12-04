import config
import stats
import sys
import matplotlib.pyplot as plt

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
    def generate_charts(datasets):
        e_types = ["_ar", "_mr", "_pred"]
        results = []



        i = 0
        for e_type in e_types:
            algo_count_map = {}
            dataset_algo_map = {}
            values = {}
            temp_list = []
            temp_dict = {}
            i = 0
            print e_type + " -----------------------------------   "
            for dataset in datasets:

                dataset_name = dataset.split("/")[-1].split(".")[0]
                report_filename = config.base_dir + config.error_metrics + "_" + dataset_name + e_type
                report_file = open(report_filename, "r")
                for line in report_file:
                    if len(line) > 0:
                        contents = line.split(",")
                        z = values.get(contents[0], [])
                        z.append(float(contents[1]))
                        values[contents[0]] = z
                result = stats.get_ranking( [ [k] + v for k,v in values.items() ])
                print dataset_name
                print result
            '''
                if e_type is not '_pred':
                    result = result[0]
                else:
                    result = result[-1]
                algo = result[1].split('_')[1]
                dataset_algo_map[dataset_name] = algo
                if algo not in algo_count_map:
                    algo_count_map[algo] = 0
                    i += 1
                    temp_dict[algo] = i
                temp_list.append(temp_dict[algo])
                algo_count_map[algo] += 1

            plt.plot(temp_list, range(len(dataset_algo_map)), 'ro')
            plt.xticks(temp_list, dataset_algo_map.values())
            plt.xlim([0,12  ])
            plt.yticks(range(len(dataset_algo_map)), dataset_algo_map.keys())
            plt.show()
            plt.plot(range(len(algo_count_map)), algo_count_map.values(), 'ro')
            plt.xticks(range(len(algo_count_map)), algo_count_map.keys())
            plt.ylim([0,12])
            plt.xlim([0,10])
            plt.show()
            '''




    @staticmethod
    def print_output(dataset):
        dataset_name = dataset.split("/")[-1].split(".")[0]
        print dataset_name
        fileobject = open(config.base_dir + config.skott_knott + "_" + dataset_name, "r")
        for line in fileobject :
            line = line[:-1]
            print line
        print "\n\n"
