#Using while and if, this will display all positive integers less than or equal to the third input value that are multiples of the first input value but are not multiples of the second input value.

def multiplenotmultiple ():
    
    first = int(input("Please input the factor of the numbers you are looking for:"))
    second = int(input("Among these, input the factor of the numbers you want to exclude:"))
    max = int(input("Please write the maximum number of range you would like to print:"))
    
    i=1
    while i <= max:
        if i % first == 0 and i % second != 0:
            print(i)
        i += 1


multiplenotmultiple()