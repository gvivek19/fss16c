##i Reference

Sandy Clark, Micheal Collis, Matt Blaze and Jonathan M. Smith, "Security and Rapid-Release in Firefox", Proceedings of the 2014 ACM SIGSAC Conference on Computer and Communications Security



##ii Keywords
ii1 Software Security - It could be defined as an idea implemented during the design phase  to protect the software against external vulnerabilities.

ii2 Baseline Vulnerabilities - The vulnerabilites that affect the original codebase before the switch to Rapid Release Cycles.

ii3 Regressive Vulnerabilities - The vunerabilites discovered in code after the version in which it was introduced has been obseleted by a more recent version

ii4 Agile Programming - It describes a set of principles for software development under which requirements and solutions evolve through the collaborative effort of self-organizing cross-functional teams. (source - wikipedia)

##iii Notes

iii1 Motivational statements: Many famous consumer facing applications today follow the Rapid Release Model in which a new version is released every few weeks. The paper aims to find the correlation between rapid releases and security. Specifically, the authors use the firefox dataset to check if the number of vulnerabilities as increased after the Mozilla switched to rapid release model.

iii2 Hypothesis: The paper seeks to answer a few questions by assuming the following hypothesis
- The addition of 250000 lines of code over 42 days increases the number of vulnerabilities discovered and disclosed.
- The scope of disclosed vulnerabilities is confined to Rapid Release Cycles(RRC).
- RRC vulnerabilities are easier to find

iii3 Data: From the inception of Rapid release cycles upto the time of writing the paper it was found that 617 new bug ids were issued corresponding to new vulnerabilities. Lines of code and file counts were derived from mercurial repositories hosted by Mozilla.  

iii4 Informative visualizations: Table 1 explains the changes between different RRC versions in terms of number of lines of code. Figure 1 shows the cummalitive total vulnerabilities affecting RRC and corresponding ESR versions during the same 6-week period. Figure 2 shows the ratio of vulnerabilties from version to version.

##iv Improvements

iv1 The authors could have given more information on the limitations of their study.

iv2 The authors could have checked whether the results they got matched with the findings in  other products ( by running their test on other publicly available datasets)

iv3 The authors could have checked the correlation between the number of vulnerabilities and the number of crash reports for each version of firefox since the inception of RRC.

##Connection to 2012 paper:

Title - Do faster releases improve software quality? An empirical case study of Mozilla Firefox

This paper is quite similar to the 2012 paper. The main difference is that while the 2012 paper addresses the effect Rapid Release cycles have on software quality in terms of number of bugs reported and mean up-time, this paper observes the affect RRC has on software quality in numbers of security and number of vulnerabilities. Both the papers conclude that RRC has no or minimal effect on software quality. 
