# 10th Project - Pythagorean theorem
# Purpose: Practicing for statement
# TIL: If we know about c using a and b, it's better not to use the for statement for code simplification
# TIL: datatype - Tuple

for a in range(1, 1000):
    for b in range(1, 1000):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2 and a < b < c:
            print(a, b, c)


sides_right_triangle = []

for x in range(1,100):
    for y in range(x,100):
        for z in range(y,100): 
            if x**2 + y**2 == z**2:
                sides_right_triangle.append((x,y,z))

print(sides_right_triangle)