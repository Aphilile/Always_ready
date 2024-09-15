def divide_nums(num1, num2):

    answer = num1 / num2
    return answer

def divide(a, b):
    """
    Divides one number by another.

    Parameters:
    a (float): The numerator.
    b (float): The denominator. Must not be zero.

    Returns:
    float: The result of the division.

    Raises:
    ZeroDivisionError: If the denominator is zero.
    """
    if b == 0:
        raise ZeroDivisionError("The denominator must not be zero.")
    return a / b
