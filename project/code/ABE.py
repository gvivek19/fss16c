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
        return [ x[1] for x in distances[:k] ]

    def train(self):
        pass

    def predict(self, row) :
        return self.knn(row)
