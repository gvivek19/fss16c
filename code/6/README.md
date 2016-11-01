#Week 6

The code is available in the repo. [Link](https://github.com/gvivek19/fss16c/tree/master/code/6/code)
##Data generator
The dataset used has been included in the repo. It was modified to include 3 classes only.

##Data reader
The result of the data reader is available [here](https://github.com/gvivek19/fss16c/blob/master/code/6/reports/anamoly.txt)
```
Era 1
Class = window, recall 0.79
Class = path, recall 0.95


Era 2
Class = window, recall 0.89
Class = path, recall 0.93


Era 3
Class = window, recall 0.91
Class = path, recall 0.91


Era 4
Class = window, recall 0.91
Class = path, recall 0.98


Era 5
Class = window, recall 0.96
Class = path, recall 0.94


Era 6
Class = window, recall 0.90
Class = path, recall 0.96


Era 7
Class = window, recall 0.96
Class = path, recall 0.98


Era 8
Class = window, recall 0.90
Class = path, recall 0.94


Era 9
Class = window, recall 0.98
Class = path, recall 0.98


Era 10
Class = window, recall 0.93
Class = path, recall 0.92
Class = brickface, recall 0.00


Era 11
Class = window, recall 0.83
Class = path, recall 1.00
Class = brickface, recall 0.68


Era 12
Class = window, recall 0.82
Class = path, recall 1.00
Class = brickface, recall 0.58


Era 13
Class = window, recall 0.72
Class = path, recall 0.92
Class = brickface, recall 0.65


Era 14
Class = window, recall 0.75
Class = path, recall 1.00
Class = brickface, recall 0.69


Era 15
Class = window, recall 0.88
Class = path, recall 0.92
Class = brickface, recall 0.75


Era 16
Class = window, recall 0.61
Class = path, recall 1.00
Class = brickface, recall 0.74


Era 17
Class = window, recall 0.81
Class = path, recall 1.00
Class = brickface, recall 0.68


Era 18
Class = window, recall 0.79
Class = path, recall 1.00
Class = brickface, recall 0.63


Era 19
Class = window, recall 0.86
Class = path, recall 1.00
Class = brickface, recall 0.67


Era 20
Class = window, recall 0.68
Class = path, recall 1.00
Class = brickface, recall 0.68
```
##Incremental learner
The prediction is made and the log of the likelihood of that prediction is also printed.
The link for the log file is [available here](https://github.com/gvivek19/fss16c/blob/master/code/6/reports/logs.txt).
```
Era 1
Expected : window, 		Predicted : window, 		Log of likelihood : -74.14
Expected : window, 		Predicted : window, 		Log of likelihood : -58.28
Expected : window, 		Predicted : window, 		Log of likelihood : -100.43
Expected : window, 		Predicted : window, 		Log of likelihood : -57.69
Expected : path, 		Predicted : path, 		Log of likelihood : -76.93
Expected : path, 		Predicted : path, 		Log of likelihood : -55.44
Expected : path, 		Predicted : path, 		Log of likelihood : -55.41
Expected : path, 		Predicted : path, 		Log of likelihood : -56.62
Expected : window, 		Predicted : window, 		Log of likelihood : -59.11
Expected : path, 		Predicted : path, 		Log of likelihood : -85.15
...
```

##Anamoly detector
The a12 test was used to predict the anamoly. If the A12 value is >= 0.71, then there is anamoly detected.
```
Era 1
Class = window, recall 0.79
Class = path, recall 0.95


Era 2
Class = window, recall 0.89
Class = path, recall 0.93


Era 3
Class = window, recall 0.91
Class = path, recall 0.91


Era 4
Class = window, recall 0.91
Class = path, recall 0.98


Era 5
Class = window, recall 0.96
Class = path, recall 0.94


Era 6
Class = window, recall 0.90
Class = path, recall 0.96


Era 7
Class = window, recall 0.96
Class = path, recall 0.98


Era 8
Class = window, recall 0.90
Class = path, recall 0.94


Era 9
Class = window, recall 0.98
Class = path, recall 0.98


Era 10
Class = window, recall 0.93
Class = path, recall 0.92
Class = brickface, recall 0.00
Anamoly detected


Era 11
Class = window, recall 0.83
Class = path, recall 1.00
Class = brickface, recall 0.68


Era 12
Class = window, recall 0.82
Class = path, recall 1.00
Class = brickface, recall 0.58


Era 13
Class = window, recall 0.72
Class = path, recall 0.92
Class = brickface, recall 0.65


Era 14
Class = window, recall 0.75
Class = path, recall 1.00
Class = brickface, recall 0.69


Era 15
Class = window, recall 0.88
Class = path, recall 0.92
Class = brickface, recall 0.75


Era 16
Class = window, recall 0.61
Class = path, recall 1.00
Class = brickface, recall 0.74


Era 17
Class = window, recall 0.81
Class = path, recall 1.00
Class = brickface, recall 0.68


Era 18
Class = window, recall 0.79
Class = path, recall 1.00
Class = brickface, recall 0.63


Era 19
Class = window, recall 0.86
Class = path, recall 1.00
Class = brickface, recall 0.67


Era 20
Class = window, recall 0.68
Class = path, recall 1.00
Class = brickface, recall 0.68
```
