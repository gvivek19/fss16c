#Week 4

Code can be found [here](https://github.com/gvivek19/fss16c/tree/master/code/4/code)
###To run the script
KNN : python KNN.py \<training_dataset\> \<testing_dataset\>

KNN+mini-batch : python KNN.py \<training_dataset\> \<testing_dataset\> KMeans

KNN+KDTree : python KNN.py \<training_dataset\> \<testing_dataset\> KDTree


We ran a 5x5 crossval using ninja and obtained the following outputs

###Runtimes (for 1 iteration in crossval):

```
KNN

real    0m0.490s
user    0m0.396s
sys     0m0.020s

KNN + KMeans

real    0m0.391s
user    0m0.344s
sys     0m0.052s

KNN + KDTree

real    0m1.686s
user    0m1.656s
sys     0m0.028s
```

###Comparison of performance:
```

NINJA: workspace/ninja 160> eg12
plainknn 1
plainknn 2
plainknn 3
plainknn 4
plainknn 5
knnkmeans 1
knnkmeans 2
knnkmeans 3
knnkmeans 4
knnkmeans 5
knnkdtree 1
knnkdtree 2
knnkdtree 3
knnkdtree 4
knnkdtree 5

pd

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    knnkmeans ,       0  ,     0 (*              |              ), 0.00,  0.00,  0.00,  0.00,  0.00
   2 ,    knnkdtree ,      52  ,    28 (        ----   |*  ------     ),27.00, 38.00, 52.00, 60.00, 78.00
   2 ,     plainknn ,      61  ,    15 (              -|-  * --       ),44.00, 53.00, 61.00, 65.00, 73.00
pf

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    knnkmeans ,       0  ,     0 (*              |              ), 0.00,  0.00,  0.00,  0.00,  0.00
   2 ,     plainknn ,       7  ,     7 ( --   *  ----  |              ), 2.00,  4.00,  7.00, 11.00, 15.00
   3 ,    knnkdtree ,      10  ,     9 (   ----- *  ---|--            ), 4.00,  9.00, 10.00, 14.00, 20.00
```

**Compare the runtimes between raw kNN and kNN+KD-trees or kNN+mini-batch**

kNN+mini-batch is faster than kNN

**Compare the performance between kNN and KD-trees (does doing it faster mean doing it wrong?)**

kMeans is better than kNN 
