import sys, table, collections, math, MyUtils
import random
from time import time
import Num

class ABE :
    def __init__(self, table, k) :
        self.table = table
        self.k = k

    def knn(self, row) :
        distances = [(self.table.row_distance(row, data), data) for data in self.table.rows]
        distances = sorted(distances, key = lambda x : x[0])
        return sum ([ x[1][-1] for x in distances[: self.k] ]) / self.k

    def train(self):
        pass

    def predict(self, row) :
        return (row[-1], self.knn(row))

    def predict_all(self, test_table) :
        return [ self.predict(row.contents) for row in test_table.rows ]
