import math

def summ(first, second):
    return first + second


def substr(first, second):
    return first - second


def multiply(first, second):
    result1 = 0
    result2 = 0

    if first < second:
        return multiply(second, first)

    for i in range(splitter(second)[0]):
        result1 = math.fsum([result1, first])

    for i in range(splitter(second)[1]):
        result2 = math.fsum([result2, first])

    # return result1 + result2/(10 ** splitter(second)[2])
    result = result2 / (10 ** splitter(second)[2])
    return math.fsum([result, result1])


def splitter(input_data):
    fullpart = int(input_data)
    decimalpart = int(str(input_data).split(".")[1])
    stepen10 = len(str(decimalpart))
    return fullpart, decimalpart, stepen10


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
        return multiply(first, second)
    elif operation == "/":
        return divid(first, second)
    else:
        print("Somthing wrong - fallback!")
        exit(1)


if __name__ == '__main__':
    print(interact())
    # print(splitter(32.43456))
