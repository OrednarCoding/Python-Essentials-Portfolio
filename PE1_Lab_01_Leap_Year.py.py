#===================================================================
#Project: Leap Year
#Course: Cisco Python Essentials 1
#Lab: PE1 Lab 01
#
#Student: Randy Crawford
#Date Started: 07/31/2026
#Date Completed: 07/31/2026
#
#Calculate if the year in question is a Leap Year
#
#====================================================================
def leap_year(y): 
    if y % 4 == 0 and y % 100 != 0:
        x="True this is a Leap Year!"
        return x
    elif y % 400 ==0:
        x = "True this is a Leap Year!"
        return x
    else:
        x="False this is not a Leap Year!"
        return x 
        
            

        


years=[2000,1900,2016,1987,2024,2100]

for y in (years):
    x=leap_year(y)
    print("The year : ",y, "is ", x)

print("I Hope this works for you.")

#End of Program


        
        