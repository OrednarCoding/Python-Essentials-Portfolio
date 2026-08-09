#===================================================================
# Project: Palindromes
# Course: Cisco Python Essentials 2
# Lab: PE2 Lab 05
#
# Student: Randy Crawford
# Date Started: 08/07/2026
# Date Completed: 08/07/2026
#
# Determine whether entered text is a palindrome by comparing its
# letters while ignoring case and non-letter characters.
#===================================================================
def pali_input():
    pali=input("Please enter the suspected Palindrome :")
    return pali
def normalize(code):
    cd1=[]
    code = code.upper()
    for i in code:
        if i in ALPHA or i in num:
            cd1.append(i)
        else:
            continue
    return cd1
#1002
            

def compare(pal):
    cd2=[]
    for let in range(len(pal)-1,-1,-1):
        cd2.append(pal[let])
    for i in range(len(pal)):
        if pal[i] != cd2[i]:
            return False
        else:
            continue
    return True
#0918


def display_results(ans):
    if ans == True:
        print("This message is a Palindrome!!!")
    else:
        print("Sorry this is not a Palindrome.")
#0922

#Main Program
ALPHA="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="0123456789"
code=pali_input()
pal=normalize(code)
ans=compare(pal)
display_results(ans)
#1104
#End of Program


