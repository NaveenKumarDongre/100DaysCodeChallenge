"""
Get the value of x and y coordinates as input from the user and check in which quadrant the point lies and print it.

Input

10 20

Output

This point lies in first quadrant.

Input

-10 20

Output

This point lies in second quadrant.

"""

x , y = [int(x) for x in input().split()]
if x >= 0 and y >= 0:
    print("This point lies in the first quadrant")
elif x < 0 and y >= 0:
    print("This point lies in the second quadrant")
elif x < 0 and y < 0:
    print("This point lies in the third quadrant")
else:
    print("This point lies in the fourth quadrant")