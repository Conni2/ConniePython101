# 19th Project: Lotto

import random

def generate_numbers(n):
    draw_time = 0
    draw_list = []
    while draw_time < n:
        num = random.randint(1, 45)
        if num not in draw_list:
            draw_list.append(num)
            draw_time += 1
    print (draw_list)

generate_numbers(5)