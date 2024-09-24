## Classification of Machine learning Algorithms based on parameters

### Parametric Machine Learning Algorithms
**Algorithms that simplify the function to a known form are called parametric machine learning algorithms.**

***A learning model that summarizes data with a set of parameters of fixed size (independent of the number of training examples) is called a parametric model. No matter how much data you throw at a parametric model, it won’t change its mind about how many parameters it needs.***

The algorithms involve two steps:
1. Select a form for the function.
2. Learn the coefficients for the function from the training data.

An easy to understand functional form for the mapping function is a line, as is used in linear regression:
    
    B0 + B1 × X1 + B2 × X2 = 0

Where B0, B1 and B2 are the coefficients of the line that control the intercept and slope, and X1 and X2 are two input variables. Assuming the functional form of a line greatly simplifies the learning process. Now, all we need to do is estimate the coefficients of the line equation and we have a predictive model for the problem.

**linear machine learning algorithms**
If the assumed functional form is a linear combination of the input variables then parametric machine learning algorithms are often also called linear machine learning algorithms. (above example)

Examples: - Logistic Regression, Linear Discriminant Analysis, Perceptron

Benefits of Parametric Machine Learning Algorithms:

Simpler: These methods are easier to understand and interpret results.
Speed: Parametric models are very fast to learn from data.
Less Data: They do not require as much training data and can work well even if the fit to the data is not perfect.

Limitations of Parametric Machine Learning Algorithms:

Constrained: By choosing a functional form these methods are highly constrained to the specified form.
Limited Complexity: The methods are more suited to simpler problems.
Poor Fit: In practice the methods are unlikely to match the underlying mapping function.

### Nonparametric Machine Learning Algorithms
**Algorithms that do not make strong assumptions about the form of the mapping function are called nonparametric machine learning algorithms. By not making assumptions, they are free to learn any functional form from the training data.**

***Nonparametric methods are good when you have a lot of data and no prior knowledge, and when you don’t want to worry too much about choosing just the right features.***

Some more examples of popular nonparametric machine learning algorithms are:
. Decision Trees like CART and C4.5
. Naive Bayes
. Support Vector Machines
. Neural Networks

Benefits of Nonparametric Machine Learning Algorithms:

Flexibility: Capable of fitting a large number of functional forms.
Power: No assumptions (or weak assumptions) about the underlying function.
Performance: Can result in higher performance models for prediction.

Limitations of Nonparametric Machine Learning Algorithms:

More data: Require a lot more training data to estimate the mapping function.
Slower: A lot slower to train as they often have far more parameters to train.
Overfitting: More of a risk to overfit the training data and it is harder to explain why specific predictions are made.


## Contrast between supervised, unsupervised and semi-supervised machine learning problems.

### Supervised Machine Learning
***Supervised learning is where you have input variables (X) and an output variable (Y ) and you use an algorithm to learn the mapping function from the input to the output.***
    
    Y = f (X)

The goal is to approximate the mapping function so well that when you have new input data (X) that you can predict the output variables (Y ) for that data. It is called supervised learning because the process of an algorithm learning from the training dataset can be thought of as a teacher supervising the learning process. We know the correct answers, the algorithm iteratively makes predictions on the training data and is corrected by the teacher. Learning stops when the algorithm achieves an acceptable level of performance.

Supervised learning problems can be further grouped into regression and classification problems.

Classification: A classification problem is when the output variable is a category, such as red or blue or disease and no disease.
Regression: A regression problem is when the output variable is a real value, such as dollars or weight.

Some common types of problems built on top of classification and regression include recommendation and time series prediction respectively.

Some popular examples of supervised machine learning algorithms are:

Linear regression for regression problems.
Random forest for classification and regression problems.
Support vector machines for classification problems.

### Unsupervised Machine Learning
***Unsupervised learning is where you you only have input data (X) and no corresponding output variables. The goal for unsupervised learning is to model the underlying structure or distribution in the data in order to learn more about the data.***
***These are called unsupervised learning because unlike supervised learning above there is no correct answers and there is no teacher. Algorithms are left to their own devises to discover and present the interesting structure in the data.***

**Unsupervised learning problems can be further grouped into clustering and association problems.**
Clustering: A clustering problem is where you want to discover the inherent groupings in the data, such as grouping customers by purchasing behavior.
Association: An association rule learning problem is where you want to discover rules that describe large portions of your data, such as people that buy A also tend to buy B.

Some popular examples of unsupervised learning algorithms are:
k-means for clustering problems.
Apriori algorithm for association rule learning problems.

### Semi-Supervised Machine Learning
***Problems where you have a large amount of input data (X) and only some of the data is labeled (Y ) are called semi-supervised learning problems. These problems sit in between both supervised and unsupervised learning.***

A good example is a photo archive where only some of the images are labeled, (e.g. dog, cat, person) and the majority are unlabeled. 
Many real world machine learning problems fall into this area. This is because it can be expensive or time consuming to
label data as it may require access to domain experts. Whereas unlabeled data is cheap and easy to collect and store.


## The Bias-Variance Trade-Off
The two biggest sources of error when learning from data, namely bias and variance and the tension between these two concerns.

### Overview
***In supervised machine learning an algorithm learns a model from training data. The goal of any supervised machine learning algorithm is to best estimate the mapping function (f ) for the output variable (Y ) given the input data (X). The mapping function is often called the target function because it is the function that a given supervised machine learning algorithm aims to approximate. ***

The prediction error for any machine learning algorithm can be broken down into three parts:
Bias Error
Variance Error
Irreducible Error (Not reducible regardless of any algorithm used)

### Bias Error
***Bias are the simplifying assumptions made by a model to make the target function easier to learn.*** 

Generally parametric algorithms have a high bias making them fast to learn and easier to understand but generally less flexible. In turn they are have lower predictive performance on complex problems that fail to meet the simplifying assumptions of the algorithms bias.

Low Bias: Suggests more assumptions about the form of the target function. ex. Decision Trees, k-Nearest Neigh-
bors and Support Vector Machines

High-Bias: Suggests less assumptions about the form of the target function. ex. Linear Regression, Linear Discriminant Analysis and Logistic Regression

### Variance Error
***Variance is the amount that the estimate of the target function will change if different training data was used.*** 

The target function is estimated from the training data by a machine learning algorithm, so we should expect the algorithm to have some variance. Ideally, it should not change too much from one training dataset to the next, meaning that the algorithm is good at picking out the hidden underlying mapping between the inputs and the output variables. Machine learning algorithms that have a high variance are strongly influenced by the specifics of the training data. This means that the specifics of the training have influences the number and types of parameters used to characterize the mapping function.

Low Variance: Suggests small changes to the estimate of the target function with changes to the training dataset.

High Variance: Suggests large changes to the estimate of the target function with changes to the training dataset.

Generally nonparametric machine learning algorithms that have a lot of flexibility have a high bias. 
For example decision trees have a high bias, that is even higher if the trees are not pruned before use. 

Examples of low-variance machine learning algorithms include: Linear Regression, Linear Discriminant Analysis and Logistic Regression. 
Examples of high-variance machine learning algorithms include: Decision Trees, k-Nearest Neighbors and Support Vector
Machines.

### Bias-Variance Trade-Off
The goal of any supervised machine learning algorithm is to achieve low bias and low variance. In turn the algorithm should achieve good prediction performance.

Parametric or linear machine learning algorithms often have a high bias but a low variance.
Nonparametric or nonlinear machine learning algorithms often have a low bias but a high variance.

Examples of configuring the bias-variance trade-off for specific algorithms:

The k-nearest neighbors algorithm has low bias and high variance, but the trade-off can be changed by increasing the value of k which increases the number of neighbors that contribute to the prediction and in turn increases the bias of the model.

The support vector machine algorithm has low bias and high variance, but the trade-off can be changed by increasing the C parameter that influences the number of violations of the margin allowed in the training data which increases the bias but decreases the variance.


There is no escaping the relationship between bias and variance in machine learning.
 
Increasing the bias will decrease the variance.
Increasing the variance will decrease the bias.

***There is a trade-off at play between these two concerns and the algorithms you choose and the way you choose to configure them are finding different balances in this trade-off for your problem. In reality we cannot calculate the real bias and variance error terms because we do not know the actual underlying target function.***


## Overfitting and Underfitting
**The cause of poor performance in machine learning is either overfitting or underfitting the data.**

### Generalization in Machine Learning
Generalization refers to how well the concepts learned by a machine learning model apply to specific examples not seen by the model when it was learning. The goal of a good machine learning model is to generalize well from the training data to any data from the problem domain. This allows us to make predictions in the future on data the model has never seen.

***There is a terminology used in machine learning when we talk about how well a machine learning model learns and generalizes to new data, namely overfitting and underfitting.***

### Statistical Fit
In statistics a fit refers to how well you approximate a target function. This is good terminology to use in machine learning, because supervised machine learning algorithms seek to approximate the unknown underlying mapping function for the output variables given the input variables.

### Overfitting in Machine Learning
Overfitting happens when a model learns the detail and noise in the training data to the extent that it negatively impacts
the performance on the model on new data. This means that the noise or random fluctuations in the training data is picked up and learned as concepts by the model. The problem is that these concepts do not apply to new data and negatively impact the models ability to generalize though it can give good performance on trained data.

### Underfitting in Machine Learning
Underfitting refers to a model that can neither model the training data not generalize to new data. An underfit machine learning model is not a suitable model and will be obvious as it will have poor performance on the training data as well as on other data.

### A Good Fit in Machine Learning
The sweet spot is the point just before the error on the test dataset starts to increase where the model has good skill on both the training dataset and the unseen test dataset

### How To Limit Overfitting
There are two important techniques that you can use when evaluating machine learning algorithms to limit overfitting:
1. Use a resampling technique to estimate model accuracy.
2. Hold back a validation dataset.

The most popular resampling technique is k-fold cross validation. It allows you to train and test your model k-times on different subsets of training data and build up an estimate of the performance of a machine learning model on unseen data.

A validation dataset is simply a subset of your training data that you hold back from your machine learning algorithms until the very end of your project. After you have selected and tuned your machine learning algorithms on your training dataset you can evaluate the learned models on the validation dataset to get a final objective idea of how the models might perform on unseen data.