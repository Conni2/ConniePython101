# 20th Project: Baseball

import random 

#Generate numbers
#TIL: Can set the condition with len(list) with while rather than defining new variable (like i)
def generate_numbers():
    numbers = []
    while len(numbers) < 3:
        random_num = random.randint(0,9)
        if random_num not in numbers:
            numbers.append(random_num)
    print("Three different numbers between 0 and 9 were drawn in random order.\n")
    return(numbers)

generate_numbers()

#User input receive
def take_guess():
    print("Please type your choice of number in order")
    numbers_user = []
    while len(numbers_user) < 3:
        user_num = int(input("Your number #{}:".format(len(numbers_user)+1)))
        if user_num > 9 or user_num < 0:
            print ("{} is out of range. Try again.".format(user_num))
        elif user_num in numbers_user:
            print ("{} is a duplicate number. Try again".format(user_num))
        else:
            numbers_user.append(user_num)
    return(numbers_user)

print(take_guess())