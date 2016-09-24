#Read 4
##i. Reference:
A. Porter, C. Yilmaz, A. M. Memon, A. S. Krishna, D. C. Schmidt, and A. Gokhale, “Techniques and processes for improving the quality and performance of open-source software,” Software Process: Improvement and Practice, 2006.

##ii. Keywords:
ii1 DRE - Real Time Embedded Systems that are implemented using distributed heterogeneous architectures. These systems are generally distributed not just in terms of hardware and software, but also in terms of communication protocols. 
ii2 System Configuration Constraint -The constraints caused by the flexibility of an open source system(running on any platform). This flexibility creates a large number of potential platform configurations
ii3 Smoke testing - The process of selecting an running a subset of functional tests that ascertain the functionality of the system. Its purpose is to reveal simple failures in the software that can lead to the halt of a software release. 
ii4 DCQA - Distributed Continuous Quality Assurance is the process of performing quality assurance tasks such testing, profiling and performance evaluation in a distributed setting with multiple users participating in the QA process from different locations.


##iii Notes:
iii1 Motivational Statements: Open-source development processes are an effective approach to reduce cycle-time and decrease costs for software. This paper presents 2 different study of OSS related to quality assurance.
iii2 Hypothesis: The paper hypothesis that creating models and setting up DCQA improves the understanding of the open-source software, more defects can be found by increasing the diversity of platform configurations and centralising QA activities eliminates redundant work.
iii3 Related work: There are many online crash reporting systems which collect the system state at a central location whenever there is a crash. But these systems do not predict any errors/crash before the occur. Auto-build scoreboards are used by Mozilla which test the software across many configurations. Bugzilla is used to monitor and track all the bugs easing the process. 
iii4 Informative visualization: Table 1 shows how the model is created for the system and how the configuration constraints are provided to the system.

##iv Improvements:
iv1 The authors do not provide sufficient data about the results. 
iv2 The authors do not provide any comparison metrics to compare the results obtained using the model and without the model.

##Connection to 2012 paper:

Title - Do faster releases improve software quality? An empirical case study of Mozilla Firefox

The section of the this paper that the authors of the 2012 paper might have been interested in is the section that discusses problems in open source software systems. Specifically, the authors discuss the problem of  how shorter development cycles of open source projects affect the quality of software and end-user satisfaction. They also discuss the problem of unsystematic QA processes followed in open source projects and how it affects the software quality. 
