import regression as rg
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    data_x = []
    data_y = []
    size = int(input("Enter the number of data points: "))

    print("Enter data for x")
    for i in range(size):
        data = float(input("Enter the data: "))
        data_x.append(data)
    
    for i in range(size):
        data = float(input("Enter the data: "))
        data_y.append(data)
        
    constant, coeff = rg.linear_regression_line(data_x, data_y)
    
    rg.plot_regression_line(data_x, data_y)
