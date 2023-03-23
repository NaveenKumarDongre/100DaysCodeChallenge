"""
Day 21 coding Statement : 
Write a program to identify if the number is Palindrome or not.
"""

def isPalindrome(num):
    original_num = num 
    reverse_num = 0 
    
    while num != 0:
        rem = num % 10 
        reverse_num = reverse_num*10 + rem
        num = num // 10
    return original_num == reverse_num  

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    if isPalindrome(n):
        print(f"{n} is palindrome")
    else:
        print(f"{n} is not a palindrome") 
        