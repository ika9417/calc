""" Pet project for fun """

import math
import sys


def summ(first, second):
    """
    :param first:
    :param second:
    :return:
    """
    return first + second


def substr(first, second):
    """
    This function will just subtract second arg from first.
    Example:
    ----
        >>> print(substr(10,2))
        8
    ----
    """
    return first - second


def multiply(first, second):
    """
    This function is really interesting it also wait two args.
    After then it compare it for detect which arg is bigger for to reduce the number
    of iterations of repetitions of zincls.
    This function using math.fsum module into "for".
    """
    result1 = 0
    result2 = 0

    if first < second:
        second, first = first, second
        return multiply(first, second)

    for i in range(splitter(second)[0]):
        result1 = math.fsum([result1, first])

    for i in range(splitter(second)[1]):
        result2 = math.fsum([result2, first])

    # return result1 + result2/(10 ** splitter(second)[2])
    result = result2 / (10 ** splitter(second)[2])
    return math.fsum([result, result1])


def splitter(input_data):
    """
    This function is using for others function, it splitting (input_data) to for three numbers.
    ----
        >>> print(splitter(10.12))
        (10, 12, 2)
    ----
    """

    fullpart = int(input_data)
    decimalpart = int(str(input_data).split(".")[1])
    stepen10 = len(str(decimalpart))
    return fullpart, decimalpart, stepen10


def divid(first, second):
    """ This function will just make divid two args. """
    return first / second


def interact():
    """
    This is entrypoint of our module
    Defining  args (first,second,operation) for others function.
    """
    print("Enter digit and choice operation type")
    first = float(input("Write first: "))
    second = float(input("Write second: "))
    operation = str(input("Write operation type (+, -, *, /): "))

    if operation == "+":
        return summ(first, second)
    if operation == "-":
        return substr(first, second)
    if operation == "*":
        return multiply(first, second)
    if operation == "/":
        return divid(first, second)

    print("Somthing wrong - fallback!")
    sys.exit(1)


if __name__ == '__main__':
    print(splitter.__doc__)
    print(splitter(10.12))
    # print(splitter(32.43456))
