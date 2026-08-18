 #===================================================================
#Project: Your Own Split Function
#Course: Cisco Python Essentials 2
#Lab: PE2 Lab 01
#
#Student: Randy Crawford
#Date Started: 08/01/2026
#Date Completed:08/02/2026
#
#Create a function that reproduces the basic behavior of split()
#
#====================================================================
def own_split(text):
    word=""
    words=[]
    x=0

    
    for letter in text:

        x +=1
        
        if letter != " " and x==(len(text)):
            word = word + letter
            words.append(word)
            
        elif letter == " ":
            if word =="":
                word=""
                continue
            else:
                words.append(word)
                word=""
        else:
            word = word + letter
    return words
   
text="Python is Fun"
seperate_words=[]

seperate_words=own_split(text)
print(seperate_words)
#End of Program.

