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

#Counting matching numbers
def count_matching_numbers(list_1, list_2):
    matching_counter = 0
    for a in range(len(list_1)):
        if list_1[a] in list_2:
            matching_counter += 1
    return(matching_counter)

#test
print(count_matching_numbers([1,2,3,4,5], [5, 4, 9]))
