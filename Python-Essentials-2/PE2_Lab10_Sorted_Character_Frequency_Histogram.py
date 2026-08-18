#===================================================================
# Project: Sorted Character Frequency Histogram
# Course: Cisco Python Essentials 2
# Lab: PE2 Lab 10
#
# Student: Randy Crawford
# Date Started: 08/12/2026
# Date Completed: 08/12/2026
#
# Original Lab Requirements:
# Read a user-selected text file, count the occurrences of each Latin
# letter regardless of case, and display the non-zero letter counts
# in alphabetical order. Now using a dictionary.
#
# Student-Added Requirements:
# This version expands the original lab by accounting for every
# character read from the file. Latin letters are counted individually
# without regard to case. Regular spaces are counted in a separate
# category. All remaining characters, including numbers, punctuation,
# symbols, tabs, and line returns, are counted as special characters.
#
# Grading Note:
# The added space and special-character categories go beyond the
# original lab requirements. They demonstrate additional character
# classification, conditional logic, and verification that every
# character read from the file is included in exactly one category.
#
# Verification:
# Total letter counts + spaces + special characters must equal the
# total number of characters read from the file.
#
#===================================================================


def enterfile():
    os.chdir(r"C:\\Users\\radcr\\Downloads")
    filename=input("Enter the name of the file: ")
    f = open(filename, "r")
    txt = f.read()
    f.close()
    return txt,filename
#1002

def char_count(chars):
    for char in chars:
        c=char.upper()
        if c == " ":
            space.append(c)
        elif c in letter_count:
            letter_count[c] += 1
        else:
            special.append(c)
            
#0918
def display_results(sd):
    for letter, count in sd:
        if count > 0:
            print(f"{letter} - {count}")
    
    print("The number of spaces = ", len(space))
    print("The number of specials = ", len(special))
#0922 
def sorted_dictionary(letter_count):
    sorted_dic  = sorted(letter_count.items(), key=lambda item: item[1], reverse=True)
    return sorted_dic
#1104
    
def write_file(fn):
    os.chdir(r"C:\\Users\\radcr\\Downloads")
    f = open(fn, "w")
    for letter, count in sd:
        if count > 0:
            f.write(f"{letter} - {count}\n")
    f.write(f"Spaces - {len(space)}\n")
    f.write(f"Special Characters - {len(special)}\n")
    f.close()
#0707
        
    

                  

#Main Program
import os
os.system("cls")
letter_count={
    "A":0,
    "B":0,
    "C":0,
    "D":0,
    "E":0,
    "F":0,
    "G":0,
    "H":0,
    "I":0,
    "J":0,
    "K":0,
    "L":0,
    "M":0,
    "N":0,
    "O":0,
    "P":0,
    "Q":0,
    "R":0,
    "S":0,
    "T":0,
    "U":0,
    "V":0,
    "W":0,
    "X":0,
    "Y":0,
    "Z":0,
    }
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
space=[]
special=[]
sd={}
chars,fn = enterfile()
char_count(chars)
sd = sorted_dictionary(letter_count)

display_results(sd)
fn = fn +(".hist")
write_file(fn)


#1216
#End of Program
