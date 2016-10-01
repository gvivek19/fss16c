##i Reference
	
On Rapid Releases and Software Testing

##ii Keywords

ii1 Wilcoxon rank-sum test - The Wilcocon signed-rank test is a non-parametric test used to determine whether there is any difference in the population mean of two related samples or samples that are repeatedly measured. 

Ii2 Shapiro-Wilk test -  It determines whether the data follows normal distribution. If the p-value is less than the chosen alpha value then the null hypothesis that the data is normally distributed is rejected.

ii3 Cliff’s Delta - Cliff’s Delta is a measure of how often the values in one distribution are larger than the values in the second distribution. 

ii4 Software Testing - It is the process of investigating a product or a service in order to determine its quality and adherence to functional requirements. 

##iii Notes

iii1 Motivational statements: A lot of software companies have started releasing a new version of the product every 6 weeks or even lesser compared to the old 12 or 18-month release cycle. This paper performs an empirical study on the effect of a rapid release model on the QA process at Mozilla. 

iii2 Hypothesis: The paper seeks to answer a few questions by assuming the following hypothesis
 - Rapid Release(RR) cycles affect the amount of testing performed.
 - RR affects the number of testers working on a project
 - RR affects the frequency of testing activity
 - RR affects the number of configurations being tested.

iii3 Data: Data was obtained by mining the test execution data stored in Firefox’ Litmus repository. Web crawling was performed on the Litmus system to get test cases and their execution data for Firefox versions 2.0 to 13.0. 

iii4 Informative visualizations:Figure 1 explains the rapid release procedure followed in Mozilla. Figures 2 and 3 compare the distribution of release cycles and number of test executions per day for traditional release model and Rapid Release model. Figures 4 and 5 compare the cummulative number of test executions over time for both traditional and rapid release model.

##iv Improvements

iv1 An ideal metric for software quality testing is code coverage and this paper, like the 2012 paper, does not talk about how shorter release cycles affect the code coverage numbers. Comparing code coverage for rapid releases can help observe the quality of unit tests.

iv2 Having access to a QA engineer, the authors could have researched more how shorter release cycles affect developer productivity.

iv3 The authors could have talked more about the limitations of their study

##Connection to 2012 paper:

Title - Do faster releases improve software quality? An empirical case study of Mozilla Firefox

A major portion of the research done by the authors both of the papers is similar. While the authors of the 2012 paper explored the effect of shorter release cycles on software quality in general (as a measure of number of crashes) with the help of data alone, the authors of the 2013 paper got first hand feeback from a mozilla QA Engineer. Their main focus was on testing aspects in shorter release cycles 
