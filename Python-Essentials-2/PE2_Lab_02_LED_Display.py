#===================================================================
#Project: LED Display
#Course: Cisco Python Essentials 2
#Lab: PE2 Lab 02
#
#Student: Randy Crawford
#Date Started: 08/02/2026
#Date Completed: 08/02/2026
#
#Display decimal digits using a simulated seven-segment LED display.
#
#====================================================================
hhh="###"
hsh="# #"
shs=" # "
ssh="  #"
hss="#  "
shh=" ##"
hhs="## "
row0=[]
row1=[]
row2=[]
row3=[]
row4=[]


dictionary = {
    "0":[hhh,hsh,hsh,hsh,hhh,],
    "1":[shs,shs,shs,shs,shs],
    "2":[shh,hsh,ssh,shs,hhh],
    "3":[hhh,ssh,shh,ssh,hhh],
    "4":[hsh,hsh,hhh,ssh,ssh],
    "5":[hhh,hss,hhh,ssh,hhh],
    "6":[shs,hss,hhs,hsh,hhh],
    "7":[hhh,ssh,ssh,ssh,ssh],
    "8":[hhh,hsh,hhh,hsh,hhh],
    "9":[hhh,hsh,hhh,ssh,ssh]
    }
#=====1002=====
def get_input():
    while True:
        try:
            n=int(input("Enter any size number :"))
        except:
            print("A number please")
            continue
        return n   
#=====0918======
def determine_board_size(number):
    dis=[]
    for letter in number:
        dis = dictionary[letter]
        for i in range(5):
            if i == 0:
                row0.append(dis[i])
                row0.append("  ")
            if i == 1:
                row1.append(dis[i])
                row1.append("  ")
            if i == 2:
                row2.append(dis[i])
                row2.append("  ")
            if i == 3:
                row3.append(dis[i])
                row3.append("  ")
            if i == 4:
                row4.append(dis[i])
                row4.append("  ")
def print_display():
    r0=""
    r1=""
    r2=""
    r3=""
    r4=""

    for r in range(len(row0)):
        r0 += row0[r]
    for s in range(len(row1)):
        r1 += row1[s]
    for t in range(len(row2)):
        r2 += row2[t]
    for u in range(len(row3)):
        r3 += row3[u]
    for v in range(len(row4)):
        r4 += row4[v]


    print(r0)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
#=====1104=====

number=str(get_input())
determine_board_size(number)
print_display()
#End of Program


