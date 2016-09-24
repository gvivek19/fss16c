import sys, math
import Num, Sym, CSVReader, ARFFReader

class Table :
    def __init__(self, fileName=None):
        self.rows = []
        self.cols = []
        self.headers = []
        if fileName is not None:
            filetype = fileName.split(".")[-1]
            if filetype == "arff" :
                self.rowsGenerator = ARFFReader.ARFFReader(fileName).read()
            elif filetype == "csv" :
                self.rowsGenerator = CSVReader.CSVReader(fileName).read()
            self.generateTable()

    def add_row(self, row) :
        if len(self.headers) == 0:
            index = 0
            for val in row :
                self.headers.append(index)
                if type(val) is int or type(val) is float:
                    self.cols.append(Num.Num())
                    self.cols[index].add(val)
                else:
                    self.cols.append(Sym.Sym())
                    self.cols[index].add(val)
                index += 1
            self.rows.append(row)
        else :
            self.rows.append(row)
            index = 0
            for val in row :
                self.cols[index].add(val)
                index += 1
    
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

    def row_distance(self, row1, row2) :
        distance = 0
        index = 0
        for index in xrange(len(self.cols) - 1):
            col = self.cols[index]
            distance += (col.dist(row1[index], row2[index]) ** 2)
        return math.sqrt(distance)

    def find_nearest(self, row) :
        nearest = None
        distance = 10**32
        for r in self.rows:
            if r != row:
                current_distance = self.row_distance(row, r)
                if distance >= current_distance :
                    nearest = r
                    distance = current_distance
        return nearest

    def find_furthest(self, row) :
        furthest = None
        distance = 10**-32
        for r in self.rows:
            if r != row:
                current_distance = self.row_distance(row, r)
                #print r, current_distance
                if distance <= current_distance:
                    furthest = r
                    distance = current_distance
        return furthest


if __name__ == "__main__":
    table = Table(sys.argv[1])
    print table.rows[0]
    print "Closest : ",table.find_nearest(table.rows[0])
    print "Furthest : ", table.find_furthest(table.rows[0])
    print ""
    print table.rows[1]
    print "Closest : ",table.find_nearest(table.rows[1])
    print "Furthest : ", table.find_furthest(table.rows[1])
