def multiply(first, second):
    result1 = 0
    result2 = 0

    if first < second:
        return multiply(second, first)

    print(splitter(second)[0], splitter(second)[1], splitter(second)[2])

    for i in range(splitter(second)[0]):
        # print(i)
        result1 = result1 + first

    for i in range(splitter(second)[1]):
        # print("dec: ", i)
        result2 = result2 + first
#     return result1 + result2 / (10 ** splitter(second)[2])
# TODO
#     Need research how avoid devine function

    return result1 + float("0." + str(result2))


def splitter(input_data):
    fullpart = int(input_data)
    decimalpart_raw = input_data - fullpart
    if decimalpart_raw == 0:
        return fullpart, 0, 0
    else:
        stepen10 = len(str(decimalpart_raw)) - 2
        decimalpart = int(str(decimalpart_raw)[2:])
        return fullpart, decimalpart, stepen10


print(multiply(3, 2.97))
