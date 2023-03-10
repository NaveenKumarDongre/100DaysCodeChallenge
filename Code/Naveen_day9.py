# Day-9 : Take an integer as the input from the user 
# and then calculate the numberof digits in the 
# given input and print it as the output.

def count_digits(num):
    if num < 0:
        num = num * (-1)
    digits = 0 
    while num != 0:
        
        digits += 1
        num = num // 10 
    return digits 


num = int(input("Enter the digits: "))
print("The number of digits:", count_digits(num))