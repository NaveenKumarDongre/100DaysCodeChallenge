# Day- 8 : Get the values of a, b and c (coefficients of quadratic equation) 
# as input from the user and calculate the roots and print as the output.
def discriminant(a,b,c):
    return (b**2) - (4*a*c)

def find_root(a,b,c):
    d = discriminant(a, b, c)
    if (d < 0):
        print("Imaginary Roots")
        return
    else:
        root1 = (-b + pow(d, 0.5))/(2*a)
        root2 = (-b - pow(d, 0.5))/(2*a)
        if (d == 0):
            print("Equal Roots")
            print("Roots:",root1,root2)
        else:
            print("Real Roots")
            print("Roots:", root1,root2)
            
if __name__ == "__main__":
    a, b, c = [int(x) for x in input("Enter the value of a, b, c :- ").split()]
    find_root(a, b, c)
            
        
        
    
    