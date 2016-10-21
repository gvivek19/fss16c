##i Reference
da Costa, Daniel Alencar, et al. "The impact of switching to a rapid release cycle on the integration delay of addressed issues: an empirical study of the mozilla firefox project." Proceedings of the 13th International Workshop on Mining Software Repositories. ACM, 2016.


##ii Keywords
ii1 Issue reports: It describes a new feature, enhancement or a bug. 

ii2 Issue Tracking System: It is used to manage issues as they transition from being understood to being addressed.

ii3 Mann-Whitney-Wilcoxon test: It is a non-parametric test of the null hypothesis that two distributions come from the same population.

ii4 Cliff’s delta: It is a non-parametric effect-size measure to verify how often values in one distribution are larger than the values in another distribution.

##iii Notes
iii1 Motivational statements: Rapid release cycle adopters claim that they deliver addressed issues quickly. This paper studies that and gives an empirical result.

iii2 Hypothesis: The paper hypothesizes that rapid release cycle delays the integration of addressed issues. Also, traditional releases prioritize the integration of backlog issues.

iii3 Data: The release information were obtained from release history wiki. Issues were linked to the release versions. 72114 issues were analysed (4673 traditional releases, 37440 rapid releases)

iii4 Informative visualizations: Figure 3 provides the data regarding the different times during the lifetime of an issue. Figure 4 shows the integration delay of addressed issues for minor/major releases. FIgure 7 shows the relationship between metrics and integration delay.

##iv Improvements
iv1 It does not take into consideration the backout rates and increase in time due to that.

iv2 The authors could have checked whether the results they got matched with the findings in other products ( by running their test on other publicly available datasets).

##Connection to 2012 paper:

Title - Do faster releases improve software quality? An empirical case study of Mozilla Firefox

This paper is quite similar to the 2012 paper. This uses the basic idea of the 2012 paper and further analyzes it to study the time taken for the issue patch to get integrated into the product for release.
