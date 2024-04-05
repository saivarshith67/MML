import numpy as np

class Regression:
    def __init__(self) -> None:
        pass
    
    def linear_regression_line(self, data_x : list, data_y : list) -> None:
        self.sum_of_prod = 0
        self.sum_x = 0
        self.sum_y = 0
        self.sum_of_squares = 0
        self.n = len(data_x)
        
        for i in range(self.n):
            self.sum_of_prod += (data_x[i] * data_y[i])
            self.sum_of_squares +=  ((data_x[i]) ** 2)
            self.sum_x += data_x[i]
            self.sum_y += data_y[i]
            
        """
        linear regression
        sum(y) = n*a + b*sum(x)
        sum(xy) = a*sum(x) + b*n*sum(x^2)
        
        now we will solve it using numpy.linalg.solve that we have to create a matrix  A and B where A is [[self.n, self.sum_x],[self.sum_x, self.sum_of_squares]] and B is [[self.sum_y],[self.sum_of_prod]]
        """
        
        self.A = np.array([[self.n, self.sum_x], [self.sum_x, self.sum_of_squares]])
        self.B = np.array([[self.sum_y],[self.sum_of_prod]])
        self.X = np.linalg.solve(self.A, self.B)
        self.constant_term = float(self.X[0]) #constant
        self.coefficient_of_x = float(self.X[1]) #coefficient of x
        
        print(f"Regression line: y = {self.constant_term} + {self.coefficient_of_x}*x")