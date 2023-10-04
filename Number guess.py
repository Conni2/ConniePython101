# 16th Project: Number guess
# Description: Number guess game. The user need to Purpose: Draw the number using random module and compare with the input value
# TIL: Random module (import random, random.randint) / Can have multiple conditions for while statement / white space (for enter): \n
import random

# Defining variables
number_A = random.randint(1, 30)
number_B = random.randint(1, 30)
num_tries = 4
tries = 0
guess_A = 0
guess_B = 0

print("~Welcome to Guessing game!~\nYou have to find two positive integers between 1 to 30(inclusive). To get higher score, you have to find the numbers with small hints. These constants are defined as A and B.")

# First hint
if number_A > number_B:
    print("A is bigger than B")
else:
    print("B is equal or bigger than A")

# Formulas for user requests
sum = number_A + number_B
product = str(number_A * number_B)[-1]
def quotient_cal(number_A, number_B):
    if number_A > number_B:
        return(str(number_A // number_B))
    else:
        return(str(number_B // number_A))
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

# User request processing
def user_request(value):
    if value == "sum":
        print(sum)
    elif value == "product":
        print(product)
    elif value == "quotient":
        print(quotient)
    elif value == "zeros":
        print(zeros)

# Guessing game starts
while guess_A != number_A and guess_B != number_B and tries < num_tries:
    request = str(input("<Attemps left: {}> \nChoose the value you would like to see(sum, (unit digit of)product, quotient, and (the number of)zeros):".format(num_tries - tries)))
    user_request(request)
    guess_A = int(input("A:"))
    guess_B = int(input("B:"))
    tries += 1

if guess_A == number_A and guess_B == number_B:
    print("Congraturations! You broke the code! \nScore: {}".format((num_tries-tries)*10))
else:
    print("Game over\n The answer is A:{}  B:{}".format(number_A, number_B))