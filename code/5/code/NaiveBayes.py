from table import Table
import MyUtils, sys

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
            existing_table = self.tables.get(row_class, MyUtils.clone(table))
            existing_table.add_row(row.contents)
            self.tables[row_class] = existing_table
    
    def predict(self, row):
        pass
    
if __name__ == "__main__":
    nb = NaiveBayes(Table(sys.argv[1]))
    predictions = nb.predictAll(sys.argv[2])
    MyUtils.showResults(predictions);