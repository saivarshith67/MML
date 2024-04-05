import regression as rg

if __name__ == '__main__':
    x = rg.Regression()
    data_x = [1, 3, 4, 6, 8, 9, 11, 14]
    data_y = [1, 2, 4, 4, 5, 7, 8, 9]
    x.linear_regression_line(data_x, data_y)