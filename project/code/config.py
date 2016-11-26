#Cross-validation
#For leave-one-out crossvalidation, put crossval.n=LOOCV

crossval_m=5
crossval_n=5

#Learners
teak = True
abe = True
abe_k = [1,2,4,8,16]
neuralnet = True
lregression = True

#Error mesaures
ar = True
mr = True
pred = True

#Datasets. Give a comma-separated paths to the datasets for which the learners are to be run
datasets= ["./data/desharnais.arff"]

#Output files
effort_values = "./output/efforts"
error_metrics = "./output/errors"
skott_knott = "./output/sk"
