#Week 4

Code can be found [here](https://github.com/gvivek19/fss16c/tree/master/code/4/code)
###To run the script
KNN : python KNN.py \<training_dataset\> \<testing_dataset\>

KNN+mini-batch : python KNN.py \<training_dataset\> \<testing_dataset\> KMeans

KNN+KDTree : python KNN.py \<training_dataset\> \<testing_dataset\> KDTree

###Datasets used:

| Dataset | URL | size | filename | goal |
| ------- | ------- | ------- | ------- | ------- |
| DEFECT/CK/ARC | https://terapromise.csc.ncsu.edu/!/#repo/view/head/defect/ck/arc/arc.csv | 235 | arc.arff | 0 |
| DEFECT/CK/JEDIT | https://terapromise.csc.ncsu.edu/!/#repo/view/head/defect/ck/jedit/jedit-4.3.csv | 493 | jedit-4.3.arff | 1 |
| DEFECT/CK/XERCES | https://terapromise.csc.ncsu.edu/!/#repo/view/head/defect/ck/xerces/xerces-1.4.csv | 589 | xerces-1.4.arff | 1 |
| DEFECT/CK/XALAN | https://terapromise.csc.ncsu.edu/!/#repo/view/head/defect/ck/xalan/xalan-2.7.csv | 910 | xalan-2.7.arff | 0 |
| SEGMENT | https://repository.seasr.org/Datasets/UCI/arff/segment.arff | 2310 | segment.arff | brickface |
| SPAMBASE | https://repository.seasr.org/Datasets/UCI/arff/spambase.arff | 4601 | spambase.arff | 1 |


We ran a 5x5 crossval using ninja and obtained the following outputs

###Runtimes (for 1 iteration in crossval):
```
data/spambase.arff

plainknn 1
real	776.2018

knnkdtree 1
real	38.0666

knnkmeans 1
real	183.5346
```

###Performance (using the ninja scripts):
```
data/spambase.arff

pd
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    knnkdtree ,      70  ,    23 (------         | *      --    ),60.00, 68.00, 82.00, 90.00, 93.00
   2 ,    knnkmeans ,      95  ,     2 (               |          - * ),93.00, 94.00, 95.00, 96.00, 97.00
   2 ,     plainknn ,      95  ,     2 (               |           - *),94.00, 95.00, 96.00, 97.00, 97.00
pf
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,     plainknn ,       4  ,     2 ( *-            |              ), 3.00,  4.00,  5.00,  6.00,  7.00
   1 ,    knnkmeans ,       5  ,     1 ( *-            |              ), 3.00,  4.00,  5.00,  5.00,  7.00
   2 ,    knnkdtree ,      18  ,    22 (     ---       |     *    --- ),10.00, 13.00, 30.00, 36.00, 40.00

```

**Compare the runtimes between raw kNN and kNN+KD-trees or kNN+mini-batch**

kNN+KDTree is faster than kNN 

**Compare the performance between kNN and KD-trees (does doing it faster mean doing it wrong?)**

kNN has the lowest pd and highest pf. Hence, it is the best learner for the dataset considered here.


##Report
```
data/arc.arff

pd
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    knnkdtree ,      67  ,    92 (-------        |    *     --- ), 0.00, 25.00, 67.00, 90.00, 98.00
   1 ,    knnkmeans ,      81  ,    73 (-------------- |        *  -- ), 0.00, 50.00, 81.00, 93.00, 97.00
   1 ,     plainknn ,      84  ,    45 (-------------- |          * - ), 0.00, 50.00, 88.00, 95.00, 100.00
pf
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    knnkmeans ,       5  ,    31 ( *     --------|-----         ), 0.00,  2.00,  5.00, 25.00, 71.00
   1 ,     plainknn ,       5  ,    23 ( *   --------- |              ), 0.00,  2.00,  5.00, 20.00, 50.00
   1 ,    knnkdtree ,       9  ,    48 (  *      ------|--------      ), 0.00,  3.00,  9.00, 33.00, 83.00
```
```
data/jedit-4.3.arff

pd
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    knnkdtree ,      92  ,   100 (               |            * ), 0.00,  0.00, 95.00, 100.00, 100.00
   1 ,    knnkmeans ,      99  ,    40 (---------------|----         *), 0.00, 67.00, 99.00, 100.00, 100.00
   1 ,     plainknn ,     100  ,    33 (---------------|-------------*), 0.00, 99.00, 100.00, 100.00, 100.00
pf
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    knnkmeans ,       0  ,     3 (*--------------|-------       ), 0.00,  0.00,  0.00,  3.00, 80.00
   1 ,     plainknn ,       0  ,     2 (*--------------|-------       ), 0.00,  0.00,  0.00,  1.00, 80.00
   1 ,    knnkdtree ,       1  ,    75 (*              |    --------- ), 0.00,  0.00,  1.00, 67.00, 100.00
```
```
data/xerces-1.4.arff

pd
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    knnkdtree ,       0  ,    51 (*             -|------        ), 0.00,  0.00,  0.00, 48.00, 76.00
   1 ,    knnkmeans ,      70  ,   100 (---------      |     *        ), 0.00, 33.00, 71.00, 100.00, 100.00
   1 ,     plainknn ,      80  ,    67 (-------------- |       *      ), 0.00, 50.00, 80.00, 100.00, 100.00
pf
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    knnkmeans ,       1  ,     2 (*--            |              ), 0.00,  0.00,  1.00,  2.00,  5.00
   1 ,    knnkdtree ,       1  ,     4 (*-------       |              ), 0.00,  0.00,  1.00,  3.00, 13.00
   1 ,     plainknn ,       1  ,     2 (*--            |              ), 0.00,  0.00,  1.00,  2.00,  5.00
```
```
data/xalan-2.7.arff

pd
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    knnkdtree ,      33  ,    67 (         *     |  --------    ), 0.00,  0.00, 33.00, 63.00, 87.00
   1 ,    knnkmeans ,      75  ,    48 (---------------|----   *    - ), 0.00, 67.00, 77.00, 96.00, 100.00
   1 ,     plainknn ,      77  ,    46 (---------------|----   *    - ), 0.00, 67.00, 77.00, 94.00, 100.00
pf
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    knnkmeans ,       1  ,     2 (*------        |              ), 0.00,  0.00,  1.00,  2.00, 15.00
   1 ,    knnkdtree ,       1  ,     6 (*--------------|--            ), 0.00,  0.00,  1.00,  4.00, 37.00
   1 ,     plainknn ,       1  ,     2 (*-----         |              ), 0.00,  0.00,  1.00,  1.00, 14.00
```
```
data/segment.arff

pd
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    knnkdtree ,      93  ,    12 (      ---------|--     *   -  ),73.00, 87.00, 93.00, 97.00, 98.00
   2 ,    knnkmeans ,      98  ,     4 (               |       ---  * ),93.00, 96.00, 98.00, 100.00, 100.00
   2 ,     plainknn ,     100  ,     1 (               |           --*),97.00, 99.00, 100.00, 100.00, 100.00
pf
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    knnkmeans ,       0  ,     0 (*------        |              ), 0.00,  0.00,  0.00,  0.00,  2.00
   1 ,     plainknn ,       0  ,     0 (*              |              ), 0.00,  0.00,  0.00,  0.00,  0.00
   2 ,    knnkdtree ,       2  ,     2 (   ----*      -|------        ), 1.00,  2.00,  2.00,  4.00,  6.00
```
```
data/spambase.arff

pd
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    knnkdtree ,      70  ,    23 (------         | *      --    ),60.00, 68.00, 82.00, 90.00, 93.00
   2 ,    knnkmeans ,      95  ,     2 (               |          - * ),93.00, 94.00, 95.00, 96.00, 97.00
   2 ,     plainknn ,      95  ,     2 (               |           - *),94.00, 95.00, 96.00, 97.00, 97.00
pf
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,     plainknn ,       4  ,     2 ( *-            |              ), 3.00,  4.00,  5.00,  6.00,  7.00
   1 ,    knnkmeans ,       5  ,     1 ( *-            |              ), 3.00,  4.00,  5.00,  5.00,  7.00
   2 ,    knnkdtree ,      18  ,    22 (     ---       |     *    --- ),10.00, 13.00, 30.00, 36.00, 40.00
```

###Runtimes:

| | data/arc.arff | data/jedit-4.3.arff | data/xerces-1.4.arff | data/xalan-2.7.arff | data/segment.arff | data/spambase.arff |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| Dataset size | 235 | 493 | 589 | 910 | 2310 | 4601 |
| plainknn | 0.5794 | 1.96284 | 3.03004 | 6.24896 | 84.382 | 776.2018 |
| knnkdtree | 0.2882 | 0.60864 | 0.90212 | 1.46704 | 4.06232 | 38.0666 |
| knnkmeans | 0.28896 | 0.59352 | 0.95544 | 2.22656 | 12.5044 | 183.5346 |
