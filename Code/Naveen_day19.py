"""
Day 19 coding Statement : 
Write a program to identify if the number is Armstrong number or not
Description
Get an input number from user and check whether the given number is an Armstrong number or not.
E.g. Let the number be 1634,
Here 1^4 + 6^4 + 3 ^4 + 4^4 = 1634
Therefore, this is an Armstrong number
"""
import math
def isArmstrong(num):
    num_digits = int(math.log10(num)) + 1 
    orginal_num = num 
    res_num = 0 
    while num != 0:
        rem = num % 10 
        res_num = res_num + rem**num_digits
        num = num // 10 
    return orginal_num == res_num        

if __name__ == "__main__":
    num = int(input("Enter the number: "))
    if isArmstrong(num):
        print("Armstrong number")
    else:
        print("Not an Armstrong number")  
        