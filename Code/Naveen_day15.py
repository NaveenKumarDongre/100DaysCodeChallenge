"""
Day 15 coding Statement : Write a program to identify if the number is Strong number or not
Description
Get a number as input from user and then check whether that number is a strong number or not. 
A number is said to be strong number if the sum of the factorial of each digit in the number 
is same as that of the number.
E.g. let the number be 145
Here 1! + 4! + 5! is 1 + 24 + 120 which is equal to 145 itself.
"""
def factorial(num):
    if num <= 1:
        return 1 
    res = 1
    for i in range(2,num+1):
        res = res * i 
    return res 

def isStrongNumber(num):
    original = num 
    fact_sum = 0 
    while num != 0:
        rem = num % 10
        fact_sum += factorial(rem) 
        num = num // 10 
    return original == fact_sum 
if __name__ == "__main__":
    num = int(input("Enter the number: "))
    if(isStrongNumber(num)):
        print(f"{num} is strong number")
    else:
        print(f"{num} is not a strong number")
        
        
        