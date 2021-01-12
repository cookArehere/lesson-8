"""
Task 1

Write a function called oops that explicitly raises an IndexError exception when called.
Then write another function that calls oops inside a try/except state­ment to catch the error.
What happens if you change oops to raise KeyError instead of IndexError?

"""

def error_oops(a=[1,2]):
    return a[(len(a)+1)]

def catch_error(oops):
    try:
        error_oops(oops)
    except IndexError:
        return "catch error IndexError"


if __name__ == '__main__':

    a = [1, 2]
    print(catch_error(a))