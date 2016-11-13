from ARFFReader import ARFFReader
from CSVReader import CSVReader
from KNN import KNN
import stats
import sys
import random
import os
from abcd import Abcd
import table

m = 1
n = 1

def generateDataFiles(filename) :
    currdir = os.getcwd() + "/temp1"

    if not os.path.exists(currdir):
        try:
            os.makedirs(currdir)
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    filetype = filename.split(".")[-1]
    if filetype == "arff" :
        rowsGenerator = ARFFReader(filename).read()
    elif filetype == "csv" :
        rowsGenerator = CSVReader(filename).read()

    headers = rowsGenerator.next()
    headerText = "@relation " + filename + "\n"
    for h in headers :
        headerText += "@attribute " + h + "\n"
    headerText += "@data\n"

    dataRows = []
    length = 0
    for row in rowsGenerator :
        dataRows.append(row)
        length += 1

    for i in xrange(m) :

        for j in xrange(n) :
            random.shuffle(dataRows)
            trainfile = open(currdir + '/train' + str(i) + '_' + str(j) + '.arff', 'w')
            testfile = open(currdir + '/test' + str(i) + '_' + str(j) + '.arff', 'w')

            trainfile.write(headerText)
            testfile.write(headerText)

            for k in dataRows[:length//n] :
                sep = ""
                for v in k:
                    testfile.write(sep + str(v))
                    sep = ","
                testfile.write("\n")

            for k in dataRows[length//n:] :
                sep = ""
                for v in k:
                    trainfile.write(sep + str(v))
                    sep = ","
                trainfile.write("\n")

def runLearner() :
    path = os.getcwd() + '/temp1/'
    report = []
    for i in xrange(m) :
        for j in xrange(n) :
            print str(i) + "_" + str(j)
            traintable = table.Table(path + 'train' + str(i) + "_" + str(j) + ".arff")
            testtable = table.Table(path + 'test' + str(i) + "_" + str(j) + ".arff")
            a = KNN(traintable, 1)

            results = a.predict_all(testtable)

            log = None
            for result in results:
                one, two= result[0], result[1]
                if log:
                    log(one, two)
                else:
                    log=Abcd("dataset", "knn")
            report.append(log.getReport())
    return report

def analyzeReport(reports, wanted) :
    pd = {} #0 8
    pf = {} #0 9
    for report in reports :
        for entry in report :
            if entry[-1] == wanted :
                z = pd.get(entry[-1], [])
                z.append(entry[8])
                pd[entry[0]] = z

                z = pf.get(entry[-1], [])
                z.append(entry[9])
                pf[entry[0]] = z

    stats.rdivDemo( [ [k] + v for k,v in pd.items() ] )
    stats.rdivDemo( [ [k] + v for k,v in pf.items() ] )

if __name__ == '__main__':
    generateDataFiles(sys.argv[1])
    report = runLearner()
    analyzeReport(report, 0)
