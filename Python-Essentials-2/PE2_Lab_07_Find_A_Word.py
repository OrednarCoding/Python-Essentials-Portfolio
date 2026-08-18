#===================================================================
# Project: Find a Word
# Course: Cisco Python Essentials 2
# Lab: PE2 Lab 07
#
# Student: Randy Crawford
# Date Started: 08/08/2026
# Date Completed:
#
# Determine whether all letters of a word appear in the correct
# order within a second string.
#
#1002,0918,0922,1104,0707,1216,0304,0410,0114,2008
#===================================================================
def enter_word():
    while True:
        letters=""
        code=[]
        letters=input("Please enter the key word letters only please : ")
        letters=letters.upper()
        for l in letters:
            code.append(l)
        test=code
        wrd=validation(test)
        if wrd != False:
            return test
        else:
            continue
#1002

def validation(test):
    
    for x in test:
        if x not in alpha:
            print("Please only use letters no numbers or symbols.")
            return False
    return True
#0918  

def enter_text():
    while True:
        texts=""
        code=[]
        c1=[]
        texts=input("Please enter the testing phrase : ")
        texts=texts.upper()
        for t in texts:
            code.append(t)
        for c in code:
            if c !=" ":
                c1.append(c)
            else:
                continue
        test=c1
        wrd=validation(test)
        if wrd != False:
            return test
        else:
            continue
#0922
          
                
                

def find_word(word,text):
    for w in word:
        if w in text:
            position=text.index(w)
            del text[0:position+1]
        else:
            return False
    return True
#1104
def display(ans):
    if ans == True:
        print("The letters of the key word appear in the correct order in the testing phrase.")
    else:
        print("The letters of the key word do not appear in the correct order in the testing phrase.")
#0707    

#Main Program
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
word=enter_word()
text=enter_text()
ans=find_word(word,text)
display(ans)
#1216
#End of Program




