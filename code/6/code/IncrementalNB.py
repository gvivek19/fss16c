import sys, table, collections, math, MyUtils, NaiveBayes
from random import randint
import DataGenerator
from time import time
import Num


class IncrementalNB:
	def __init__(self, datagen) :
		self.dataGenerator = datagen
		self.train_table = table.Table()
		self.classes = []

	def next_batch(self, table1, rowcount):
		for i in range(0, rowcount):
			r = self.dataGenerator.get_next()
			if r[-1] not in self.classes:
				self.classes.append(r[-1])
			table1.add_row(r)

	def copy_table(self, table1, table2):
		for row in table2.rows:
			table1.add_row(row.contents)

	def compute_recall(self, results):
		for current_positive in self.classes:
			b = 0.0
			d = 0.0
			for prediction in results:
				actual = prediction[0]
				predicted = prediction[1]
				print 'Expected : %s, \t\tPredicted : %s, \t\tLog of likelihood : %.2f' % (str(actual), str(predicted), math.log(prediction[2]))
				if actual == current_positive :
					if predicted == current_positive :
						d += 1
					else :
						b += 1
			#print 'Class = %s, recall %.2f' % (str(current_positive), (d / (b + d)))
				#pd = D/(B+D)
				#False negagive= B => actual = positive; predicted = negative
				#True positive = D => actual = positive; predicted = positive
	def process_batch(self, old_results, results):
		likelihood_old = [math.log(x[2]) for x in old_results]
		likelihood_new = [math.log(x[2]) for x in results]

		score = MyUtils.a12slow(likelihood_old, likelihood_new)
		if score >= 0.71 :
			print "Anamoly detected"

	def incremental_NB(self):
		size = self.dataGenerator.get_row_count()
		numeras = size / 100

		self.next_batch(self.train_table, 100)
		prev_results = None
		for i in range(0, numeras):
			print 'Era ' + str(i + 1)
			nb = NaiveBayes.NaiveBayes(self.train_table)
			test_table = table.Table()
			self.next_batch(test_table, 100)
			results = nb.predict_all(test_table)
			self.compute_recall(results)
			if prev_results is not None:
				self.process_batch(prev_results, results)
			prev_results = results
			self.copy_table(self.train_table, test_table)
			print '\n'

if __name__ == "__main__":
	t = table.Table(sys.argv[1])
	dataGenerator = DataGenerator.DataGenerator(t)
	inb = IncrementalNB(dataGenerator)
	inb.incremental_NB()
