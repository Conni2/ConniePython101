# 15th project - Palindrome
# Purpose: To practice str indexing

# First attempt: Thought of '토마토' which is a common palindrome in korean (meaning tomato). Since it consists of three Korean alphabets, I only thought of comparing the alphabet one by one
def palindrome1 ():
    tomato = str(input("Please input '토마토':"))
    reverse = []
    reverse = list(tomato)
    for left in range(len(reverse)//2):
        right = len(reverse)-left-1
        if reverse[left] != reverse[right]:
            print (False)
        else:
            print (True)

palindrome1()

# The first code had a problem that if I input more than three vocabs, the code prints the result comparing the alphabets one by one

# Second attempt: Using "join" from the last project, I tried to reverse the vocabulary and then change it into str, and then compare it with the input value to see if it is palindrome

def palindrome ():
    word = str(input("Please input the word:"))
    reversed = []
    reversed = list(word)
    for left in range (len(reversed)//2):
        right = len(reversed)-left-1
        temp = reversed[left]
        reversed[left] = reversed[right]
        reversed[right] = temp
    reversed_word = ''.join(reversed)
    if reversed_word == word:
        print(True)
    else:
        print(False)

palindrome ()