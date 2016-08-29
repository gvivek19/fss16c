##i Reference
    
F. Khomh, T. Dhaliwal, Y. Zou and B. Adams. 2012.Do Faster Releases Improve Software Quality?: An Empirical Case Study of Mozilla Firefox.Proceedings of the 9th IEEE Working Conference on Mining Software Repositories. IEEE Press, 2012.

##ii Keywords
ii1 Post release bugs - These are bugs(malfunctioning features) that occur after the release of a version of software.

ii2 Release Cycle - The time between the release of one version of a software to the next.

ii3 Software Quality - The quality of a software is a measure of the degree to which a software conforms to its functional requirements and design.

ii4 P-value - A statistical metric used decide whether to reject a null hypothesis or not. It can also be defined as the probability of obtaining a result that is equal to or more extreme than what was actually observed.(Source: Wikipedia).

##iii Notes
iii1 Motivational statements: A lot of software companies have started releasing a new version of the product every 6 weeks or even lesser compared to the old 12 or 18-month release cycle. It is not clear whether the shift in this release cycle has any effect on the product quality. This paper is about an empirical study on the change in software quality with Mozilla Firefox as a case study.

iii2 Hypothesis: The paper hypothesizes that the shift from a longer traditional release cycle to a shorter rapid one has lead to a decrease in post-release bugs, faster resolution of bugs, detection of bugs faster and users switch to newer versions in case of rapid releases.

iii3 Data: The paper collected data of 25 alpha, 25 beta versions, 29 minor and 7 major versions. The release cycle and development time are obtained from the Mozilla Wiki. The Mozilla Source Code Repository is used to analyse the complexity using a tool - SourceMonitor. The Crash Repository (Socorro) is used to obtain the crash summaries and the Bug Repository (Bugzilla) is used to obtain details about each reported bug. All these are documented in figure 3 of the paper.

iii4 Informative visualizations: Figures 4 to 7 provide useful insight about the studies done in the paper. Each figure shows us how the hypothesis vary for the traditional release and the rapid release, giving us an empirical value whether the hypothesis can be rejected or not. Figure 4 shows that the number of post release bugs raised per day doesn’t change by a large value whereas figure 5 shows us that the user detects the bug earlier since firefox crashes more and hence the low uptime. Figures 6 and 7 show how the difference is when it comes to the bug fixes.

##iv Improvements
iv1 The effect that a shorter release cycle produces on developer productivity can be checked. Although the authors have mentioned that developers are less pressured to rush half-baked features into the software repository to meet the deadline, they could add a source to back this claim. Also, It has been observed that agile practices, which have shorter release cycles, are quite intense on developers.

iv2 A very important metric to track the quality of a software is code coverage. The authors could have efficiently observed the quality of unit tests written for both the models by comparing their code coverage numbers.

iv3 The authors can check for number of features released in traditional release model compared to multiple rapid releases for the same time period. They could then use this information observe the number of bugs with relation to the number of features released in both the models.
