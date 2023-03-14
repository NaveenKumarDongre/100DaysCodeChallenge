# Day 13 coding Statement:  
# Write a program to find Sum of N natural numbers

def sumOfNaturalNumber(n):
    return n*(n+1)//2 

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    result = sumOfNaturalNumber(n)
    print(f"The sum of first {n} natural number are: {result}")