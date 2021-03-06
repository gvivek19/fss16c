import sys, table, collections, math, MyUtils
import random
from time import time
from Num import Num
from Sym import Sym
from table import Column
from ABE import ABE

class Tree:
    def __init__(self, table_id, row_id, row_index, left, right):
        self.table_id = table_id
        self.row_id = row_id
        self.row_index = row_index
        self.left = left
        self.right = right
        self.effort_values = []

        if left != None:
            self.effort_values += left.effort_values

        if right != None:
            self.effort_values += right.effort_values

class Teak :
    def __init__(self, table, k) :
        self.table = table
        self.fill_missing_values(self.table)
        self.tables = []
        self.tables.append(table)
        self.k = k

    def fill_missing_values(self, table) :
        for row in table.rows :
            for col in table.cols :
                if row[col.pos] == Column.UNKNOWN :
                    if isinstance(self.table.cols[col.pos].col, Num) :
                        row[col.pos] = self.table.cols[col.pos].col.mu

    def row_distance(self, row1, row2) :
        if row1 is None or row2 is None:
            return 10**32
        distance = 0
        for col in self.table.cols[:-1]:
            if col.col is not None:
                distance += (col.col.dist(row1[col.pos], row2[col.pos]) ** 2)
        return math.sqrt(distance)

    def find_best(self, rows, row, init_dist, better):
        output = None
        distance = init_dist
        for r in rows :
            if r.rid != row.rid :
                current_distance = self.row_distance(row, r)
                if better(current_distance , distance) :
                    distance = current_distance
                    output = r
        return output

    def find_nearest(self, rows, row) :
        return self.find_best(rows, row, 10**32, MyUtils.less)

    def centroid(self, row1, row2):
        result = []
        row1_contents = row1.contents

        if (row2 is not None):
            row2_contents = row2.contents
        else:
            row2_contents = [0 for i in range(0,len(row1))]
        for i in range(0,len(row1)):
            if isinstance(row1_contents[i], int) and isinstance(row2_contents[i], int) :
            	result.append((row1_contents[i] + row2_contents[i]) / 2)
            else :
            	c = random.random()
            	if c < 0.5 :
            		result.append(row1_contents[i])
            	else :
            		result.append(row2_contents[i])
        return result

    def find_trees(self, trees, left_row, right_row):
        left_tree = None
        right_tree = None
        for tree in trees:
            if tree.row_id == left_row.rid:
                left_tree = tree
            elif tree.row_id == right_row.rid:
                right_tree = tree
        return left_tree, right_tree

    def gac_helper(self, curr_table, trees) :
        if len(trees) == 1:
            return trees[0]
        rows = []
        for row in curr_table.rows:
            rows.append(row)
        new_table = table.clone(curr_table)
        new_trees = []
        row_index = 0
        while len(rows) > 1 :
            row = rows[0]
            nearest = self.find_nearest(rows, row)
            rid = new_table.add_row(self.centroid(nearest, row))
            left_tree, right_tree = self.find_trees(trees, row, nearest)
            new_tree = Tree(len(self.tables), rid, row_index, left_tree, right_tree)
            new_trees.append(new_tree)
            rows.remove(row)
            rows.remove(nearest)
            row_index += 1
        if len(rows) == 1:
            rid = new_table.add_row(rows[0])
            left_tree, right_tree = self.find_trees(trees, rows[0], rows[0])
            new_tree = Tree(len(self.tables), rid, row_index, left_tree, None)
            new_trees.append(new_tree)
        self.tables.append(new_table)
        return self.gac_helper(new_table, new_trees)

    def gac(self, table) :
        trees = []
        for i, row in enumerate(table.rows):
            tree = Tree(0, row.rid, i, None, None)
            tree.effort_values.append(row.contents[-1])
            trees.append(tree)
        return self.gac_helper(table, trees)

    def prune(self, tree):
        if tree == None or (tree.left == None and tree.right == None):
            return
        num_root = Num()
        num_left = Num()
        num_right = Num()

        for effort in tree.effort_values:
            num_root.add(effort)

        if tree.left is not None :
            for effort in tree.left.effort_values:
                num_left.add(effort)

        if tree.right is not None:
            for effort in tree.right.effort_values:
                num_right.add(effort)

        num_root_var = num_root.sd() ** 2
        num_left_var = num_left.sd() ** 2
        num_right_var = num_right.sd() ** 2

        max_var = num_root_var if num_root_var > num_left_var else num_left_var
        max_var = max_var if max_var > num_right_var else num_right_var

        R = random.random()
        metric = (R ** 9) * max_var

        if (num_left_var > num_root_var + metric):
            tree.left = None

        if (num_right_var > num_root_var + metric):
            tree.right = None

        self.prune(tree.left)
        self.prune(tree.right)

        return tree

    def tree2table(self, table, tree):
    	if tree is None:
    		return
    	if tree.left is None and tree.right is None:
            table.add_row(self.table.rows[tree.row_index])
        self.tree2table(table, tree.left)
        self.tree2table(table, tree.right)

    def train(self):
        cluster_tree = self.gac(self.table)
        #pruned_tree = self.prune(cluster_tree)
        #pruned_table = table.clone(self.table)
        #self.tree2table(pruned_table, pruned_tree)
        self.model = cluster_tree
        #self.gac(pruned_table)

    def get_tree_row(self, node):
        if node is None :
            return None
        return self.tables[node.table_id].rows[node.row_index].contents

    def predict_helper(self, tree, row):
        if (len(tree.effort_values) <= self.k):
            return self.get_tree_row(tree)[-1]
        if self.row_distance(self.get_tree_row(tree.left), row) < self.row_distance(self.get_tree_row(tree.right), row) :
            return self.predict_helper(tree.left, row)
        else:
            return self.predict_helper(tree.right, row)

    def predict(self, row):
        tree = self.model
        return (row[-1], self.predict_helper(tree, row))

    def predict_all(self, test_table) :
        import config
        abe = ABE(self.table, config.abe_k[0])
        return [ (self.predict(row.contents), abe.predict(row)) for row in test_table.rows]

if __name__ == '__main__':
	import config
	for url in config.datasets:
		print url
		team = Teak(table.Table(config.base_dir + url), 3)
		team.train()
