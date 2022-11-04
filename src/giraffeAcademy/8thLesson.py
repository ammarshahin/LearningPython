# ************* Lesson 8 **************
# ************* If statement **************
'''
is_male = False

if is_male:
    print("you are male")
elif not(is_male):
    print("you aren't a male")
else:
    pass # 'pass' is the keyword for continue (basically don't do anything) {else is a MUST in python!!!!}
    

'''

'''
is_male = False
is_tall = True

if is_male and is_tall:
    print("you are male and tall")
elif is_male or not(is_tall):
    print("you are male but not tall")
elif not(is_male) or is_tall:
    print("you are tall but not male")
else:
    print("you are neither male or tall")
'''
# Conditional operators >> [== , <= , >= , != , or , not , and]


# def max_num(num1, num2, num3):
#     result = num1
#     if (num2 >= num1) and (num2 >= num3):
#         result = num2
#     elif (num3 >= num1) and (num3 >= num2):
#         result = num3
#     else:
#         pass
#     return result

def max_num(num1, num2, num3):
    if (num2 >= num1) and (num2 >= num3):
        return num2
    elif (num3 >= num1) and (num3 >= num2):
        return num3
    else:
        return num1


is_max = max_num(6, 8, 7)
print(is_max)
