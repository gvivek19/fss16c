from sklearn import neural_network
from table import Table
from table import Column
import sys
import sklearn
from Num import Num
from Sym import Sym

class neural_network :
    def __init__(self, train_table):
        self.training_table = train_table
        self.fill_missing_values(self.training_table)

    def get_independent_cols_rows(self, table) :
        rows = []
        last_col = []

        for row in table.rows :
            r = []
            for c in self.training_table.cols[:-1]:
                if isinstance(c.col, Num):
                    r.append(row.contents[c.pos])
            rows.append(r)
            last_col.append(row[-1])
        return (rows, last_col)

    def fill_missing_values(self, table) :
        for row in table.rows :
            for col in table.cols :
                if row[col.pos] == Column.UNKNOWN :
                    if isinstance(self.training_table.cols[col.pos].col, Num) :
                        row[col.pos] = self.training_table.cols[col.pos].col.mu

    def train(self) :
        X, Y = self.get_independent_cols_rows(self.training_table)

        self.model = sklearn.neural_network.MLPRegressor()
        self.model.fit(X, Y)

    def predict(self, row) :
        pass

    def predict_all(self, test_table) :
        self.fill_missing_values(test_table)
        X, Y = self.get_independent_cols_rows(test_table)
        Y_predicted = self.model.predict(X)
        return zip(Y, Y_predicted)

if __name__ == '__main__':
    learner = neural_network(Table(sys.argv[1]))
    learner.train()
    results = learner.predict_all(Table(sys.argv[2]))
    print results
