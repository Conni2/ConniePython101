# 10th Project - Pythagorean theorem
# Purpose: Practicing for statement
# TIL: If we know about c using a and b, it's better not to use the for statement for code simplification
# TIL: isinstance() varifies if the data type is integer or not (Boolean)

for a in range(1, 1000):
    for b in range(1, 1000):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2 and a < b < c:
            print(a, b, c)


sides_right_triangle = []

for x in range (1, 1000):
    for y in range (1, 1000):
         z = (x ** 2 + y ** 2) ** 1/2
         if isinstance (z, int) == True:
             sides_right_triangle.append(z)

print(sides_right_triangle)