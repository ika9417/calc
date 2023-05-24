"""
Just another `calculator` yet
"""

import sys
import argparse


parser = argparse.ArgumentParser(
                    prog='Calculator',
                    description='Calculation tool',
                    epilog='Just for fun, to code with friends')


parser.add_argument('--first', help="The first number")
parser.add_argument('--operation', help="The math operation")
parser.add_argument('--second', help="The second number")
# parser.add_argument('--corepart', action=argparse.BooleanOptionalAction, default=False, help=" Use --corepart | --no-corepart to get blablabla")
parser.add_argument('--corepart', type=bool, action=argparse.BooleanOptionalAction, default=False, help=" Use --corepart | --no-corepart to get blablabla")
parser.add_argument('--version', action='version', version='%(prog)s 0.1-alpha')


def addition(first, second):
    """
    :param first: int or float
    :param second: int or float
    :return: the summ of first and second
    """
    return first + second


def subtraction(first, second):
    """
    :param first: int or float
    :param second: int or float
    :return: subtraction of the second from first
    """
    return first - second


def multiplication(first, second):
    """
    :param first: int or float
    :param second: int or float
    :return: multiplication of the first and second
    """
    return first * second


def division(first, second):
    """
    :param first: int or float
    :param second: int or float
    :return: division of the first by second
    """
    return first / second


def interact():
    """
    :return: result of calculation
    """
    print("Enter digit and choice operation type")
    first = float(input("Write first: "))
    second = float(input("Write second: "))
    operation = str(input("Write operation type (+, -, *, /): "))

    return maths (first, operation, second)

    print("Somthing wrong - fallback!")
    sys.exit(1)

def maths (first, operation, second):
    """
    : For internal use only
    :param first: int or float
    :param operation: int or float
    :param second: operation like a '+', '-', '/', or '*'
    :return: result of calculation
    """
    if operation == "+":
        return addition(first, second)
    if operation == "-":
        return subtraction(first, second)
    if operation == "*":
        return multiplication(first, second)
    if operation == "/":
        return division(first, second)
    return None

def clirun(first, operation, second):
    """
    CLI format for tool
    :param first: int or float
    :param operation: int or float
    :param second: operation like a '+', '-', '/', or '*'
    :return: result of calculation
    """
    corepart = ""
    if corepart == True:
     return str(maths(first, operation, second)).split(".")[1]
     # return maths(first, operation, second)

if __name__ == '__main__':
    args = parser.parse_args()
    if len(sys.argv) == 1:
        # не совсем, хак но это другой способ вытягивания аогументов
        print(interact())
    else:
        print(clirun(float(args.first), str(args.operation), float(args.second)), bool(args.corepart) )
        # print(clirun(float(args.first), str(args.operation), float(args.second)))
