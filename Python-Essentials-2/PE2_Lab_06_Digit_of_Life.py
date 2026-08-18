#===================================================================
# Project: Digit of Life
# Course: Cisco Python Essentials 2
# Lab: PE2 Lab 06
#
# Student: Randy Crawford
# Date Started: 08/07/2026
# Date Completed: 08/07/2026
#
# Calculate the Digit of Life by repeatedly summing the digits of
# an entered birth date until a single digit remains.
#1002,0918,0922,1104,0707,1216,0304,0410,0114,2008
#===================================================================
def enter_bday():
    while True:
        
        date=input("Please enter your birthday in the (YYYYMMDD) format if a single digit day or month add a 0 before it : ")
        if len(date) !=8:
            print("Please try again that date was the wrong length.")
            continue
        d1=[]
        for d in date:
            d1.append(d)
        vd=validation(d1)
        if vd != False:
            return d1
#1002

def validation(d1):
    num="0123456789"
    for x in d1:
        if x not in num:
            print("Please only use the number format provided.")
            return False
    return True
#0918

def calculation(value):
    total=0
    for v in value:
        vt=int(v)
        total +=vt
    if total >9:
        total=str(total)
        t1=single_digit(total)
        return t1
    else:
        return total
#0922
      

def single_digit(total):
    t3=int(total)
    while t3 > 9:
        t6=0
        t3=str(t3)
        for t4 in t3:
            t5=int(t4)
            t6 +=t5
        t3=t6
    return t3    
#1104

def display(calc):
    print("Congratulations your Digit of Life is : ",calc)
#0707

#Main program
value=enter_bday()
calc=calculation(value)
display(calc)
#1216
#End of Program




