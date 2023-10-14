# 20th Project: Number baseball

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


#print score
#TIL: Can return two values using return(A, B), also try to simplify the code using elif(since this will filter the numbers in the first if)
def get_score(numbers, numbers_user):
    ball = 0
    strike = 0
    for i in range(len(numbers)):
        if numbers[i] == numbers_user[i]:
            strike += 1
        elif numbers[i] in numbers_user:
            ball += 1
    return (strike, ball)


#Game begins
computer = generate_numbers()
tries = 1

while True:
    user_guess = take_guess()
    s, b = get_score(computer, user_guess)
    print ("<#{} Inning> \n Strike: {} | Ball: {}\n".format(tries,s,b))
    tries += 1
    if s == 3:
        print("Three strikes! You won the game after {} winning".format(tries-1))
        break