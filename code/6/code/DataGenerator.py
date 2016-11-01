import sys, table, collections, math, MyUtils, NaiveBayes
from random import randint
from time import time
import Num

class DataGenerator:
    def __init__(self, data):
        self.table = data
        self.tables = {}
        self.create_class_tables()
        self.k = 1;

    def create_class_tables(self) :
        for row in self.table.rows :
            row_class = row[-1]
            existing_table = self.tables.get(row_class, table.clone(self.table))
            existing_table.add_row(row.contents)
            self.tables[row_class] = existing_table

    def get_row_count(self):
        return len(self.table.rows)

    def get_next(self):
        class_variables = list(self.tables.keys());

        if self.k <= 1000:
            randnum = randint(0, 1)
            rClass = class_variables[randnum]
        else:
            randnum = randint(1, 10)
            r = 0;
            if randnum > 1 and randnum < 5:
                r = 1
            elif randnum >= 5:
                r = 2
            rClass = class_variables[r]

        self.k += 1
        r = self.tables[rClass].next_row()
        return r.contents
