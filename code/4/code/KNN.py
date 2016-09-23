import sys, table

class KNN :
    def __init__(self, table, op_fun) :
        self.prediction_function = self.knn
        self.table = table
        self.k = 1
        if op_fun == "KDTree":
            self.prediction_function = self.kdtree
            self.k = 1
        elif op_fun == "KMeans":
            self.prediction_function = self.kmeans
            self.k = 20
    
    def kdtree(self, row) :
        pass
    
    def kmeans(self, row) :
        pass
    
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
            
'''
python <dataset> <optimization>
'''
if __name__ == "__main__":
    table = table.Table(sys.argv[1])
    optimization_func = None
    if len(sys.argv) > 2 :
        optimization_func = sys.argv[2]
    knn = KNN(table, optimization_func)