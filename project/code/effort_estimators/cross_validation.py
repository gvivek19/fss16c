from ARFFReader import ARFFReader
from CSVReader import CSVReader
import ABE, Teak, linear_regression, neural_network
import stats
import sys
import random
import os
import table
from error import Error
import config
import shutil

class cross_validation:
    def __init__(self, data_filename):
        self.m = config.crossval_m
        self.n = config.crossval_n
        self.loocv = (self.n == 'LOOCV')

        self.data_filename = config.base_dir + data_filename
        dataset_name = self.data_filename.split("/")[-1].split(".")[0]
        if config.ar :
            self.ar_file = open(config.base_dir + config.error_metrics + "_" + dataset_name + "_ar", "w")
        if config.mr :
            self.mr_file = open(config.base_dir + config.error_metrics + "_" + dataset_name + "_mr", "w")
        if config.pred :
            self.pred_file = open(config.base_dir + config.error_metrics + "_" + dataset_name + "_pred", "w")

    def generate_data_files(self) :
        currdir = config.base_dir + "/temp"

        if not os.path.exists(currdir):
            try:
                os.makedirs(currdir)
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        filetype = self.data_filename.split(".")[-1]
        if filetype == "arff" :
            rowsGenerator = ARFFReader(self.data_filename).read()
        elif filetype == "csv" :
            rowsGenerator = CSVReader(self.data_filename).read()

        headers = rowsGenerator.next()
        headerText = "@relation " + self.data_filename + "\n"
        for h in headers :
            headerText += "@attribute " + h + "\n"
        headerText += "@data\n"

        dataRows = []
        length = 0
        for row in rowsGenerator :
            dataRows.append(row)
            length += 1

        if self.loocv :
            self.n = length

        for i in xrange(self.m) :
            random.shuffle(dataRows)

            for j in xrange(self.n) :
                trainfile = open(currdir + '/train' + str(i) + '_' + str(j) + '.arff', 'w')
                testfile = open(currdir + '/test' + str(i) + '_' + str(j) + '.arff', 'w')

                trainfile.write(headerText)
                testfile.write(headerText)

                start_index = j * length // self.n
                end_index = (j + 1) * length // self.n
                for k in dataRows[start_index : end_index] :
                    sep = ""
                    for v in k:
                        testfile.write(sep + str(v))
                        sep = ","
                    testfile.write("\n")

                for k in dataRows[0 : start_index] :
                    sep = ""
                    for v in k:
                        trainfile.write(sep + str(v))
                        sep = ","
                    trainfile.write("\n")

                for k in dataRows[end_index : ] :
                    sep = ""
                    for v in k:
                        trainfile.write(sep + str(v))
                        sep = ","
                    trainfile.write("\n")

    def run_teak_9(self, train, test) :
        learner = Teak.Teak(train, config.teak_k, 9)
        learner.train()
        return learner.predict_all(test)

    def run_teak_4_5(self, train, test) :
        learner = Teak.Teak(train, config.teak_k, 4.5)
        learner.train()
        return learner.predict_all(test)

    def run_teak_2_2(self, train, test) :
        learner = Teak.Teak(train, config.teak_k, 2.2)
        learner.train()
        return learner.predict_all(test)

    def run_teak0(self, train, test) :
        learner = Teak.Teak(train, config.teak_k, 9)
        learner.train(False)
        return learner.predict_all(test)

    def run_teak2(self, train, test):
        learner = Teak.Teak(train, config.teak_k, 9)
        learner.train(False)
        return learner.predict_all2(test)

    def run_lr(self, train, test) :
        learner = linear_regression.linear_regression(train)
        learner.train()
        return learner.predict_all(test)

    def run_nnet(self, train, test) :
        learner = neural_network.neural_network(train)
        learner.train()
        return learner.predict_all(test)

    def run_abe_k(self, train, test, k):
        learner = ABE.ABE(train, k)
        return learner.predict_all(test)

    def run_abe_1(self, train, test):
        return self.run_abe_k(train, test, 1)

    def run_abe_2(self, train, test):
        return self.run_abe_k(train, test, 2)

    def run_abe_4(self, train, test):
        return self.run_abe_k(train, test, 4)

    def run_abe_8(self, train, test):
        return self.run_abe_k(train, test, 8)

    def run_abe_16(self, train, test):
        return self.run_abe_k(train, test, 16)

    def run_learners(self):
        learners = []

        if config.teak :
            if 9 in config.teak_gamma:
                learners.append(self.run_teak_9)
            if 4.5 in config.teak_gamma:
                learners.append(self.run_teak_4_5)
            if 2.2 in config.teak_gamma:
                learners.append(self.run_teak_2_2)

        if config.teak0:
            learners.append(self.run_teak0)

        if config.teak2:
            learners.append(self.run_teak2)

        if config.abe:
            if 1 in config.abe_k:
                learners.append(self.run_abe_1)
            if 2 in config.abe_k:
                learners.append(self.run_abe_2)
            if 4 in config.abe_k:
                learners.append(self.run_abe_4)
            if 8 in config.abe_k:
                learners.append(self.run_abe_8)
            if 16 in config.abe_k:
                learners.append(self.run_abe_16)

        if config.neuralnet:
            learners.append(self.run_nnet)

        if config.lregression:
            learners.append(self.run_lr)

        for learner in learners:
            self.run_learner(learner)

    def run_learner(self, learner) :
        print learner.__name__
        path = config.base_dir + '/temp/'

        dataset_name = self.data_filename.split("/")[-1].split(".")[0]
        efforts_file = open(config.base_dir + config.efforts + "_" + dataset_name + "_" + learner.__name__, "w")
        for i in xrange(self.m) :
            for j in xrange(self.n) :
                train_table = table.Table(path + 'train' + str(i) + "_" + str(j) + ".arff")
                test_table = table.Table(path + 'test' + str(i) + "_" + str(j) + ".arff")

                results = learner(train_table, test_table)
                for result in results:
                    efforts_file.write(str(result[0]) + "," + str(result[1]) + "\n")

                if config.ar:
                    self.ar_file.write("%s,%.4f\n" %(learner.__name__, Error.absolute_residual_error(results)))
                if config.mr:
                    self.mr_file.write("%s,%.4f\n" %(learner.__name__, Error.magnitude_relative_error(results) * 100))
                if config.pred:
                    self.pred_file.write("%s,%.4f\n" %(learner.__name__, Error.pred(results)))


    @staticmethod
    def run_cross_validation(dataset):
        cv = cross_validation(dataset)
        cv.generate_data_files()
        cv.run_learners()
        shutil.rmtree(config.base_dir + "/temp")
