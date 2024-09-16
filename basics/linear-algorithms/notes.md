## Gradient Descent For Machine Learning
**Optimization is a big part of machine learning. Almost every machine learning algorithm has an optimization algorithm at it’s core.**

### Gradient Descent
Gradient descent is an optimization algorithm used to find the values of parameters (coefficients) of a function (f ) that minimizes a cost function (cost). Gradient descent is best used when the parameters cannot be calculated analytically (e.g. using linear algebra) and must be searched for by an optimization algorithm.

#### Intuition for Gradient Descent
The goal is to continue to try different values for the coefficients, evaluate their cost and select new coefficients that have a slightly better (lower) cost. We can think of such coefficient where cost can be minimized.

#### Gradient Descent Procedure
The procedure starts off with initial values for the coefficient or coefficients for the function. These could be 0.0 or a small random value.
    
    coefficient = 0.0

The cost of the coefficients is evaluated by plugging them into the function and calculating the cost.
    
    cost = f (coefficient)
    cost = evaluate(f (coefficient))

The derivative of the cost is calculated. The derivative refers to the slope of the function at a given point. We need to know the slope so that we know the direction (sign) to move the coefficient values in order to get a lower cost on the next iteration.
    
    delta = derivative(cost)

Now that we know from the derivative which direction is downhill, we can now update the coefficient values. A learning rate parameter (alpha) must be specified that controls how much the coefficients can change on each update.
    
    coefficient = coefficient − (alpha × delta)

This process is repeated until the cost of the coefficients (cost) is 0.0 or no further improvements in cost can be achieved. You can see how simple gradient descent is. It does require you to know the gradient of your cost function or the function you are optimizing, but besides that, it’s very straightforward.

### Batch Gradient Descent
The goal of all supervised machine learning algorithms is to best estimate a target function (f ) that maps input data (X) onto output variables (Y ).

The cost is calculated for a machine learning algorithm over the entire training dataset for each iteration of the gradient
descent algorithm. One iteration of the algorithm is called one batch and this form of gradient descent is referred to as batch gradient descent.

### Stochastic Gradient Descent
Gradient descent can be slow to run on very large datasets. Because one iteration of the gradient descent algorithm requires a prediction for each instance in the training dataset, it can take a long time when you have many millions of instances. In situations when you have large amounts of data, you can use a variation of gradient descent called stochastic gradient descent.

In this variation, the gradient descent procedure described above is run but the update to the coefficients is performed for each training instance, rather than at the end of the batch of instances.


### Tips for Gradient Descent
Plot Cost versus Time: Collect and plot the cost values calculated by the algorithm each iteration. The expectation for a well performing gradient descent run is a decrease in cost each iteration. If it does not decrease, try reducing your learning rate.

Learning Rate: The learning rate value is a small real value such as 0.1, 0.001 or 0.0001. Try different values for your problem and see which works best.

Rescale Inputs: The algorithm will reach the minimum cost faster if the shape of the cost function is not skewed and distorted. You can achieve this by rescaling all of the input variables (X) to the same range, such as between 0 and 1.

Few Passes: Stochastic gradient descent often does not need more than 1-to-10 passes through the training dataset to converge on good or good enough coefficients.

Plot Mean Cost: The updates for each training dataset instance can result in a noisy plot of cost over time when using stochastic gradient descent. Taking the average over 10, 100, or 1000 updates can give you a better idea of the learning trend for the algorithm.