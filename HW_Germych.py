import re

a = '10 + 10 - 100 * 0 + 2 + 5'

print(re.findall('\D+', a))

print(re.findall('\W+', a))