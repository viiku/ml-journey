## supervised learning

In supervised learning, the machine attempts to learn the relationship between data from scratch, by running labeled training data through a learning algorithm.

The two tasks of supervised learning: 
1. Regression
    Predict a continuous numerical value (Y)

    Y = f(X) + ε, where X = (x1, x2…xn)
    Training: machine learns f from labeled training data
    Test: machine predicts Y from unlabeled testing data

### Linear Regression (ordinary least squares)
Linear regression is a parametric method, which means it makes an assumption about the form of the function relating X and Y

    Y = B0 + B1 x X + e 

    B0 = Y-intercept or variance
    B1 = Slope or Coefficient

***Goal here is to learn the model parameters (in this case, β0 and β1) that minimize error in the model’s predictions.***

To find the best parameters:
1. Define a cost function, or loss function, that measures how inaccurate our model’s predictions are.
2. Find the parameters that minimize loss, i.e. make our model as accurate as possible.

![alt text](./images/image.png)

Where n stands for number of observations.

### Gradient Descent

**As a cost function grows in complexity, finding a closed form solution with calculus is no longer feasible then an iterative approach called gradient descent, which allows us to minimize a complex loss function**

***The goal of gradient descent is to find the minimum of our model’s loss function by iteratively getting a better and better approximation of it.***

    f(β0,β1)=z

To begin gradient descent, we make some guess of the parameters β0 and β1 that minimize the function. Next, we find the partial derivatives of the loss function with respect to each beta parameter: [dz/dβ0, dz/dβ1]. A partial derivative indicates how much total loss is increased or decreased if you increase β0 or β1 by a very small amount.

    if dz/dβ1 < 0 then increasing β1 is good, because it would reduce total cost
    If dz/dβ1 > 0, we will decrease β1. 
    If dz/dβ1 = 0 it’s zero, don’t change β1 because it means we've reached an optimum.

### Overfitting
**Learning a function that perfectly explains the training data that the model learned from, but doesn’t generalize well to unseen test data.**

***Overfitting happens when a model overlearns from the training data to the point that it starts picking up idiosyncrasies that aren’t representative of patterns in the real world. This becomes especially problematic as you make your model increasingly complex.***

### Underfitting
**Underfitting is a related issue where model is not complex enough to capture the underlying trend in the data.**

### Bias-Variance Tradeoff
Bias is the amount of error introduced by approximating real-world phenomena with a simplified model.

Variance is how much your model's test error changes based on variation in the training data. It reflects the model's sensitivity to the idiosyncrasies of the data set it was trained on.

As a model increases in complexity and it becomes more wiggly (flexible), its bias decreases (it does a good job of explaining the training data), but variance increases (it doesn't generalize as well). Ultimately, in order to have a good model, you need one with low bias and low variance.

![alt text](./images/image-1.png)

**Combating overfitting**
1. Use more training data. The more you have, the harder it is to overfit the data by learning too much from any single training example.

2. Use regularization. Add in a penalty in the loss function for building a model that assigns too much explanatory power to any one feature or allows too many features to be taken into account.


![alt text](./images/image-2.png)

The first piece of the sum above is our normal cost function.

The second piece is a regularization term that adds a penalty for large beta coefficients that give too much explanatory power to any specific feature.

The lambda coefficient of the regularization term in the cost function is a hyperparameter: a general setting of your model that can be increased or decreased (i.e. tuned) in order to improve performance. A higher lambda value will more harshly penalize large beta coefficients that could lead to potential overfitting. To decide the best value of lambda, you’d use a method called cross-validation which involves holding out a portion of the training data during training, and then seeing how well your model explains the held-out portion.



2. Classification. 
    Assign a label. Is this a picture of a cat or a dog?

Linear regression, loss functions, and gradient descent.