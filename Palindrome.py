# 15th project - Palindrome
# Purpose: To practice str indexing
# Challenge: Succeed in Korean but need to fix with alphabet

def palindrome (word):
    reverse = []
    reverse = list(word)
    for left in range(len(reverse)//2):
        right = len(reverse)-left-1
        if reverse[left] != reverse[right]:
            print (False)
        print (True)

palindrome("토마토")