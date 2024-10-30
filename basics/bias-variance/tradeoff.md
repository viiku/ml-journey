### The Bias-Variance Trade-Off
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
