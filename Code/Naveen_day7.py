"""
Day 7 coding Statement: 
Get the number of month and year as input from the user 
and check the number of days present in that month.

Input:
Enter month : 2
Enter year : 2000

Output:
29
"""
def isLeafYear(year):
    if year % 4  == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True 
            else:
                return False 
        else:
            return True 
    else:
        return False 
    
def daysInMonth(month, year):
    
    if month in (1,3,5,7,8,10,12):
        print("Number of Days 31")
    elif month == 2 and isLeafYear(year):
        print("Number of days is 29")
    elif month == 2:
        print("Number of days is 28")
    else:
        print("Number of days is 30")
        
        
if __name__ == "__main__":
    month = int(input("Enter the month: "))
    year  = int(input("Enter the year: "))
    daysInMonth(month, year)