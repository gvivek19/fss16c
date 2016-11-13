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
        self.tables.append(table)
        self.k = k

    def row_distance(self, row1, row2) :
        distance = 0
        for col in self.table.cols[:-1]:
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
        print "NTL", len(new_trees)
        return self.gac_helper(new_table, new_trees)

    def gac(self, table) :
        trees = []
        for i, row in enumerate(table.rows):
            tree = Tree(0, row.rid, i, None, None)
            tree.effort_values.append(row.contents[-1])
            trees.append(tree)
        return self.gac_helper(table, trees)

    def prune(self, tree):
        if tree == None or tree.left == None and tree.right == None:
            return
        num_root = Num.Num()
        num_left = Num.Num()
        num_right = Num.Num()
        
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
        self.prune(tree.left)
        self.prune(tree.right)

    def tree2table(self, table, tree):
    	if tree is None:
    		return
    	if tree.left is None and tree.right is None:
            table.append(self.table.rows[tree.row_index])
        self.tree2table(self, table, tree.left)
        self.tree2table(self, table, tree.right)

    def train(self):
		cluster_tree = self.gac(self.table)
		self.printTree(cluster_tree)
		pruned_tree = self.prune(cluster_tree)
		#pruned_table = table.clone(self.table)
		#self.tree2table(pruned_table, pruned_tree)
		#print pruned_table.rows
		#self.model = self.gac(pruned_table)
		#print self.model

    def printTree(self, tree) :
	if tree is None:
	    return
	print self.tables[tree.table_id].rows[tree.row_index]
	self.printTree(tree.left)
	self.printTree(tree.right)

    def predict_helper(self, tree, row):
        pass

    def predict(self, row):
        tree = self.model
        return predict_helper(tree, row)

if __name__ == '__main__':
	team = Teak(table.Table(sys.argv[1]), 3)
	team.train()
