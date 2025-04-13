# Resources
## Python
- [Session 1-4](https://g.co/kgs/qjVcg7e): Book (paid)
- [Session 1-4](https://automatetheboringstuff.com/): Book (free)
- [Session 05](https://realpython.com/read-write-files-python): Read/Write files
- [Session 06](https://realpython.com/working-with-files-in-python): Working with files
- [Session 07](https://realpython.com/python3-object-oriented-programming): Classes
- [Session 08](https://realpython.com/python3-object-oriented-programming): Inheritance
- [Session 09](https://realpython.com/python-modules-packages): Modules & Packages

## Libraries
- NumPy: [Tutorial](https://numpy.org/devdocs/user/quickstart.html), [Cheatsheet](https://images.datacamp.com/image/upload/v1676302459/Marketing/Blog/Numpy_Cheat_Sheet.pdf)
- Pandas: [Tutorial](https://pandas.pydata.org/docs/user_guide/10min.html#min), [Cheatsheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf), [Playlist](https://youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&si=aTa8e6_zZV_mB7kx)
- [Matplotlib](https://matplotlib.org/stable/users/explain/quick_start.html#quick-start)
- [Seaborn](https://seaborn.pydata.org/examples/index.html)

## Introduction to ML algorithms and their taxonomy
- `class_notes/ML01 Intro to ML.pdf`

## Linear Regression
- `class_notes/ML02 Linear Regression.pdf`
- `cs229-lecture_notes.pdf`: chapter 1
- Positive semi-definite matrices: `cs229-linear_algebra_review.pdf`: section 3.11
- Proving a matrix is positive semi-definite: [MIT-RES.18-009](https://youtu.be/ojUQk_GNQbQ)
- Gradients and Hessians: `cs229-linear_algebra_review.pdf`: sections 4.1, 4.2, 4.3
- Hessian: [Khan Academy](https://youtu.be/LbBcuZukCAw)

## Generalization
- `class_notes/ML03 Generalizing to unseen data.pdf`
- `cs229-lecture_notes.pdf`: section 8.1 (8.1.1 is optional)

## Regularization
- `class_notes/ML03 Generalizing to unseen data.pdf`
- ⁠`cs229-lecture_notes.pdf`: section 9.1
- [⁠Ridge and Lasso regression](https://www.ibm.com/topics/regularization)
- Optional readings:
    - [Ridge regression](https://www.ibm.com/topics/ridge-regression)
    - [Lasso regression](https://www.ibm.com/topics/lasso-regression)

## Cross-validation
- `class_notes/ML03 Generalizing to unseen data.pdf`
- `cs229-lecture_notes.pdf`: section 9.3

## Logistic Regression
- `class_notes/ML04 Logistic Regression.pdf`
- `cs229-lecture_notes.pdf`: chapter 2

## Gradient Discriminant Analysis
- `class_notes/ML05 Gradient Discriminant Analysis.pdf`
- `cs229-lecture_notes.pdf`: chapter 4.1
- [Machine Learning: What is Discriminant Analysis?](https://youtu.be/eBm8Uo9yhwI)
- [LDA and QDA decision boundaries](https://scikit-learn.org/1.5/_images/sphx_glr_plot_lda_qda_001.png)
- LDA vs QDA [Chapter 4, figures 4.5, 4.6 “The Elements of Statistical Learning”](https://www.sas.upenn.edu/~fdiebold/NoHesitations/BookAdvanced.pdf)

## Naive Bayes
- `class_notes/ML06 Naive Bayes.pdf`
- `cs229-lecture_notes.pdf`: chapter 4.2
- [Bernoulli NB pseudocode](https://nlp.stanford.edu/IR-book/html/htmledition/the-bernoulli-model-1.html)
- [Multinomial NB pseudocode](https://nlp.stanford.edu/IR-book/html/htmledition/naive-bayes-text-classification-1.html)
- [Library](https://scikit-learn.org/stable/api/sklearn.naive_bayes.html)

## Support Vector Machines
- `class_notes/ML07 SVM.pdf`
- Pre Lagrangian
    - Watch up to 7:24 - [Support Vector Machines: All you need to know!](https://youtu.be/ny1iZ5A8ilA?si=Ojn3UTEmc-Jqdv2F)
    - Watch up to 23:47 - [16. Learning: Support Vector Machines | MITOpenCourseWare](https://youtu.be/_PwhiWxHK8o?si=y4iZ77vXcarF1Zmf)
- Lagrangian
    - [Lecture recording](https://csciitd-my.sharepoint.com/:v:/g/personal/csz228001_iitd_ac_in/Eb9fqyoLMb1Pq6CDjoGnSBcBgLNyQE6fsTWu13JABy_eKg?e=ORDc56&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D)
    - `cs229-lecture_notes.pdf`: Sections 6.5 and 6.6
- Soft SVM, Kernel trick
    - [Lecture recording](https://csciitd-my.sharepoint.com/:v:/g/personal/csz228001_iitd_ac_in/EZem5sOqvodPvNH1vhmGiYkBmdTdgWGC461KA1VAaN_FWQ?e=2X9jMw&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D)

## Decision Trees
- `class_notes/ML08 Decision trees.pdf`
- `cs229-decision_trees.pdf`: Section 1
- [Decision and Classification Trees, Clearly Explained!!!](https://youtu.be/_L39rN6gz7Y?si=Oeo24OmwF94FRuyd)
- [Cost complexity pruning](https://scikit-learn.org/stable/modules/tree.html#minimal-cost-complexity-pruning)
- [AdaBoost](https://youtu.be/LsK-xG1cLYA?si=W-nMTowEW98MKgBK)

## Clustering
- `class_notes/ML09 Clustering.pdf`
- K-Means
    - [Video: StatQuest](https://youtu.be/4b5d3muPQmA?si=WXFd4uizWMj2ifv4)
    - [Video: Serrano.Academy](https://youtu.be/QXOkPvFM6NU?t=163)
- Heirarchical Agglomerative Clustering
    - [Video: DataLab](https://youtu.be/8QCBl-xdeZI?si=L7vu6tC7oD0XUQ9i)
    - [Video: Stanford](https://youtu.be/yktzn-Mr2Nw?si=gzCnl5UBNg5Ar0Ca)
    - Choosing the right distance metric
        - [Stack Exchange](https://stats.stackexchange.com/questions/195446/choosing-the-right-linkage-method-for-hierarchical-clustering)
        - [Stanford](https://nlp.stanford.edu/IR-book/html/htmledition/single-link-and-complete-link-clustering-1.html#fig:rprojectcomplete)
- DBSCAN
    - [Research paper](https://www.dbs.ifi.lmu.de/Publikationen/Papers/KDD-96.final.frame.pdf)
    - [Video: StatQuest](https://youtu.be/RDZUdRSDOok?si=V8S6j8XzPYcvQkaG)
- [Comparing clustering techniques](https://scikit-learn.org/stable/_images/sphx_glr_plot_cluster_comparison_001.png)
