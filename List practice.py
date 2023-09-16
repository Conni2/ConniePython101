#9th project - List practice
#Purpose: Understand various functions in list
#TIM: Need to think about the index number after deleting the odd numbers (Because the next index number will remain same, because of the del)

list =[]

list.append(1)
list.append(4)
list.append(9)
list.append(32)
list.append(2)
list.append(5)
list.append(16)

print(list)

i = 0
while i < len(list):
    if int(list[i]) % 2 == 1:
        del list[i]
    else:
        i += 1

print (list)

list.insert(2, 12)
list.sort()

print(list)

def remain (x):
    return x % 13

n = 0
while n < len(list):
    remain(list[n])
    n += 1

print(list)