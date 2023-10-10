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
    winning_numbers = sorted(winning_numbers[:6]) + winning_numbers [6:]
    return(winning_numbers)

#test print(draw_winning_numbers())

#Counting matching numbers
def count_matching_numbers(draw_list, winning_numbers):
    matching_counter = 0
    for a in range(len(draw_list)):
        if draw_list[a] in winning_numbers:
            matching_counter += 1
    return(matching_counter)

#test print(count_matching_numbers([1,2,3,4,5], [5, 4, 9]))

#check
def check (draw_list, winning_numbers):
    no_bonus = winning_numbers[:6]
    counter_no_bonus = count_matching_numbers(draw_list, no_bonus)
    counter_with_bonus = count_matching_numbers(draw_list, winning_numbers)
    if counter_no_bonus == 6:
        return(1000000000)
    elif counter_no_bonus == 5 and counter_with_bonus == 6:
        return(50000000)
    elif counter_no_bonus == 5:
        return(1000000)
    elif counter_no_bonus == 4:
        return(50000)
    elif counter_no_bonus == 3:
        return(5000)
    else:
        return(0)
    
#test print(check(numbers_test, winning_numbers_test))