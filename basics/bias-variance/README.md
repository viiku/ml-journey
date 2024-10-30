### Bias-Variance
The two biggest sources of error when learning from data, namely bias and variance and the tension between these two concerns.

### Overview
***In supervised machine learning an algorithm learns a model from training data. The goal of any supervised machine learning algorithm is to best estimate the mapping function (f) for the output variable (Y) given the input data (X). The mapping function is often called the target function because it is the function that a given supervised machine learning algorithm aims to approximate. ***

The prediction error for any machine learning algorithm can be broken down into three parts:
Bias Error
Variance Error
Irreducible Error (Not reducible regardless of any algorithm used)

### Bias Error
***Bias are the simplifying assumptions made by a model to make the target function easier to learn.*** 

Generally parametric algorithms have a high bias making them fast to learn and easier to understand but generally less flexible. In turn they are have lower predictive performance on complex problems that fail to meet the simplifying assumptions of the algorithms bias.

Low Bias: Suggests more assumptions about the form of the target function. ex. Decision Trees, k-Nearest Neighbors (K-NN) and Support Vector Machines (SVM)

High-Bias: Suggests less assumptions about the form of the target function. ex. Linear Regression, Linear Discriminant Analysis and Logistic Regression

### Variance Error
***Variance is the amount that the estimate of the target function will change if different training data was used.*** 

The target function is estimated from the training data by a machine learning algorithm, so we should expect the algorithm to have some variance. Ideally, it should not change too much from one training dataset to the next, meaning that the algorithm is good at picking out the hidden underlying mapping between the inputs and the output variables. Machine learning algorithms that have a high variance are strongly influenced by the specifics of the training data. This means that the specifics of the training have influences the number and types of parameters used to characterize the mapping function.

Low Variance: Suggests small changes to the estimate of the target function with changes to the training dataset.

High Variance: Suggests large changes to the estimate of the target function with changes to the training dataset.

Generally nonparametric machine learning algorithms that have a lot of flexibility have a high bias. 
For example decision trees have a high bias, that is even higher if the trees are not pruned before use. 

Examples of low-variance machine learning algorithms include: 
1. Linear Regression
2. Linear Discriminant Analysis 
3. Logistic Regression. 

Examples of high-variance machine learning algorithms include: 
1. Decision Trees
2. K-Nearest Neighbors
3. Support Vector Machines.