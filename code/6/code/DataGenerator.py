import sys, table, collections, math, MyUtils, NaiveBayes
from random import randint
from time import time
import Num

class DataGenerator:
    def __init__(self, data):
        self.table = data
        self.tables = {}
        self.create_class_tables
        self.k = 1;

    def create_class_tables(self) :
        for row in self.table.rows :
            row_class = row[-1]
            existing_table = self.tables.get(row_class, table.clone(self.table))
            existing_table.add_row(row.contents)
            self.tables[row_class] = existing_table

    def get_next(self):
        class_variables = list(tables.keys());
        if self.k <= 1000:
            randnum = randint(0,1)
            rClass = class_variables[randnum]
        else:
            randnum = randint(1, 10)
            r = 0;
            if randnum > 1 and randnum < 5:
                r = 1
            elif randnum >= 5:
                r = 2
            rClass = class_variables[r]
        return self.tables[rClass].next_row

    def populate_table(self, table):
        for i in range(0, 100):
            table.add_row(self.getNext())

    def copy_table(self, table1, table2):
        for i in range(0, 100):
            table1.add_row(table2.rows[i]);

    def incremental_NB(self):
        size = len(tables.rows)
        eras = size / 100
        train_table = table.clone(self.table)
        populate_table(train_table)
        for i in range(0, eras):
            nb = NaiveBayes(train_table)
            test_table = table.clone(self.table)
            populate_table(test_table)
            results = nb.predict_all(test_table)
            #TODO compute recall
            copytable(train_table, test_table)




if __name__ == "__main__":
