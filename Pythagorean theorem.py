#10th Project - Pythagorean theorem
# Purpose: Practicing for statement

for a in range(1, 1000):
    for b in range(1, 1000):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2 and a < b < c:
            print(a, b, c)