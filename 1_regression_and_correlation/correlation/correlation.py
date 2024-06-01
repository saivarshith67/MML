import numpy as np

def correlation_coefficient(x: list, y: list) -> float:
    """
    Calculate correlation coefficient between x and y.
    
    Args:
        x (list): List of x values
        y (list): List of y values
    
    Returns:
        float: Correlation coefficient
    """
    x = np.array(x)
    y = np.array(y)
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    numerator = np.sum((x - mean_x) * (y - mean_y))
    denominator = np.sqrt(np.sum((x - mean_x) ** 2) * np.sum((y - mean_y) ** 2))
    return numerator / denominator


def main() -> None :
    # Example usage of correlation_coefficient function
    x = []
    y = []
    n = int(input("Enter the number of data points: "))

    print("Enter values for x")
    for i in range(n):
        data = float(input("Enter the data: "))
        x.append(data)

    print("Enter values for y")
    for i in range(n):
        data = float(input("Enter the data: "))
        y.append(data)

    correlation = correlation_coefficient(x, y)
    print("Correlation coefficient:", correlation)
    
    pass


if __name__ == '__main__' :
    main()