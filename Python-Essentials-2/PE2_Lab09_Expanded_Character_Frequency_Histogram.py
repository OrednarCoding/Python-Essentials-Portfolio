#===================================================================
# Project: Expanded Character Frequency Histogram
# Course: Cisco Python Essentials 2
# Lab: PE2 Lab 09
#
# Student: Randy Crawford
# Date Started: 08/11/2026
# Date Completed: 08/11/2026
#
# Original Lab Requirements:
# Read a user-selected text file, count the occurrences of each Latin
# letter regardless of case, and display the non-zero letter counts
# in alphabetical order.
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
    return txt
#1002

def char_count(chars):
    for char in chars:
        c=char.upper()
        if c == " ":
            space.append(c)
            
        elif c == "A":
            a.append(c)
           
        elif c == "B":
            b.append(c)
            
        elif c == "C":
            c1.append(c)
            
        elif c == "D":
            d.append(c)
            
        elif c == "E":
            e.append(c)
            
        elif c == "F":
            f.append(c)
            
        elif c == "G":
            g.append(c)
            
        elif c == "H":
            h.append(c)
            
        elif c == "I":
            i.append(c)
           
        elif c == "J":
            j.append(c)
           
        elif c == "K":
            k.append(c)
            
        elif c == "L":
            l.append(c)
            
        elif c == "M":
            m.append(c)
            
        elif c == "N":
            n.append(c)
            
        elif c == "O":
            o.append(c)
            
        elif c == "P":
            p.append(c)
            
        elif c == "Q":
            q.append(c)
            
        elif c == "R":
            r.append(c)
            
        elif c == "S":
            s.append(c)
           
        elif c == "T":
            t.append(c)
            
        elif c == "U":
            u.append(c)
            
        elif c == "V":
            v.append(c)
            
        elif c == "W":
            w.append(c)
           
        elif c == "X":
            x.append(c)
           
        elif c == "Y":
            y.append(c)
            
        elif c == "Z":
            z.append(c)
            
        else:
            special.append(c)
            
#0918
def display_results(letter, clist):
    if len(clist) > 0:
        print(f"{letter}- {len(clist)}")
        return 
#0922       
    
def listchar(text):
    
    for c in text:
        c1=str(c)
        chars.append(c1)
#1104                   

#Main Program
import os

space=[]
special=[]
a=[]
b=[]
c1=[]
d=[]
e=[]
f=[]
g=[]
h=[]
i=[]
j=[]
k=[]
l=[]
m=[]
n=[]
o=[]
p=[]
q=[]
r=[]
s=[]
t=[]
u=[]
v=[]
w=[]
x=[]
y=[]
z=[]
A="A"
B="B"
C1="C"
D="D"
E="E"
F="F"
G="G"
H="H"
I="I"
J="J"
K="K"
L="L"
M="M"
N="N"
O="O"
P="P"
Q="Q"
R="R"
S="S"
T="T"
U="U"
V="V"
W="W"
X="X"
Y="Y"
Z="Z"
SP="Space"
SC="Special Characters"
chars=[]
total=0
text=enterfile()
listchar(text)
char_count(chars)
display_results(A,a)
total += len(a)
display_results(B,b)
total += len(b)
display_results(C1,c1)
total += len(c1)
display_results(D,d)
total += len(d)
display_results(E,e)
total += len(e)
display_results(F,f)
total += len(f)
display_results(G,g)
total += len(g)
display_results(H,h)
total += len(h)
display_results(I,i)
total += len(i)
display_results(J,j)
total += len(j)
display_results(K,k)
total += len(k)
display_results(L,l)
total += len(l)
display_results(M,m)
total += len(m)
display_results(N,n)
total += len(n)
display_results(O,o)
total += len(o)
display_results(P,p)
total += len(p)
display_results(Q,q)
total += len(q)
display_results(R,r)
total += len(r)
display_results(S,s)
total += len(s)
display_results(T,t)
total += len(t)
display_results(U,u)
total += len(u)
display_results(V,v)
total += len(v)
display_results(W,w)
total += len(w)
display_results(X,x)
total += len(x)
display_results(Y,y)
total += len(y)
display_results(Z,z)
total += len(z)
display_results(SP,space)
total += len(space)
display_results(SC,special)
total += len(special)
print(f"The total characters of the file : {len(chars)} vs total count of Characters {total}!")
#0707
#End of Program
