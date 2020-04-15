# ************* Lesson 11 **************
# ************* Exponent Function ******

# Note: 2**3 == 2^3


def raise_to_power(num, pow):
    for index in range(0, pow):
        num *= num
    return num


print(raise_to_power(2, 3))
