from __future__ import division
import copy
from table import Table
from table import Column
import MyUtils, sys, table

class NaiveBayes:
    def __init__(self, data):
        self.k = 1
        self.m = 2
        
        self.table = data
        self.tables = {}
        self.create_class_tables()
        
    
    def create_class_tables(self):
        for row in self.table.rows :
            row_class = row[-1]
            existing_table = self.tables.get(row_class, table.clone(self.table))
            existing_table.add_row(row.contents)
            self.tables[row_class] = existing_table
        
        
    def predict(self, row):
        all = len(self.table.rows);
        guess, best, nh, k = None, -1*10**32, len(self.tables), self.k
        
        vals = {}
        for this, table in self.tables.items():
            like  = prior = (len(table.rows)  + k) / (all + k * nh)
            for col in table.cols[:-1]:
                if col.col:
                    x = row[col.pos]
                    if x != Column.UNKNOWN:
                        like *= col.col.like( x, prior) # mult together all the likes
            vals[this] = like
            if like > best:
                guess, best = this, like
        return (row[-1], guess)
    
    def predict_all(self, test_data):
        results = [self.predict(row) for row in test_data.rows[:10]]
        return results
        
if __name__ == "__main__":
    nb = NaiveBayes(Table(sys.argv[1]))
    predictions = nb.predict_all(Table(sys.argv[2]))
    MyUtils.showResults(predictions);