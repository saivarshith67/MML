import numpy as np


def linear_regression_line(data_x : list, data_y : list) -> None:
    sum_of_prod = 0
    sum_x = 0
    sum_y = 0
    sum_of_squares = 0
    n = len(data_x)
    
    for i in range(n):
        sum_of_prod += (data_x[i] * data_y[i])
        sum_of_squares +=  ((data_x[i]) ** 2)
        sum_x += data_x[i]
        sum_y += data_y[i]
        
    """
    linear regression
    sum(y) = n*a + b*sum(x)
    sum(xy) = a*sum(x) + b*n*sum(x^2)
    
    now we will solve it using numpy.linalg.solve that we have to create a matrix  A and B where A is [[n, sum_x],[sum_x, sum_of_squares]] and B is [[sum_y],[sum_of_prod]]
    """
    
    A = np.array([[n, sum_x], [sum_x, sum_of_squares]])
    B = np.array([[sum_y],[sum_of_prod]])
    X = np.linalg.solve(A, B)
    constant_term = float(X[0]) #constant
    coefficient_of_x = float(X[1]) #coefficient of x
    
    print(f"Regression line: y = {constant_term} + {coefficient_of_x}*x")