# Day 18 
# Add two fraction a/b and c/d and print answer in simplest form.
def gcd(a, b):
    if(a == 0):
        return b
    return gcd(b % a, a)

class Fraction:
    def __init__(self, num, deno):
        self.num = num 
        self.deno = deno 
    
    def add(self, f2):
        self.num = (self.num * f2.deno)+(self.deno * f2.num)
        self.deno = (self.deno * f2.deno)
        self.simplify()
        
    def simplify(self):
        common_factor = gcd(self.num, self.deno)
        self.num = self.num // common_factor
        self.deno = self.deno // common_factor
        
    def __str__(self):
        return f"{self.num}/{self.deno}"
        
if __name__ == "__main__":
    n1 , d1 = [int(x) for x in input().split()]
    f1 = Fraction(n1, d1)
    n2 , d2 = [int(x) for x in input().split()]
    f2 = Fraction(n2, d2)
    f1.add(f2)
    print(f1)