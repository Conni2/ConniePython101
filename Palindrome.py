# 15th project - Palindrome
# Purpose: To practice str indexing
# Improvement needed: Succeeded in Korean but need to change the code in case of English

def palindrome ():
    word = str(input("Please input the word:"))
    reverse = []
    reverse = list(word)
    for left in range(len(reverse)//2):
        right = len(reverse)-left-1
        if reverse[left] != reverse[right]:
            print (False)
        print (True)

palindrome()