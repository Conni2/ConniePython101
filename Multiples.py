#Using while and if, this will display all positive integers less than or equal to the third input value that are multiples of the first input value but are not multiples of the second input value.

def multiplenotmultiple():
    
    first = int(input("Please input the factor of the numbers you are looking for:"))
    second = int(input("Among these, input the factor of the numbers you want to exclude:"))
    max = int(input("Please write the maximum number of range you would like to print:"))
    
    i=1
    while i <= max:
        if i % first == 0 and i % second != 0:
            print(i)
        i += 1


multiplenotmultiple()

#Also using while and if to get total sum of the common multiples of two positive integers in the range that is provided by the user

def multiplesum():
    
    commonfirst = int(input("Please input the first number for the common multiples:"))
    commonsecond = int(input("Please input the second number for the common multiples:"))
    range = int(input("Please input the maximum number in the range of your choice:"))

    n = 1
    total = 0
    while n <= range:
        if n % commonfirst == 0 and n % commonsecond == 0:
            total += n
        n += 1
    print (total)


multiplesum()