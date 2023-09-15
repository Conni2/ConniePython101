# 3rd Project - Multiples
# Description: Various calculator using the multiples | Purpose: To practice while statment
# Display all positive integers less than or equal to the third input value that are multiples of the first input value but are not multiples of the second input value.

def multiplenotmultiple():
    print ("Finding multiple of A but not B:")
    first = int(input("A:"))
    second = int(input("B:"))
    max = int(input("Maximum value of multiple:"))
    
    i=1
    while i <= max:
        if i % first == 0 and i % second != 0:
            print(i)
        i += 1


multiplenotmultiple()

#Total sum of the common multiples of two positive integers in the range that is provided by the user

def multiplesum():
    print ("This is to find the common multiples of a and b")
    commonfirst = int(input("a:"))
    commonsecond = int(input("b:"))
    range = int(input("Maximum value of common multiple:"))

    n = 1
    total = 0
    while n <= range:
        if n % commonfirst == 0 and n % commonsecond == 0:
            total += n
        n += 1
    print (total)


multiplesum()