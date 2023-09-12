previous = 0
current = 1
i = 1

while i <= 10:
    print(current)
    temp = previous
    previous = current
    current = current + temp
    i += 1