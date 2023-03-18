"""
Day 17 coding Statement : Write a program to find the Factors of a number
Description:
Get an input from the user and find the factors of the number.
Input:
4
Output:
1,2,4
"""  

def factors(num):
    for i in range(1,num+1):
        if i == num:
            print(i)
            return 
        if num % i == 0:
            print(i, end=",")
        
if __name__ == "__main__":
    num = int(input("Enter the number: "))
    factors(num)
        