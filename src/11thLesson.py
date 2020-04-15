# ************* Lesson 11 **************
# ************* Exponent Function ******

# Note: 2**3 == 2^3


def raise_to_power(num, pow):
    result = num
    for index in range(1, pow):
        result *= num
    return result


print(raise_to_power(2, 2))
