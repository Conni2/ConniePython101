# 15th project - Palindrome
# Purpose: To practice str indexing
# Improvement needed: Succeeded in Korean but need to change the code in case of English

def palindromekr ():
    krword = str(input("단어를 입력해주세요:"))
    reverse = []
    reverse = list(krword)
    for left in range(len(reverse)//2):
        right = len(reverse)-left-1
        if reverse[left] != reverse[right]:
            print (False)
        else:
            print (True)

palindromekr()

def palindromeeng ():
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

palindromeeng ()