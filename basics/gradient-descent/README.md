
### Gradient Descent

**At a theoretical level, gradient descent is an algorithm that minimizes functions. Given a function defined by a set of parameters, gradient descent starts with an initial set of parameter values and iteratively moves toward a set of parameter values that minimize the function. This iterative minimization is achieved using calculus, taking steps in the negative direction of the function gradient.**

***The goal of gradient descent is to find the minimum of our model’s loss function by iteratively getting a better and better approximation of it.***

    f(β0,β1) = z

To begin gradient descent, we make some guess of the parameters β0 and β1 that minimize the function. Next, we find the partial derivatives of the loss function with respect to each beta parameter: [dz/dβ0, dz/dβ1]. A partial derivative indicates how much total loss is increased or decreased if you increase β0 or β1 by a very small amount.

    if dz/dβ1 < 0 then increasing β1 is good, because it would reduce total cost

    If dz/dβ1 > 0, we will decrease β1. 

    If dz/dβ1 = 0 it’s zero, don’t change β1 because it means we've reached an optimum.

Learn more about it here...

1. [Gradient-descent-linear-regression](https://spin.atomicobject.comgradient-descent-linear-regression/)

2. [Understanding-gradient-descent](https://eli.thegreenplace.net/2016/understanding-gradient-descent/)

#### Let's understand it using an example
Gradient descent is an optimization algorithm used to find the minimum of a function.
Let's use a simple quadratic function as our example:
    f(x) = x² + 2

Our goal is to find the minimum of this function using gradient descent.

let's walk through the gradient descent process:

1. Choose a starting point:
    Let's start at x = 4

2. Calculate the gradient (derivative) of the function:
    f'(x) = 2x

3. Choose a learning rate:
    Let's use a learning rate of 0.1

4. Update the x value using the gradient and learning rate:
    x_new = x_old - (learning rate * gradient)

5. Repeat steps 2-4 until convergence or a set number of iterations

#### Implecations of learning_rate
1. A larger learning rate can lead to faster convergence but might overshoot the minimum.
2. A smaller learning rate leads to slower but more stable convergence.
3. More iterations generally lead to a more accurate result, but there are diminishing returns after a certain point.
