# 16th Project: Number guess
# Description: Number guess game. The user need to Purpose: Draw the number using random module and compare with the input value
# TIL: Random module (import random, random.randint)
import random

number_guess = random.randint(1, 30)
number_given = random.randint(1, 30)
print(number_guess)
print(number_given)
plus = print(number_guess + number_given)
times = print(str(number_guess * number_given)[-1])
def division(number_guess, number_given):
    if number_guess > number_given:
        print(str(number_guess // number_given)[-1])
    else:
        print(str(number_given // number_guess)[-1])

division(number_guess, number_given)
def zero (number_guess, number_given):
    total_zero = []
    num_zero = 0
    i = 0
    total_zero = list(str(number_guess)+str(number_given))
    while i < len(total_zero):
        if total_zero[i] == 0:
            num_zero += 1
            i += 1
        else:
            i += 1
    print(num_zero)
zero(number_guess, number_given)