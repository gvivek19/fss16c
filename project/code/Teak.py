import sys, table, collections, math, MyUtils
import random
from time import time
import Num

class Teak :
    def __init__(self, table, k) :
        self.table = table
        self.k = k
    
    def gac(self, table) :
    	pass
    
    def prune(self, tree):
    	pass
    
    def tree2table(self, tree):
    	pass
    
    def train(self):
		cluster_tree = self.gac(self.table)
		pruned_tree = self.prune(cluster_tree)
		pruned_table = self.tree2table(pruned_tree)
		self.model = self.gac(pruned_table)
    
    def predict(self, row) :
        pass

