#Cross-validation
#For leave-one-out crossvalidation, put crossval.n='LOOCV'

crossval_m = 5
#crossval_n='LOOCV'
crossval_n = 5

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
base_dir = '.'
datasets= ["/data/albrecht.arff", "/data/cosmic.arff", \
			"/data/isbsg10.arff", "/data/kitchenham.arff", \
            "/data/miyazaki94.arff", "/data/coc81.arff", \
            "/data/china.arff", "/data/cocomo-sdr.arff", \
            "/data/desharnais.arff", "/data/kemerer.arff", \
            "/data/maxwell.arff", "/data/nasa93.arff"]

#Output files
error_metrics = "/output/errors"
skott_knott = "/output/sk"

display_output = False
