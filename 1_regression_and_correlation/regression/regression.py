import numpy as np
import matplotlib.pyplot as plt

def linear_regression_line(independ_var_data: list, dep_var_data: list) -> tuple:
    """
    This function calculates the coefficients of the linear regression line for the given independent and dependent variable data.

    :param independ_var_data: List of independent variable data
    :param dep_var_data: List of dependent variable data
    :return: Tuple of constant term and coefficient of independent variable
    """

    sum_of_prod = 0
    sum_x = 0
    sum_y = 0
    sum_of_squares = 0
    n = len(independ_var_data)

    for i in range(n):
        sum_of_prod += (independ_var_data[i] * dep_var_data[i])
        sum_of_squares += ((independ_var_data[i]) ** 2)
        sum_x += independ_var_data[i]
        sum_y += dep_var_data[i]

    """
    Linear regression formula:
    sum(y) = n*a + b*sum(x)
    sum(xy) = a*sum(x) + b*n*sum(x^2)

    Now we will solve it using numpy.linalg.solve that we have to create a matrix A and B where A is [[n, sum_x],[sum_x, sum_of_squares]] and B is [[sum_y],[sum_of_prod]]
    """
    A = np.array([[n, sum_x], [sum_x, sum_of_squares]])
    B = np.array([[sum_y], [sum_of_prod]])
    X = np.linalg.solve(A, B)
    constant_term = float(X[0])  # Constant term
    coeff_of_indep_var = float(X[1])  # Coefficient of independent variable

    return (constant_term, coeff_of_indep_var)

def predict(constant_term: float, coeff_of_indep_var: float, val_of_indep_var) -> float:
    """
    This function predicts the dependent variable value for the given independent variable value using the linear regression coefficients.

    :param constant_term: Constant term of the linear regression line
    :param coeff_of_indep_var: Coefficient of independent variable of the linear regression line
    :param val_of_indep_var: Value of independent variable
    :return: Predicted value of dependent variable
    """
    return constant_term + coeff_of_indep_var * val_of_indep_var



def plot_regression_line(independ_var_data: list, dep_var_data: list) -> None:
    """
    This function plots the scatter diagram of the given independent and dependent variable data along with the regression line.

    :param independ_var_data: List of independent variable data
    :param dep_var_data: List of dependent variable data
    """

    constant_term, coeff_of_indep_var = linear_regression_line(independ_var_data, dep_var_data)

    x = np.array(independ_var_data)
    y = np.array(dep_var_data)

    # Scatter plot of the data
    plt.scatter(x, y, color='b', label='Data')

    # Line of best fit
    min_x = min(x)
    max_x = max(x)
    y_pred = predict(constant_term, coeff_of_indep_var, np.array(range(min_x, max_x+1)))
    plt.plot(range(min_x, max_x+1), y_pred, color='r', label='Regression Line')

    plt.xlabel('Independent Variable')
    plt.ylabel('Dependent Variable')
    plt.title('Scatter Diagram of Data and Regression Line')
    plt.legend()
    plt.show()

