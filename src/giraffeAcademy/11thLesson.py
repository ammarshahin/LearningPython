# ************* Lesson 11 **************
# ************* Exponent Function ******

# Note: in python >> 2**3 == 2^3


def raise_to_power(num, pow):
    result = 1
    for index in range(pow):
        result *= num
    return result


print(raise_to_power(3, 5))
print(pow(3, 5))  # build in func
