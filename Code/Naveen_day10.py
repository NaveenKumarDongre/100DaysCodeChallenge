#Find factorial of a number

# Iterative method 
def factorial(n):
    if n <= 1:
        return 1 
    res = 1 
    for i in range(2,n+1):
        res = res * i 
    return res 

# Recursion method 
def factorial_recc(n):
    if n <= 1:
        return 1 
    return n*factorial_recc(n-1)

if __name__ == "__main__":
    n = int(input("Enter the number: ")) 
    print(f"The factorial of {n} is {factorial(n)}")
    print(f"The factorial of {n} using recursion {factorial_recc(n)}")