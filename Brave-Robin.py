"""
Small part of main logic
"""
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


# a = "10+10*100-20*2+3+4"

# problem string
a = "10+10.1*100-20*2+3+4*3*3*3*3*3"


def string_parser_multiply(input_data):
    """
    :param input_data: string - raw data for calculation
    :return: New string with calculated data
    """

    step1 = re.split(r'["*"]', input_data)

    if len(step1) == 1:
        # length
        return input_data

    # https://docs.python.org/3/library/re.html ctr+f
    # "A|B, where A and B can be arbitrary REs, creates a regular expression that will match either A or B."
    step2 = re.findall(r'\d*\.\d+|\d+', step1[0])[-1]
    """
    \d* - digitals and any symbols after 12sd-card
    \. - only one "."
    \d+ - digitals ethernal | infinity
    """
    step3 = re.findall(r'\d*\.\d+|\d+', step1[1])[0]
    result_multiply = float(step2) * float(step3)
    find_string = step2 + "*" + step3 # 10.1*100
    # # https://docs.python.org/3/library/stdtypes.html#str.split
    result_string = str(input_data.split(find_string, 1)[0]) \
                    + str(result_multiply) \
                    + str(input_data.split(find_string, 1)[1])

    print("Recreation: ", input_data.split(find_string, 1)[0], result_multiply, input_data.split(find_string, 1)[1])

    return string_parser_multiply(result_string.replace(" ", ""))


print("The original string is:", a)
print(string_parser_multiply(a))
