# Day 11 coding Statement:  
# Write a program to find Fibonacci series up to n

def fibonacci(n):
    a = 0
    b = 1
    if a == 1:
        print(0)
    elif a == 2:
        print(f"{a}, {b}") 
        
    
    else:
        print(f"{a}, {b}", end=", ")
        for i in range(n-2):
            c = a + b 
            print(c,end=", ")
            a = b 
            b = c 
            
n = int(input())
fibonacci(n)
            