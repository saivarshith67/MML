import numpy as np


def linear_regression_line(independ_var_data : list, dep_var_data : list) -> None:
    sum_of_prod = 0
    sum_x = 0
    sum_y = 0
    sum_of_squares = 0
    n = len(independ_var_data)
    
    for i in range(n):
        sum_of_prod += (independ_var_data[i] * dep_var_data[i])
        sum_of_squares +=  ((independ_var_data[i]) ** 2)
        sum_x += independ_var_data[i]
        sum_y += dep_var_data[i]
        
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
    coeff_of_indep_var = float(X[1]) #coefficient of x
    
    # print(f"Regression line: y = {constant_term} + {coeff_of_indep_var}*x")
    return (constant_term, coeff_of_indep_var)

def predict(constant_term : float, coeff_of_indep_var : float, val_of_indep_var) -> float:
    return constant_term + coeff_of_indep_var * val_of_indep_var