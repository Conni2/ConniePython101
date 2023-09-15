# 6th Project - Fibonacci Sequence
# Description: Fibonacci sequence | Purpose: Practice while statement
# TIL: Using other variable to save "previous" value before update "previous" value into "current" for calculating next term

previous = 0
current = 1
i = 1

while i <= 10:
    print(current)
    temp = previous
    previous = current
    current = current + temp
    i += 1