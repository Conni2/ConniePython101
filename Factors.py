# 4th Project - Factors
# Description: Finding & count factors of a given number | Purpose: To practice while & if statment

def factor():
    number = int(input("Finding the factors of:"))

    i = 1
    count = 0

    while i <= number:
        if number % i == 0:
            count += 1
            print(i)
        i += 1
    print(f"The number of factors of {number} is {count}.")

factor()