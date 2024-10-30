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

1.  Logistic Regression
2.  Linear Discriminant Analysis
3.  Perceptron

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

1. Decision Trees like CART and C4.5
2. Naive Bayes
3. Support Vector Machines
4. Neural Networks

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
