# Day 20 
# coding Statement : Write a program to identify 
# if the number is Prime number or not
import math 
def isPrime(num):
    
    if num <= 1:
        return False 
    
    for i in range(2, int(math.sqrt(num)) + 1):
        
        if num % i == 0:
            return False 
    
    return True 

if __name__ == "__main__":
    
    num = int(input("Enter the number: "))
    
    if isPrime(num):
        print(f"{num} is a prime number")
    
    else:
        print(f"{num} is not a prime number")