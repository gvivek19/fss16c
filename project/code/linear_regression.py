from sklearn import linear_model
from table import Table
from table import Column
import sys

class linear_regression :
    def __init__(self, train_table):
        self.training_table = train_table
        self.fill_missing_values(self.training_table)

    def get_independent_cols_rows(self, table) :
        rows = []
        last_col = []
        for row in table.rows :
            rows.append(row[:-1])
            last_col.append(row[-1])
        return (rows, last_col)

    def fill_missing_values(self, table) :
        for row in table.rows :
            for col in table.cols :
                if row[col.pos] == Column.UNKNOWN :
                    row[col.pos] = col.col.mu

    def train(self) :
        X, Y = self.get_independent_cols_rows(self.training_table)

        self.model = linear_model.LinearRegression()
        self.model.fit(X, Y)

    def predict(self, row) :
        pass

    def predict_all(self, test_table) :
        self.fill_missing_values(test_table)
        X, Y = self.get_independent_cols_rows(test_table)
        Y_predicted = self.model.predict(X)
        return zip(Y, Y_predicted)

if __name__ == '__main__':
    learner = linear_regression(Table(sys.argv[1]))
    learner.train()
    results = learner.predict_all(Table(sys.argv[2]))
    print results