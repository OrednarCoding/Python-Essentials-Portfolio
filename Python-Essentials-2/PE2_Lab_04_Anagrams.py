#===================================================================
# Project: Anagrams
# Course: Cisco Python Essentials 2
# Lab: PE2 Lab 04
#
# Student: Randy Crawford
# Date Started: 08/06/2026
# Date Completed: 08/06/2026
#
# Determine whether two words or phrases are anagrams by comparing
# their letters while ignoring case and non-letter characters.
#===================================================================

def message_enter(a):
    print("Please enter the",a)
    x=input("message :")
    return x
#0707
  
def normalize(text):
    code=[]
    text=text.upper()
    for l in text:
        if l in ALPHA:
            code.append(l)
        else:
            continue
    return code
#1216
def candc(code1,code2):
    if len(code1) == len(code2):
        length=0
        length = len(code1)
        for e in range (length-1, -1, -1):
            if code1[e] in code2:
                position = code2.index(code1[e])
                del code1[e]
                del code2[position]
            else:
                return False
        return True
    return False
#0304
def answer(ans):
    if ans == True:
        print("These are Anagrams congratulations ")
    else:
        print("These are not anagrams, Sorry")
#0410




ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a="first"
messone = message_enter(a)
a="second"
mestwo = message_enter(a)
code1=normalize(messone)
code2=normalize(mestwo)
ans = candc(code1,code2)
answer(ans)
#2008
#End of Program
