print("hello") # temo
"""
there
and the
and many lines - will be ignored
"""
print('')
print(int(7.5))
print(float(5))
print(str(3*2+2))
variable1 = 7
print(type(variable1)) # additional information

# condition
a = 5
b = 9
if a == b:
    print(a ,b)
else:
    print("Not equal")
print(type(a == b))
messige = "gamar joba"
print(len(messige))
print(messige[-1])


def our_function(one = "3", second = "4"):
    return one + second



print(our_function(2, 6))
print(our_function("5", "Ha "))
print(our_function(4.5, 7))
print(our_function())
