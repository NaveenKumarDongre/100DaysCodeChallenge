
def vowel_consonant(char):
    
    if char in "aeiouAEIOU":
        print("Vowel")
    elif char.isalpha():
        print("Consonant")
    else:
        print("Invalid Input")
        
        
char = input("Enter the character:") 
vowel_consonant(char)
    