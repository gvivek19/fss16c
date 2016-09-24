import sys, table
from random import randit

class KNN :
    def __init__(self, table, op_fun) :
        self.prediction_function = self.knn
        self.table = table
        self.k = 1
        if op_fun == "KDTree":
            self.training_function = self.kdtree
            self.prediction_function = self.knn_kmeans
            self.k = 1
            self.root = None
        elif op_fun == "KMeans":
            self.clusters = None
            self.training_function = self.kmeans
            self.k = 20
            self.v = {}

    def train(self) :
        if self.training_function == self.kmeans :
            self.training_function(100, 50)
            self.table = table.Table()
            for cluster in self.clusters :
                self.table.add_row(cluster)
        elif self.training_function == self.kdtree :
            self.root = kdtree(self, 0, len(self.table.rows))

    def test(self, row) :
        if self.predication_function == self.knn_kmeans:
            predicted_class = knn_kmeans(row)
                        
    Node = collections.namedtuple("Node", 'point axis left right')
    def kmeans(self, t, batch_size) :
        if self.clusters is None:
            c = [randint(0, len(self.table.rows)) for _ in range(0, self.k)]
            for i in c:
                self.clusters.add(self.table.rows[i])
        dist = {}

        for i in range(0, t):
            b = [randint(0, len(self.table.rows)) for _ in range(0, batch_size)]
            batch = []
            for i in b:
                row = self.table.rows[i]
                for j in range(0, len(self.clusters)):
                    cluster = clusters[j]
                    if dist[i] is None:
                        dist[i] = (self.table.row_distance(row, cluster), cluster)
                    else :
                        existing = dist[i]
                        current = self.table.row_distance(row, cluster)
                        if current < existing :
                            dist[i] = (current, j)
            for i in b:
                center = self.clusters[dist[i][1]]
                self.v.put(center, self.v.get(center, 0) + 1)
                rate = 1 / self.v[center]
                new_center = [( 1 - rate ) * center[col] + rate * self.table.rows[i][col] for col in xrange(len(center) - 1)]
                self.clusters[dist[i][1]] = new_center


    def kdtree(self, start, end, axis = 0) :
        if (start == end)
            return None;
        self.table.rows[start:end].sort(key = lambda x: x[axis])
        median = len(self.table.rows)//2
        median_point = self.table.rows[median_index]
        return Node( median_point, axis, kdtree(start, median, axis + 1), kdtree(median + 1, end, axis + 1))

    def knn(self, row) :
        distances = [(self.table.row_distance(row, data), data[-1]) for data in self.table.rows]
        sorted(distances, reverse=True, key = lambda x : x[0])
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

    def knn_kmeans(self, row) :
        best = [None, float('inf')]

        def recursive_search(here):
            if here is None:
                return
            point, axis, left, right = here

            here_sd = self.table.row_distance(point, row)
            if here_sd < best[2]:
                best[:] = point, here_sd

            diff = row[axis] - point[axis]
            close, away = (left, right) if diff <= 0 else (right, left)

            recursive_search(close)
            if diff ** 2 < best[2]:
                recursive_search(away)

        recursive_search(self.root)
        return best[0][-1]

'''
python <dataset> <optimization>
'''
if __name__ == "__main__":
    table = table.Table(sys.argv[1])
    optimization_func = None
    if len(sys.argv) > 2 :
        optimization_func = sys.argv[2]
    knn = KNN(table, optimization_func)
