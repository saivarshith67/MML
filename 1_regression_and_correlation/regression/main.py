import regression as rg

if __name__ == '__main__':
    data_x = [1, 3, 4, 6, 8, 9, 11, 14]
    data_y = [1, 2, 4, 4, 5, 7, 8, 9]
    constant, coeff = rg.linear_regression_line(data_x, data_y)
    print(constant, coeff)
    print(rg.predict(constant_term=constant, coeff_of_indep_var=coeff,val_of_indep_var=14))