# 11th project - Reverse elements in lists
# Purpose: To practice list
# TIL: Have to divide the len of list to only go through half way of the loop

numbers = [2, 3, 5, 7, 11, 13, 17, 19]

for left in range(len(numbers)//2):
    right = len(numbers) - left - 1
    temp = numbers[left]
    numbers[left] = numbers[right]
    numbers[right] = temp

print("Reversed list: " + str(numbers))