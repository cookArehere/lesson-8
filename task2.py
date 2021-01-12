"""
Task 2

Write a function that takes in two numbers from the user via input(), call the numbers a and b,
and then returns the value of squared a divided by b, construct a try-except block which raises an exception
if the two values given by the input function were not numbers,
and if value b was zero (cannot divide by zero).
"""


def function(a, b):
    return a ** a / b


if __name__ == '__main__':

    try:
        print(function(a=int(input("Number1: ")), b=int(input("Number2: "))))
    except ValueError:
        print("We need numbers")
    except ZeroDivisionError:
        print("We can't substrack on zero")
