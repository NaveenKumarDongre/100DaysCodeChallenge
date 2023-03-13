# Day 12 coding Statement:  Write a program to find Sum of digits of a number

# Description
# Get a number from user and then find the sum of the digits in the given number.
# E.g. let the number = 341
# Sum of digits is 3+4+1= 8

# Input
# 4521

# Output
# 12

def sumOfDigits(num):
    ans = 0 
    
    while(num!=0):
        ans = ans + (num%10)
        num = num // 10 
    return ans 

if __name__ == "__main__":
    num = int(input("Enter the digit: "))
    print(f"The Sum of Digits is: {sumOfDigits(num)}")