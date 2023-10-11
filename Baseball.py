# 20th Project: Baseball

import random 

#Generate numbers
#TIL: Can set the condition with len(list) with while rather than defining new variable (like i)
def generate_numbers (n):
    numbers = []
    while len(numbers) < n:
        random_num = random.randint(1,45)
        if random_num not in numbers:
            numbers.append(random_num)
    return(numbers)

print(generate_numbers (6))
