
def isAlphabet(s):
    
    return s.isalpha()
    

# print(isAlphabet(s))


"""
Day 2 coding Statement : Write a program to identify if the character is an alphabet or not.

Description:

Take an input character from user and check whether it is an alphabet or not.

Input :

A

Output: 

Alphabet

Input:

7

Output:

Not an alphabet

"""

def isAlphabet(ch):
    
    if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
        print("Is Alphabet")
    else:
        print("Not an alphabet")
# Output
s = input()
isAlphabet(s)