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
    return(numbers)

#test 
print(generate_numbers ())
