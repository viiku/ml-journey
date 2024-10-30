### Fitting

### Generalization in Machine Learning
Generalization refers to how well the concepts learned by a machine learning model apply to specific examples not seen by the model when it was learning. The goal of a good machine learning model is to generalize well from the training data to any data from the problem domain. This allows us to make predictions in the future on data the model has never seen.

***There is a terminology used in machine learning when we talk about how well a machine learning model learns and generalizes to new data, namely overfitting and underfitting.***

### Statistical Fit
In statistics a fit refers to how well you approximate a target function. This is good terminology to use in machine learning, because supervised machine learning algorithms seek to approximate the unknown underlying mapping function for the output variables given the input variables.

## Overfitting and Underfitting
**The cause of poor performance in machine learning is either overfitting or underfitting the data.**

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

**Combating overfitting**
1. Use more training data. The more you have, the harder it is to overfit the data by learning too much from any single training example.

2. Use regularization. Add in a penalty in the loss function for building a model that assigns too much explanatory power to any one feature or allows too many features to be taken into account.


![alt text](../assets/image-2.png)

The first piece of the sum above is our normal cost function.

The second piece is a regularization term that adds a penalty for large beta coefficients that give too much explanatory power to any specific feature.

The lambda coefficient of the regularization term in the cost function is a hyperparameter: a general setting of your model that can be increased or decreased (i.e. tuned) in order to improve performance. A higher lambda value will more harshly penalize large beta coefficients that could lead to potential overfitting. To decide the best value of lambda, you’d use a method called cross-validation which involves holding out a portion of the training data during training, and then seeing how well your model explains the held-out portion.