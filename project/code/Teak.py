import sys, table, collections, math, MyUtils
import random
from time import time
import Num
import ABE
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
        self.tables = []
        self.tables.add(table)
        self.k = k

    def row_distance(self, row1, row2) :
        distance = 0
        for col in table.cols[:-1]:
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
        return self.find_best(row, 10**32, MyUtils.less)

    def centroid(self, row1, row2):
        result = []
        row1_contents = row1.contents
        if (row2 != None):
            row2_contents = row2.contents
        else:
            row2_contents = [0 for i in range(0,len(row1))]
        for i in range(0,len(row1)):
            result.add((row1_contents[i] + row2_contents[i]) / 2)
        return result

    def find_trees(self, trees, left_row, right_row):
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
            rows.add(row)
        new_table = table.clone(curr_table)
        new_trees = []
        row_index = 0
        for row in rows:
            nearest = self.find_nearest(rows, row)
            rid = new_table.add_row(centroid(nearest, row))
            left_tree, right_tree = find_trees(trees, row, nearest)
            new_tree = Tree(len(tables), rid, row_index, left_tree, right_tree)
            new_trees.add(new_tree)
            rows.remove(row)
            rows.remove(nearest)
            row_index += 1
        self.tables.add(new_table)
        return gac_helper(new_table, new_tree)

    def gac(self, table) :
        trees = []
        for row in table.rows:
            tree = Tree(0, row.rid, None, None);
            tree.effort_values.add(row.contents[-1])
            trees.add(tree)
        return gac_helper(table, trees)

    def prune(self, tree):
        if tree == None or tree.left == None and tree.right == None:
            return
        num_root = Num()
        num_left = Num()
        num_right = Num()
        for effort in tree.effort_values:
            num_root.add(effort)
        for effort in tree.left.effort_values:
            num_left.add(effort)
        for effort in tree.right.effort_values:
            num_right.add(effort)
        num_root_sd = num_root.sd()
        num_left_sd = num_left.sd()
        num_right_sd = num_right.sd()
        if num_root_sd < num_left_sd:
            tree.left = None
        if num_root_sd < num_right_sd:
            tree.right = None
        prune(tree.left)
        prune(tree.right)

    def tree2table(self, table, tree):
    	if tree.left == None and tree.right == None:
            table.append(self.table.rows[tree.row_index])
        tree2table(self, table, tree.left)
        tree2table(self, table, tree.right)

    def train(self):
		cluster_tree = self.gac(self.table)
		pruned_tree = self.prune(cluster_tree)
		self.tree2table(pruned_table, pruned_tree)
		self.model = self.gac(pruned_table)

    def predict_helper(self, tree, row):
        pass

    def predict(self, row):
        tree = self.model
        return predict_helper(tree, row)
