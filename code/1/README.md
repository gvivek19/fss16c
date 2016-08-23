#Week 1

##Run something

###eg0:
eg0 prints the attributes present in the data followed by the dataset in an organized and readable format by printing the rows with 5 attributes with proper spacing and sorted based on the outlook attribute. Finally, it gives us the decision tree which can be used for future predictions built using the j4810 algorithm with does a 10-way cross validation. 

###eg1:
eg1 prints the weather dataset in an organized and readable format separated by spaces and sorted in ascending order based on the outlook attribute. Sorting the dataset using the outlook attribute makes it easier to show that the data can be split easily using the outlook attribute first when building the decision tree. Also, it prints all the rows which have only 5 attributes present.

###eg2:
eg2 prints the output of the j4810 algorithm with line numbers attached to each line. The output starts with the decision tree and the number of records associated with each leaf node. It then prints the total number of leaf nodes and total number of nodes. This data can be used when deciding whether to do pruning or not. The next information contains the total time taken to run the algorithm and train the learner. The next part of the output contains the confusion matrix and other metrics like true positive rate, true negative rate, error metrics, accuracy, etc. These metrics are also calculated after doing a 10-fold cross validation on the dataset. Doing a 10-fold cross-validation gives us a more useful insight about the learner.

###eg3:
eg3 calls the learner j48 with the same dataset as the training data and testing data. The output shows a perfect prediction for all the data in the testing data because both the training and testing data are the same giving a false impression that the learner works well.

###eg4:
eg4 obtains the output of eg3 and parses the output to print only the actual and predicted classes, removing all the unnecessary details. This makes the output more usable later.

###eg5:
eg5 takes the output of eg4 and calculates various metrics like the number of true positives, true negatives, false positives and false negatives. Using these values, accuracy, recall (probability of detection = pd), precision and probability of false alarm (pf) are calculated. From the output, we can conclude that the learner predicts is accurate 100%. This is because we tested it using the same data used for training.

###eg6:
eg6 performs a 1x3 cross validation on the data set and passes the dataset to 2 algorithms - j48 and jrip. Hence, for each algorithm, a 3-fold cross validation is run once and the output is processed to obtain the metrics which is displayed. Also, it uses stratified cross validation since the output is different for each of the cases as the rows are chosen randomly to run each iteration of the validation.

###eg7:
eg7 runs a 5x5 cross validation on the dataset i.e., it runs a 5-fold cross validation on the dataset 5 times for each algorithm. The algorithms used here are j48 and jrip. The output is then stored in a temp file and processed such that the learner, recall and learner, probability of failure are extracted and stored separately for all class = yes. 

###eg8:
eg8 performs the same operations as eg7 but instead uses the name of the column and the value in that column to filter so that it is easy to read and understand. A named column is a column in the table (The confusion matrix along with recall, accuracy and other details in this case) with a column name which can be used directly to filter out the necessary columns. This is more suitable to use because we don’t have to worry about the code when a new column is introduced in the table affecting the column id (the numbers used).

###eg9:
eg9 uses the output of eg8 and obtains a visualization of the data for each algorithm. The output contains a visual representation of the median along with the 10, 30, 50, 70 and the 90th percentile which is easy to understand where the data lies. Also, the rank of the algorithm, median and the interquartile range are displayed for each algorithm. In this case, the algorithms have the same rank as the values are similar.

What is the advantage (if any) of separating (a)the reporting of a data mining run (as done in eg9) from (b)the execution of that run (as done in eg8)?
The advantage of separating the data mining run(a) and the reporting(b) is that the reports can be run and modified independent of the data mining run. The data mining run is usually a time-consuming script and hence saves us a lot of time. 

###eg10:
We use 5 learners here - j48, jrip, nb, rbfnet and bnet. The script runs a 5x5 cross validation and stores the pd anf pf results separately which is then passed on to the report script for obtaining the report. The report shows a ranked list of the algorithms based on the pd and pf values along with a visualization of the values for each algorithm.

J48 : It uses the C4.5 algorithm which builds a tree in such a way that each split using an attribute is made such that the information gain is maximum due to that split. The algorithm then recurs using the remaining dataset and the remaining attributes.

NB: It assumes there is independence among the features. For a given set of features and training data, we calculate the probability of the new record belonging to all possible outcomes. The class is then predicted to be the class whose probability is the highest. 
