#Summary of the paper
Paper link : http://menzies.us/pdf/11teak.pdf

Only a few sections of the paper has been summarized here.

##ABE0:
* Analogy Based Effort Estimator
* K = 3 Nearest Neighbor
* Similarity metric usually used is Euclidean distance.
* Other variants include:
  * Feature subset selection
  * Different similarity metric
  * Weighted simiarity functions
  * value of K
  * solution function/adaption strategy

##TEAK
Teak is ABE0 with the following variations:
1. Select prediction system:
* Limit design options to those that directly address the essential assumption of prediction. 
  * Case subset selection
  * no of analogies used for estimation

2. Identify essential assumptions:
* Projects that are similar with respect to project and product features have similar effort
* Projects from high variance region have very different project effort values. 
  * Leads to decrease in accuracy estimation.

3. Identify assumption violation:
* Compare the variance of large and small k values
* Use GAC (Greedy Agglomerative clustering) - bottom up approach
* Other options include recursive k-means, MESO
* Find nearest neighbour using GAC.

4. Remove violations:
* Remove situations which violate the essential assumption.
  * Violation of Essential Assumption is "Recursing into subtrees with higher variance than parent".
  * This occurs if there are outliers.
* Done using a randomized method:
  * R ^ \gamma * max\( \sigma ^ 2 \)  where 0 <= R <= 1 and \gamma = 9 are recommended.

5. Execute modified values:
* Use GAC on training set and create GAC1
* Prune GAC1 using the above metric
* Applu GAC to the leaves of pruned GAC1 to form GAC2
Use GAC2 to predict the effort


Use Skott-Knott analysis to rank the algorithms
