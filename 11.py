def is_int(input_data):
    if str(input_data)[-1] == "0":
        print("int")
        return int(input_data)
    else:
        print("float")
        return float(input_data)


def multiply(first, second):
    result1 = 0
    result2 = 0

    # if first < second:
    #     is_int(first)
    #     return returnmultiply(second, first)

    # else:
    #     is_int(second)

    for i in range(splitter(second)[0]):
        result1 = result1 + first

    for i in range(splitter(second)[1]):
        result2 = result2 + first
    return result1 + result2/10


def splitter(input_data):
    fullpart = int(input_data)
    decimalpart = (input_data - fullpart) * 10
    return fullpart, int(decimalpart)


print(multiply(20, 1.5))
