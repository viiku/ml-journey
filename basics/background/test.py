from numpy import *

#   Suppose we've a function called and has learning_rate of 0.1
#
#       y = mx + c
#       
#   Let's assume an cost function / MSE (Mean Squared Error)
#
#   MSE or Cost = (y_predict - y_actual)
#   
#   MSE or Cost = 1/n * ((mx+c) - y) ** 2
#
#   Calculate the gradients
#
#   dCost/dm = 2/n * ((mx+c) - y) * x
#
#   dCost/dc = 2/n * ((mx+c) -y)

def compute_gradient(starting_m, starting_c, learning_rate, total_points):
    n = total_points
    total_m_grad = 0
    total_c_grad = 0
    
    for i in range(total_points):
        total_m_grad += (1/n )* (mx + c - y)
        total_c_grad += (1/n) * (mx + c - y)
    
    # m = m - gr
    # return [m, c]
    
def run():
    total_points = 1000
    learning_rate = 0.1
    initial_m = 0
    initial_c = 0

    [grad_m, grad_c] = compute_gradient(initial_m, initial_c, learning_rate, total_points)
    
if __name__ == '__main__':
    run()