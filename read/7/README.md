##i Reference
Souza, Rodrigo, Christina Chavez, and Roberto A. Bittencourt. "Rapid releases and patch backouts: A software analytics approach." IEEE Software, 2015


##ii Keywords
ii1 Release engineering: Release engineering is a sub-discipline in software engineering concerned with the compilation, assembly, and delivery of source code into finished products or other software components. (Source: Wikipedia)

ii2 Software Analytics: The exploration of software engineering data to obtain insightful information.

ii3 Backout: Backout is reverting a patch because it broke the build.

ii4 Early backout and late backout: If the backout occurs before changing the status of bug report, it is early backout. Otherwise, it is a late backout.

##iii Notes
iii1 Motivational statements: Mozilla has adopted the rapid release cycle. The authors analysed the reports and spoke to the developers to study the reasons behind the conclusions obtained.

iii2 Hypothesis: The authors hypothesized that developers are backing out the broken patches earlier making the release process more stable. 

iii3 Data: The 2 primary information sources are commit logs and bug reports. Bug reports were available as an SQL database dump. Release dates were obtained from Mozilla wiki. 3 periods of releases- traditional, transitional rapid and rapid releases were studied.

iii4 Informative visualizations: Table 1 shows all the metrics for the 3 periods which shows the developer workload didn’t change much, early backouts increased while late backouts decreased. This is explained by the graph in figure 3.

##iv Improvements
iv1 The paper does not prove the effect of code size changes using any data.

iv2 The paper does not take the bug priority into account for any of the studies.

iv3 The author could have talked more about the limitations of their study.

##Connection to 2012 paper:

Title - Do faster releases improve software quality? An empirical case study of Mozilla Firefox

This paper is quite similar to the 2012 paper. The main difference is that while the 2012 paper addresses the effect Rapid Release cycles have on software quality in terms of number of bugs reported and mean up-time, this paper observes the backout rates and the productivity of the developers and how it has changed due to the shift in the release cycle.
