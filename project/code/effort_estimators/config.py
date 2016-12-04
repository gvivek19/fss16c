#Cross-validation
#For leave-one-out crossvalidation, put crossval.n='LOOCV'

crossval_m = 5
#crossval_n='LOOCV'
crossval_n = 5

#Learners
teak = True
teak_k = 3
teak_gamma = [9, 4.5, 2.2]

teak0 = True
teak2 = True

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
efforts = "/output/efforts/efforts"
error_metrics = "/output/errors/errors"
skott_knott = "/output/sk/sk"

display_output = True
