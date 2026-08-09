#===================================================================
#Project: Day of Year
#Course: Cisco Python Essentials 1
#Lab: PE1 Lab 03
#
#Student: Randy Crawford
#Date Started: 07/31/2026
#Date Completed: 08/01/2026
#
#Calculate how many days of a year given that date
#
#====================================================================




def day_of_year(year, month, day):
      if month == 1:
        y=day
        return y
      else:
        y=day
        for m in range(1,month):
            x=days_in_month(year, m)
            y +=x
        return y          

def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        x=29
        return x
    elif year % 400 ==0:
        x =29
        return x
    else:
        x=28
        return x 

def days_in_month(year, m):
    if m == 2:
        x = leap_year(year)
        return x
    elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        x = 31
        return x
    else:
        x = 30
        return x
    

def validate_date(month, day):
    if month>12 or month<1:
        return False
    else:
        if day<1 or day>31:
            return False
        else:
            return True

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_days = [28, 29, 1, 30]

for date in range (4):
    year = test_years[date]
    month = test_months[date]
    day = test_days[date]
    if validate_date(month, day) == False:
        print("Invalid Date")
        break
    else:
        y = day_of_year(year, month, day)
        print("The date ",month,"-",day,"-",year," has ",y," Days!")

#End of Program
