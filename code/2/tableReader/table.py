import sys
import Num, Sym, CSVReader, ARFFReader

class Table :
    def __init__(self, fileName):
        self.rows = []
        self.cols = []
        self.headers = []
        filetype = fileName.split(".")[-1]
        if filetype == "arff" :
            self.rowsGenerator = ARFFReader.ARFFReader(fileName).read()
        elif filetype == "csv" :
            self.rowsGenerator = CSVReader.CSVReader(fileName).read()
        self.generateTable()
        
    def generateTable(self):
        self.headers = self.rowsGenerator.next()
        self.rows.append(self.rowsGenerator.next())
        index = 0
        for val in self.rows[0] :
            if type(val) is int or type(val) is float:
                self.cols.append(Num.Num())
                self.cols[index].add(val)
            else:
                self.cols.append(Sym.Sym())
                self.cols[index].add(val)
            index += 1
        
        for row in self.rowsGenerator :
            self.rows.append(row)
            index = 0
            for val in row:
                self.cols[index].add(val)
                index += 1
    
    def showStats(self) :
        index = 0
        for col in self.cols :
            print self.headers[index]
            col.show()
            index += 1

if __name__ == "__main__":
    table = Table(sys.argv[1])
    table.showStats()