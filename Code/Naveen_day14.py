# Day 14 coding Statement : Write a program to reverse a given number
# Input
# 675
# Output
# 576

def reverse_num(num):
    ans = 0 
    while num != 0 :
        rem = num % 10 
        ans = (ans*10) + rem 
        num = num // 10
    return ans 

if __name__ == "__main__":
    num = int(input("Enter the number: "))
    rev_num = reverse_num(num)
    print(f"The reverse of number: {rev_num}")