#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    The factorial of a number n is the product of all positive integers less than or equal to n.
    It is denoted as n! and is defined as:
        n! = n * (n-1) * (n-2) * ... * 1
    Special case: 0! = 1

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the input number n. If n is 0, returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
