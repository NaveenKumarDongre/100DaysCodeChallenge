"""
Day 16 coding Statement : 
Write a program to identify if the number is Perfect number or not.

Description:
Get the input from the user and check whether that number is a perfect number or not.
E.g. Let number is 28, factors of 28 are 1,2,4,7,14. 
Now the sum of all these factors are 28 itself.

"""

def isPerfectNumber(num):
    
    fact_sum = 0 
    for i in range(1, num):
        if num % i == 0:
            fact_sum += i 
            
    return fact_sum == num 

if __name__ == "__main__":
    num = int(input("Enter the number: "))
    if isPerfectNumber(num):
        print(f"{num} is perfect number")
    else:
        print(f"{num} is not perfect number")
    