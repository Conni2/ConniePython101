# 19th Project: Lotto

import random

#Generating numbers
#TIL: if ~ not in ~
def generate_numbers(n):
    draw_time = 0
    draw_list = []
    while draw_time < n:
        num = random.randint(1, 45)
        if num not in draw_list:
            draw_list.append(num)
            draw_time += 1
    return (draw_list)

#test print(generate_numbers(5))

#Draw the winning numbers
#TIL: sorted(list) // list slicing (need more practice)
def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return(sorted(winning_numbers[:6]) + winning_numbers [6:])

print(draw_winning_numbers())