# 16th Project: Number guess
# Description: Number guess game. The user need to Purpose: Draw the number using random module and compare with the input value
# TIL: Random module (import random, random.randint)
import random

# draw random numbers
number_A = random.randint(1, 30)
number_B = random.randint(1, 30)
print(number_A)
print(number_B)

# First hint
def hint_1(number_A, number_B):
    if number_A > number_B:
        print("A is bigger than B")
    else:
        print("B is equal or bigger than A")
hint_1(number_A, number_B)

# Hints will be given according to user's request. Users are allowed to request one value of (sum, unit digit of product, unit digit of quotient, number of 0)
# First request won't deduct the point
sum = number_A + number_B
product = str(number_A * number_B)[-1]
def quotient_cal(number_A, number_B):
    if number_A > number_B:
        return(str(number_A // number_B)[-1])
    else:
        return(str(number_B // number_A)[-1])
quotient = quotient_cal(number_A, number_B)
def zero (number_A, number_B):
    total_zero = []
    num_zero = 0
    i = 0
    total_zero = list(str(number_A)+str(number_B))
    while i < len(total_zero):
        if total_zero[i] == 0:
            num_zero += 1
            i += 1
        else:
            i += 1
    return(num_zero)
zeros = zero(number_A, number_B)

