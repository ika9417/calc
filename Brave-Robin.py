import re

"""
<ath functions and priority:
The highest: (, )
to low:
    - ** (aka ^), root - # ! not released
    - Trigonometric function
    - *, /
    - +, -
"""


a = "10+10*100-20*2+3+4"

# problem string
# a = "10+10*100-20*2+3+4*3*3*3*3*3"

def stringparse_multiply(input_data):
    """
    :param input_data:
    :param b:
    :return:
    """

    step1 = re.split(r'["*"]', input_data)
    print(step1)
    if len(step1) == 1:
        return input_data

    step2 = re.findall(r'\d+', step1[0])[-1]
    step3 = re.findall(r'\d+', step1[1])[0]
    result_multiply = float(step2) * float(step3)
    print(result_multiply)
    find_string = step2 + "*" + step3
    print(str(input_data.split(find_string))) # "10*100"
    result_string = str(input_data.split(find_string)[0]) + str(result_multiply) + str(input_data.split(find_string)[1])
    print("The result of concatination: ", result_string.replace(" ", ""))
    return stringparse_multiply(result_string.replace(" ", ""))



print(stringparse_multiply(a))
