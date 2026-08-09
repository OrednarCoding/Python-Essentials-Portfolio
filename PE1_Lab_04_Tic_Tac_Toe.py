#===================================================================
#Project: Tic Tac Toe game
#Course: Cisco Python Essentials 1
#Lab: PE1 Lab 04
#
#Student: Randy Crawford
#Date Started: 08/01/2026
#Date Completed: 08/01/2026
#
#Create a Tic Tac Toe display and game
#
#====================================================================
import random
import os

def display_board():
    print("+======================+")
    print("|       |       |      |")
    print("|  ",board[0][0],"  |  ",board[0][1],"  |  ",board[0][2]," |")
    print("|       |       |      |")
    print("+======================+")
    print("|       |       |      |")
    print("|  ",board[1][0],"  |  ",board[1][1],"  |  ",board[1][2]," |")
    print("|       |       |      |")
    print("+======================+")
    print("|       |       |      |")
    print("|  ",board[2][0],"  |  ",board[2][1],"  |  ",board[2][2]," |")
    print("|       |       |      |")
    print("+======================+")
    

def enter_move(move,sign):
        while True:
            try:
                move = int(input("Please enter your move :"))
            except ValueError:
                print("Please only use whole numbers between 1-9")
                continue      
              
    
            if move < 1 or move > 9:
                 print("Please only use whole numbers between 1-9")
                 continue
            
            row = (move - 1)//3
            col = (move - 1)%3

            if board[row][col] == "X" or board[row][col] == "O":
                 print("That sqaure is already occupied.  Please choose a different square.")
                 continue
            
            board[row][col] = sign
            return


def draw_move(move,sign):
    while True:
        move = random.randint(1,9)
        row = (move-1)//3
        col = (move-1)%3
    
        if board[row][col] == "X" or board[row][col] == "O":
            continue
    
        board[row][col] = sign
        return 
        

    
    
def check_win(sign,w):
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
         w=1
         return w
    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
         w=1
         return w
    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
         w=1
         return w
    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
         w=1
         return w
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
         w=1
         return w
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
         w=1
         return w
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
         w=1
         return w
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
         w=1
         return w
    else:
         w=0
         return w
    
def show_winner(sign):
     os.system("cls")
     display_board()
     print("The winner is : ",sign)

def check_tie(t):
     for r in range(3):
          for c in range(3):
               if board[r][c] != "X" and board[r][c] != "O":
                    return 0

     return 1
      
     


     

board = [
        ["1", "2", "3"],
        ["4", "X", "6"],
        ["7", "8", "9"]
]
move=0
w=0
t=0
while w==0:
    display_board()
    sign="O"
    enter_move(move,sign)
    w=check_win(sign,w)
    if w==0:
     t=check_tie(t)
     if t==1:
          sign="None it is a DRAW"
          w=1
     sign="X"
     draw_move(move,sign)   
     w=check_win(sign,w)
     if w == 0:
          t=check_tie(t)
          if t==1:
               sign="None it is a DRAW"
               w=1
show_winner(sign)
#end game

