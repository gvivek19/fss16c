#Week 8

##Datasets
* Obtained from WEKA repository. 
* The details about the datasets used are listed below


| Dataset | URL | #Instances | #Attributes |
| ------- | ------- | ------- | ------- |
| Iris | [Iris](http://storm.cis.fordham.edu/~gweiss/data-mining/weka-data/iris.arff) | 150 | 4 |
| Ionosphere | [Ionosphere](http://storm.cis.fordham.edu/~gweiss/data-mining/weka-data/ionosphere.arff) | 351 | 34 |
| Vote | [Vote](http://storm.cis.fordham.edu/~gweiss/data-mining/weka-data/vote.arff) | 435 | 16 |
| Diabetes | [Diabetes](http://storm.cis.fordham.edu/~gweiss/data-mining/weka-data/diabetes.arff) | 768 | 8 |
| Segment challenge | [Segment challenge](http://storm.cis.fordham.edu/~gweiss/data-mining/weka-data/segment-challenge.arff) | 1500 | 19 |
| Sick | [Sick](http://repository.seasr.org/Datasets/UCI/arff/sick.arff) | 3772 | 29 |

##Feature selection using J48 M trick:
| | #Features | | Recall | | Precision | |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| Dataset | All | Selected | All | Selected | All | Selected |
| Iris | 4 | 1 | 0.94 | 0.94 | 0.94 | 0.887 |
| Ionosphere | 34 | 2 | 0.964 | 0.938 | 0.908 | 0.913 |
| Vote | 16 | 1 | 0.97 | 0.948 | 0.97 | 0.981 |
| Diabetes | 8 | 2 | 0.814 | 0.858 | 0.79 | 0.776 |
| Segment challenge | 19 | 5 | 0.956 | 0.834 | 0.975 | 0.929 |
| Sick | 29 | 5 | 0.995 | 0.992 | 0.992 | 0.988 |


##Feature selection using Wrapper:
| | #Features | | Recall | | Precision | |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| Dataset | All | Selected | All | Selected | All | Selected |
| Iris | 4 | 1 | 0.94 | 0.96 | 0.94 | 0.889 |
| Ionosphere | 34 | 2 | 0.964 | 0.987 | 0.908 | 0.925 |
| Vote | 16 | 1 | 0.97 | 0.948 | 0.97 | 0.981 |
| Diabetes | 8 | 4 | 0.814 | 0.842 | 0.79 | 0.797 |
| Segment challenge | 19 | 4 | 0.956 | 0.971 | 0.975 | 0.948 |
| Sick | 29 | 9 | 0.995 | 0.995 | 0.992 | 0.993 |


##Feature selection using CFS:
| | #Features | | Recall | | Precision | |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| Dataset | All | Selected | All | Selected | All | Selected |
| Iris | 4 | 1 | 0.94 | 0.94 | 0.94 | 0.887 |
| Ionosphere | 34 | 2 | 0.964 | 0.938 | 0.908 | 0.913 |
| Vote | 16 | 1 | 0.97 | 0.948 | 0.97 | 0.981 |
| Diabetes | 8 | 2 | 0.814 | 0.858 | 0.79 | 0.776 |
| Segment challenge | 19 | 5 | 0.956 | 0.834 | 0.975 | 0.929 |
| Sick | 29 | 5 | 0.995 | 0.992 | 0.992 | 0.988 |
