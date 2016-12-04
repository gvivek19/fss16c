import sys, table, collections, math, MyUtils
import random
from time import time
from Num import Num
from Sym import Sym
from table import Column
from ABE import ABE
class Node:
    def __init__(self, id, left, right, contents):
        self.id = id
        self.left_node = left
        self.right_node = right
        self.contents = contents

class Tree:
    def __init__(self, sample_table):
        self.table = table.clone(sample_table)

    def centroid(self, tbl):
        centroid = []
        for col in tbl.cols:
            if isinstance(col.col, Num) :
                numbers = [row[col.pos] for row in tbl.rows]
                centroid.append(MyUtils.median(numbers))
            elif isinstance(col.col, Sym) :
                centroid.append(col.col.mode)
            else :
                centroid.append(Column.UNKNOWN)
        return centroid

    def new_node(self, left_node, right_node, leaf_node = None):
        contents = table.clone(self.table)

        if left_node is not None:
            for row in left_node.contents.rows :
                contents.add_row(row)
        if right_node is not None:
            for row in right_node.contents.rows :
                contents.add_row(row)
        if leaf_node is not None:
            contents.add_row(leaf_node)

        c = self.centroid(contents)
        self.table.add_row(c)
        nodeid = len(self.table.rows) - 1

        return Node(nodeid, left_node, right_node, contents)

    def nearest_node(self, nodes, nde):
        nearest = None
        nearest_distance = 0
        for node in nodes:
            if node.id != nde.id:
                dist = self.table.row_distance(self.table.rows[node.id], self.table.rows[nde.id])
                if nearest is None or nearest_distance > dist:
                    nearest = node
                    nearest_distance = dist
        return nearest

    def gac(self, nodes):
        if len(nodes) == 1:
            self.root = nodes[0]
            return

        new_nodes = []
        while len(nodes) > 1 :
            node = nodes[0]
            nearest = self.nearest_node(nodes, node)
            nnode = self.new_node(node, nearest)
            new_nodes.append(nnode)
            nodes.remove(node)
            nodes.remove(nearest)

        if len(nodes) > 0:
            new_nodes.append(nodes[0])

        self.gac(new_nodes)

    def __print_tree(self, node):
        print self.table.rows[node.id]
        if node.left_node:
            self.__print_tree(node.left_node)
        if node.right_node:
            self.__print_tree(node.right_node)

    def print_tree(self):
        self.__print_tree(self.root)

    def __traverse(self, node, row, k) :
        if len(node.contents.rows) <= k :
            return self.table.rows[node.id][-1]

        nodes = [node.left_node, node.right_node]
        return self.__traverse(self.nearest_node(nodes, node), row, k)

    def traverse(self, row, k):
        return self.__traverse(self.root, row, k)

    def __traverse2(self, node, row, k) :
        if len(node.contents.rows) <= k :
            return self.table.rows[node.id][-1]

        num_left_node = len(node.left_node.contents.rows)
        num_right_node = len(node.right_node.contents.rows)
        num_node = len(node.contents.rows)

        var_curr_node = node.contents.cols[-1].col.sd() ** 2
        var_left_node = node.left_node.contents.cols[-1].col.sd() ** 2
        var_right_node = node.right_node.contents.cols[-1].col.sd() ** 2
        var_subtree = (float(num_left_node) / num_node * var_left_node) + (float(num_right_node) / num_node * var_right_node)

        nodes = [node.left_node, node.right_node]
        nearest_node = self.nearest_node(nodes, node)

        if var_subtree > var_node:
            return self.table.rows[node.id][-1]

        return self.__traverse2(nearest_node, row, k)

    def traverse2(self, row, k):
        return self.__traverse(self.root, row, k)

    def prune(self, gamma, node = None):
        if node is None:
            node = self.root

        var_node = node.contents.cols[-1].col.sd() ** 2
        var_root = self.root.contents.cols[-1].col.sd() ** 2

        if len(node.contents.rows) <= 1:
            return

        num_left = len(node.left_node.contents.rows)
        num_right = len(node.right_node.contents.rows)
        num_node = num_left + num_right


        var_left = node.left_node.contents.cols[-1].col.sd() ** 2
        var_right = node.right_node.contents.cols[-1].col.sd() ** 2

        var_subtree = (float(num_left) / num_node) * var_left + (float(num_right) / num_node) * var_right

        metric = random.random() ** gamma * var_node + var_node
        # print var_subtree, metric, var_node
        if var_subtree > metric :
            # print "pruned", num_node
            node.left_node = None
            node.right_node = None
        else :
            self.prune(gamma, node.left_node)
            self.prune(gamma, node.right_node)

    def tree2table(self, tbl = None, node = None):
        if tbl is None:
            tbl = table.clone(self.table)
        if node is None:
            node = self.root

        if node.left_node is None and node.right_node is None:
            tbl.add_row(self.table.rows[node.id])
        else :
            self.tree2table(tbl, node.left_node)
            self.tree2table(tbl, node.right_node)
        return tbl

class Teak:
    def __init__(self, train_table, k=3, gamma=9):
        self.train_table = train_table
        self.fill_missing_values(self.train_table)
        self.k = k
        self.gamma = gamma
        self.cluster_tree = None
        self.model = None

    def fill_missing_values(self, table) :
        for row in table.rows :
            for col in table.cols :
                if row[col.pos] == Column.UNKNOWN :
                    if isinstance(self.train_table.cols[col.pos].col, Num) :
                        row[col.pos] = self.train_table.cols[col.pos].col.mu


    def gac(self, tbl):
        tree = Tree(tbl)
        nodes = []

        for row in tbl.rows :
            nodes.append(tree.new_node(None, None, row.contents))

        tree.gac(nodes)
        return tree

    def train(self, prune = True):
        gac1 = self.gac(self.train_table)
        if prune :
            gac1.prune(self.gamma)
            pruned_table = gac1.tree2table()
            # print len(self.train_table.rows), len(pruned_table.rows)
            gac2 = self.gac(pruned_table)
            self.model = gac2
        else :
            self.model = gac1

    def predict(self, row):
        return (row[-1], self.model.traverse(row, self.k))

    def predict_all(self, test_table):
        return [self.predict(row.contents) for row in test_table.rows]

    def predict_all2(self, test_table):
        return [(row[-1], self.model.traverse2(row, self.k)) for row in test_table.rows]

if __name__ == '__main__':
	import config
	for url in config.datasets:
		print url
		team = Teak(table.Table(config.base_dir + url), 3)
		team.train()
