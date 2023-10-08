# 19th Project: Lotto

import random

#Generating numbers
def generate_numbers(n):
    draw_time = 0
    draw_list = []
    while draw_time < n:
        num = random.randint(1, 45)
        if num not in draw_list:
            draw_list.append(num)
            draw_time += 1
    return (draw_list)

#test
print(generate_numbers(5))