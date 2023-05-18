def summ(first, second):
    """

    :param first:
    :param second:
    :return:
    """
    return first + second


def substr(first, second):
    return first - second


def mult(first, second):
    return first * second


def divid(first, second):
    return first / second


def interact():
    print("Enter digit and choice operation type")
    first = float(input("Write first: "))
    second = float(input("Write second: "))
    operation = str(input("Write operation type (+, -, *, /): "))

    if operation == "+":
        return summ(first, second)
    elif operation == "-":
        return substr(first, second)
    elif operation == "*":
        return mult(first, second)
    elif operation == "/":
        return divid(first, second)
    else:
        print("Somthing wrong - fallback!")
        exit(1)


if __name__ == '__main__':
    print(interact())
