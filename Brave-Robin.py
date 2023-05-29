import re

"""
<ath functions and priority:
The highest: "(, )"
to low:
    - ** (aka ^), root - # ! not released
    - Trigonometric function
    - *, /
    - +, -
"""


a = "10+10*100-20*2+5"
# a1 = ""

print(a)
# print("Dumb solution:", re.findall(r'\D', a))

step1 = re.split(r'["*"]', a)
print(step1, len(step1), type(step1))
print(step1[0], " : ", step1[1])
step2 = re.findall(r'\d+', step1[0])[-1]
print(step2, type(step2))
step3 = re.findall(r'\d+', step1[1])[0]
print(step3, type(step3))

result_multiply = float(step2) * float(step3)

print(result_multiply)
