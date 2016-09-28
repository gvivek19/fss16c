import sys, table, collections, math
from random import randint
from time import time

class KNN :
    def __init__(self, table, op_fun) :
        self.prediction_function = self.knn
        self.training_function = None
        self.table = table
        self.k = 5
        self.Node = collections.namedtuple("Node", 'point axis left right')
        
        if op_fun == "KDTree":
            self.training_function = self.kdtree
            self.prediction_function = self.knn_kmeans
            self.k = min(len(self.table.cols) - 1, 10)
            self.root = None
        elif op_fun == "KMeans":
            self.clusters = None
            self.training_function = self.kmeans
            self.k = 10
            self.v = {}

    def train(self) :
        if self.training_function == self.kmeans :
            self.training_function(100, 10)
            self.table = table.Table()
            for cluster in self.clusters :
                self.table.add_row(cluster)
        elif self.training_function == self.kdtree :
            self.root = self.kdtree(0, len(self.table.rows))

    def test(self, row) :
        return self.prediction_function(row)
    
    def knn(self, row) :
        distances = [(self.table.row_distance(row, data), data[-1]) for data in self.table.rows]
        distances = sorted(distances, key = lambda x : x[0])
        classCounts = {}
        max_class = None
        for i in xrange(self.k) :
            cl = distances[i][1]
            if max_class == None:
                max_class = cl
            existing_count = classCounts.get(cl, 0)
            classCounts[cl] = existing_count + 1
            if classCounts[max_class] < existing_count + 1 :
                max_class = cl
        return max_class
    
    def kmeans(self, t, batch_size) :
        if self.clusters is None:
            self.clusters = []
            c = [randint(0, len(self.table.rows) - 1) for _ in range(0, self.k)]
            for i in c:
                self.clusters.append(self.table.rows[i])
        dist = {}

        for h in range(0, t):
            b = [randint(0, len(self.table.rows) - 1) for _ in range(0, batch_size)]
            batch = []
            for i in b:
                row = self.table.rows[i]
                for j in range(0, len(self.clusters)):
                    cluster = self.clusters[j]
                    if i not in dist:
                        dist[i] = (self.table.row_distance(row, cluster), j)
                    else :
                        existing = dist[i]
                        current = self.table.row_distance(row, cluster)
                        if current < existing :
                            dist[i] = (current, j)
            for i in b:
                center = self.clusters[dist[i][1]]
                self.v[dist[i][1]] = self.v.get(dist[i][1], 0) + 1
                rate = 1 / self.v[dist[i][1]]
                new_center = [( 1 - rate ) * center[col] + rate * self.table.rows[i][col] for col in xrange(len(center))]
                self.clusters[dist[i][1]] = new_center


    def kdtree(self, start, end, axis = 0) :
        if (start == end):
            return None
        if axis >= self.k:
            return None;
        temp_rows = self.table.rows[start:end]
        sorted(temp_rows, key = lambda x: x[axis])
        self.table.rows[start:end] = temp_rows
        median = len(temp_rows)//2
        median_point = self.table.rows[median]
        return self.Node( median_point, axis, self.kdtree(start, median, axis + 1), self.kdtree(median + 1, end, axis + 1))

    
    def knn_kmeans(self, row) :
        best = [None, float('inf')]

        def recursive_search(here):
            if here is None:
                return
            point, axis, left, right = here

            here_sd = self.table.row_distance(point, row)
            if here_sd < best[1]:
                best[:] = point, here_sd
            diff = self.table.cols[axis].dist(row[axis], point[axis])
            close, away = (left, right) if diff <= 0 else (right, left)

            recursive_search(close)
            if diff ** 2 < best[1]:
                recursive_search(away)

        recursive_search(self.root)
        return best[0][-1]

'''
python <training dataset> <testing dataset> <optimization>
'''
if __name__ == "__main__":
    start_time = time()
    training_table = table.Table(sys.argv[1])
    optimization_func = None
    if len(sys.argv) > 3 :
        optimization_func = sys.argv[3]
    knn = KNN(training_table, optimization_func)
    knn.train()
    testing_table = table.Table(sys.argv[2])
    print "\n=== Predictions on test data ===\n"
    print " inst#     actual  predicted error prediction"
    iteratorIndex = 1
    classNumbers = {}
    classNo = 1
    for row in testing_table.rows:
        predicted = knn.test(row)
        expected = row[-1]
        
        if expected not in classNumbers:
            classNumbers[expected] = classNo
            classNo += 1
        if predicted not in classNumbers:
            classNumbers[predicted] = classNo
            classNo += 1
        temp1 = str(classNumbers[expected]) + ":" + str(expected)
        temp2 = str(classNumbers[predicted]) + ":" + str(predicted)
        prediction = (expected == predicted)
        
        print ("{: >6.0f}".format(iteratorIndex) + "{:>21}".format(temp1) + "{: >21}".format(temp2) + "{:>18.0f}".format(prediction))
        iteratorIndex += 1
    end_time = time()
    #print "Total runtime : %d" % (end_time - start_time) 