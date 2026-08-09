#===================================================================
#Project: Days in Month
#Course: Cisco Python Essentials 1
#Lab: PE1 Lab 02
#
#Student: Randy Crawford
#Date Started: 07/31/2026
#Date Completed: 07/31/2026
#
#Calculate how many days in a month
#
#====================================================================
def leap_year(x2):
    if x2 % 4 == 0 and x2 % 100 != 0:
        x=29
        return x
    elif x2 % 400 ==0:
        x =29
        return x
    else:
        x=28
        return x 

def tm(x1,x2):
    if x1 == 2:
        x = leap_year(x2)
        return x
    elif x1 == 1 or x1 == 3 or x1 == 5 or x1 == 7 or x1 == 8 or x1 == 10 or x1 == 12:
        x = 31
        return x
    else:
        x = 30
        return x

test_years = [1900, 2000, 2016, 1987]
test_months= [2, 2, 1, 11]

for fd in range (4):
    x1=test_months[fd]
    x2=test_years[fd]
    if x1<13 and x1>0:
        days = tm(x1,x2)
        print("The number of days for month ",x1, "for the year of ",x2," is : ",days)
        
    else:
        print("None")

# End of Program


    