from ARFFReader import ARFFReader
from CSVReader import CSVReader
import ABE, Teak, linear_regression, neural_network
import stats
import sys
import random
import os
from abcd import Abcd
import table

class cross_validation:
    def __init__(self):
        self.m = 1
        self.n = 5

    def generate_data_files(self, data_filename) :
        currdir = os.getcwd() + "/temp1"

        if not os.path.exists(currdir):
            try:
                os.makedirs(currdir)
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        filetype = data_filename.split(".")[-1]
        if filetype == "arff" :
            rowsGenerator = ARFFReader(data_filename).read()
        elif filetype == "csv" :
            rowsGenerator = CSVReader(data_filename).read()

        headers = rowsGenerator.next()
        headerText = "@relation " + data_filename + "\n"
        for h in headers :
            headerText += "@attribute " + h + "\n"
        headerText += "@data\n"

        dataRows = []
        length = 0
        for row in rowsGenerator :
            dataRows.append(row)
            length += 1

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

    def run_teak(self, train, test) :
        learner = Teak.Teak(train, 3)
        learner.train()
        return learner.predict_all(test)

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
        learners = [self.run_teak, self.run_lr, self.run_nnet, self.run_abe_1, self.run_abe_2, self.run_abe_4, self.run_abe_8, self.run_abe_16]
        for learner in learners:
            self.run_learner(learner)

    def run_learner(self, learner) :
        path = os.getcwd() + '/temp1/'
        report = []
        for i in xrange(self.m) :
            for j in xrange(self.n) :
                print str(i) + "_" + str(j)

                train_table = table.Table(path + 'train' + str(i) + "_" + str(j) + ".arff")
                test_table = table.Table(path + 'test' + str(i) + "_" + str(j) + ".arff")

                learner(train_table, test_table)
        return report

    def analyze_report(self, reports) :
        pd = {} #0 8
        pf = {} #0 9
        for report in reports :
            for entry in report :
                z = pd.get(entry[-1], [])
                z.append(entry[8])
                pd[entry[0]] = z

                z = pf.get(entry[-1], [])
                z.append(entry[9])
                pf[entry[0]] = z

        stats.rdivDemo( [ [k] + v for k,v in pd.items() ] )
        stats.rdivDemo( [ [k] + v for k,v in pf.items() ] )


if __name__ == '__main__':
    cv = cross_validation()
    cv.generate_data_files(sys.argv[1])
    cv.run_learners()
    #report = runLearner()
    #analyzeReport(report, 0)
    #runLearners(table.Table(sys.argv[1]), table.Table(sys.argv[1]))
