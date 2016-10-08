#Week 5
Code can be found [here](https://github.com/gvivek19/fss16c/tree/master/code/5/code)
###To run the script
NB : python NaiveBayes.py \<training_dataset\> \<testing_dataset\>

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


We ran a 5x5 crossval using ninja and obtained the following runtimes:

| | data/arc.arff | data/jedit-4.3.arff | data/xerces-1.4.arff | data/xalan-2.7.arff | data/segment.arff | data/spambase.arff |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| Dataset size | 235 | 493 | 589 | 910 | 2310 | 4601 |
| naivebayes | 0.05396 | 0.08928 | 0.1164 | 0.14888 | 0.32032 | 1.3122 |
| knnkdtree | 0.20468 | 0.51168 | 0.67472 | 1.03576 | 1.70288 | 14.04168 |


###Performance (using the ninja scripts):
```
data/xerces-1.4.arff

pd
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    knnkdtree ,       0  ,    51 (*             -|------        ), 0.00,  0.00,  0.00, 48.00, 76.00
   1 ,   naivebayes ,      33  ,   100 (         *     |              ), 0.00,  0.00, 33.00, 100.00, 100.00
   1 ,    knnkmeans ,      67  ,   100 (-------        |    *         ), 0.00, 25.00, 67.00, 97.00, 100.00
pf
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    knnkmeans ,       1  ,     2 (*--            |              ), 0.00,  0.00,  1.00,  2.00,  5.00
   1 ,    knnkdtree ,       1  ,     4 (*-------       |              ), 0.00,  0.00,  1.00,  3.00, 13.00
   1 ,   naivebayes ,      10  ,    20 (      * -------|--            ), 0.00,  0.00, 10.00, 14.00, 29.00

```

**Compare the runtimes between your fastest knn device (from last week) and NaiveBayes.**

Naive Bayes is faster than the other knn learners

**Compare the performance between Bayes and your fastest KNN device (does doing it faster mean doing it wrong?)**

Naive Bayes has a relatively bad performance compared to the other learners for the datasets used here.

##Reports
```
data/arc.arff

naivebayes 1
naivebayes 2
naivebayes 3
naivebayes 4
naivebayes 5
real	0.05396

knnkdtree 1
knnkdtree 2
knnkdtree 3
knnkdtree 4
knnkdtree 5
real	0.20468

knnkmeans 1
knnkmeans 2
knnkmeans 3
knnkmeans 4
knnkmeans 5
real	0.19456

pd
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    knnkdtree ,      67  ,    92 (-------        |    *     --- ), 0.00, 25.00, 67.00, 90.00, 98.00
   1 ,   naivebayes ,      78  ,    90 (-------------  |       *  --- ), 0.00, 44.00, 78.00, 89.00, 100.00
   1 ,    knnkmeans ,      81  ,    68 (-------------- |        *  -- ), 0.00, 50.00, 83.00, 91.00, 98.00
pf
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    knnkmeans ,       5  ,    23 (  *  ----------|----          ), 0.00,  2.00,  7.00, 20.00, 67.00
   1 ,    knnkdtree ,       9  ,    48 (  *      ------|--------      ), 0.00,  3.00,  9.00, 33.00, 83.00
   1 ,   naivebayes ,      10  ,    22 (  *  ----------|------------- ), 0.00,  0.00, 10.00, 20.00, 100.00
```

```
data/jedit-4.3.arff

naivebayes 1
naivebayes 2
naivebayes 3
naivebayes 4
naivebayes 5
real	0.08928

knnkdtree 1
knnkdtree 2
knnkdtree 3
knnkdtree 4
knnkdtree 5
real	0.51168

knnkmeans 1
knnkmeans 2
knnkmeans 3
knnkmeans 4
knnkmeans 5
real	0.53788

pd
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,   naivebayes ,      90  ,    60 (---------------|-         *   ), 0.00, 60.00, 90.00, 100.00, 100.00
   1 ,    knnkdtree ,      92  ,   100 (               |            * ), 0.00,  0.00, 95.00, 100.00, 100.00
   1 ,    knnkmeans ,      99  ,    40 (---------------|----         *), 0.00, 67.00, 99.00, 100.00, 100.00
pf
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    knnkmeans ,       1  ,    20 (*--------------|------------- ), 0.00,  0.00,  1.00,  3.00, 100.00
   1 ,    knnkdtree ,       1  ,    75 (*              |    --------- ), 0.00,  0.00,  1.00, 67.00, 100.00
   1 ,   naivebayes ,      10  ,    10 (  *----------- |              ), 0.00,  0.00, 10.00, 10.00, 50.00

```

``` 
data/xerces-1.4.arff

naivebayes 1
naivebayes 2
naivebayes 3
naivebayes 4
naivebayes 5
real	0.1164

knnkdtree 1
knnkdtree 2
knnkdtree 3
knnkdtree 4
knnkdtree 5
real	0.67472

knnkmeans 1
knnkmeans 2
knnkmeans 3
knnkmeans 4
knnkmeans 5
real	0.7358

pd
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    knnkdtree ,       0  ,    51 (*             -|------        ), 0.00,  0.00,  0.00, 48.00, 76.00
   1 ,   naivebayes ,      33  ,   100 (         *     |              ), 0.00,  0.00, 33.00, 100.00, 100.00
   1 ,    knnkmeans ,      67  ,   100 (-------        |    *         ), 0.00, 25.00, 67.00, 97.00, 100.00
pf
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    knnkmeans ,       1  ,     2 (*--            |              ), 0.00,  0.00,  1.00,  2.00,  5.00
   1 ,    knnkdtree ,       1  ,     4 (*-------       |              ), 0.00,  0.00,  1.00,  3.00, 13.00
   1 ,   naivebayes ,      10  ,    20 (      * -------|--            ), 0.00,  0.00, 10.00, 14.00, 29.00
```

```
data/xalan-2.7.arff

naivebayes 1
naivebayes 2
naivebayes 3
naivebayes 4
naivebayes 5
real	0.14888

knnkdtree 1
knnkdtree 2
knnkdtree 3
knnkdtree 4
knnkdtree 5
real	1.03576

knnkmeans 1
knnkmeans 2
knnkmeans 3
knnkmeans 4
knnkmeans 5
real	1.4164

pd
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    knnkdtree ,      33  ,    67 (         *     |  --------    ), 0.00,  0.00, 33.00, 63.00, 87.00
   1 ,   naivebayes ,      67  ,    89 (------------   |    *  ------ ), 0.00, 43.00, 67.00, 80.00, 100.00
   1 ,    knnkmeans ,      77  ,    45 (---------------|----   *    - ), 0.00, 67.00, 78.00, 94.00, 100.00
pf
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    knnkmeans ,       1  ,     2 (*--            |              ), 0.00,  0.00,  1.00,  1.00, 11.00
   1 ,    knnkdtree ,       1  ,     6 (*----------    |              ), 0.00,  0.00,  1.00,  4.00, 37.00
   1 ,   naivebayes ,      10  ,    20 (--*----------- |              ), 0.00, 10.00, 10.00, 11.00, 50.00
```

```
data/segment.arff

naivebayes 1
naivebayes 2
naivebayes 3
naivebayes 4
naivebayes 5
real	0.32032

knnkdtree 1
knnkdtree 2
knnkdtree 3
knnkdtree 4
knnkdtree 5
real	1.70288

knnkmeans 1
knnkmeans 2
knnkmeans 3
knnkmeans 4
knnkmeans 5
real	4.82284

pd
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    knnkdtree ,      93  ,    12 (               |     ----- *  ),73.00, 87.00, 93.00, 97.00, 98.00
   1 ,    knnkmeans ,      98  ,     4 (               |           --*),93.00, 97.00, 98.00, 100.00, 100.00
   1 ,   naivebayes ,     100  ,     0 (              -|-------------*),50.00, 100.00, 100.00, 100.00, 100.00
pf
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    knnkmeans ,       0  ,     1 (*---           |              ), 0.00,  0.00,  0.00,  1.00,  3.00
   1 ,   naivebayes ,       0  ,     0 (*--------------|------------- ), 0.00,  0.00,  0.00,  0.00, 22.00
   1 ,    knnkdtree ,       2  ,     2 ( -*  ---       |              ), 1.00,  2.00,  2.00,  4.00,  6.00
```

```
data/spambase.arff

naivebayes 1
naivebayes 2
naivebayes 3
naivebayes 4
naivebayes 5
sys	0.00576
user	1.30992
real	1.3122

knnkdtree 1
knnkdtree 2
knnkdtree 3
knnkdtree 4
knnkdtree 5
sys	0.00912
user	14.02096
real	14.04168

knnkmeans 1
knnkmeans 2
knnkmeans 3
knnkmeans 4
knnkmeans 5
sys	0.01552
user	83.88176
real	84.0094

pd
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    knnkdtree ,      77  ,    19 (               |-     *  -    ),62.00, 68.00, 80.00, 87.00, 90.00
   1 ,   naivebayes ,      86  ,    29 (           ----|----    *     ),50.00, 75.00, 86.00, 100.00, 100.00
   2 ,    knnkmeans ,      95  ,     2 (               |          - * ),92.00, 94.00, 95.00, 96.00, 97.00
pf
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    knnkmeans ,       4  ,     1 ( *             |              ), 3.00,  4.00,  4.00,  5.00,  7.00
   2 ,   naivebayes ,      14  ,    25 (     *   ------|--            ), 0.00,  0.00, 14.00, 25.00, 50.00
   2 ,    knnkdtree ,      20  ,    19 (   --   *  --- |              ),10.00, 15.00, 23.00, 32.00, 38.00
```
