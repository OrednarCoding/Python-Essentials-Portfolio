#===================================================================
# Project: Sudoku
# Course: Cisco Python Essentials 2
# Lab: PE2 Lab 08
#
# Student: Randy Crawford
# Date Started: 08/09/2026
# Date Completed: 08/11/2026
#
# Determine whether a 9x9 Sudoku board contains a valid solution by
# checking its rows, columns, and 3x3 sub-squares.
#
#1002,0918,0922,1104,0707,1216,0304,0410,0114,2008
#===================================================================
def display_board(board):   
    star="*"
    star = star*55
    print(star)
    for i in range(9):
        print(f"| ",board[i][0]," | ",board[i][1]," | ",board[i][2]," | ",board[i][3]," | ",board[i][4]," | ",board[i][5]," | ",board[i][6]," | ",board[i][7]," | ",board[i][8]," |")
        print(star)
    return
#1002      
def enterboard():
    rows=9
    columns=9
    os.system("cls")
    for r in range(rows):
        print("Here is an Invalid board please enter in your information to validate your board.")
        display_board(board) 
        for c in range(columns):
            while True:
                rs=r+1
                cs=c+1
                num=input(f"Enter for spot : Row {rs} Column {cs} :")
                ans = validate_entry(num)
                if ans == False:
                    board[r][c]=num
                    break
                else:
                    print("Please only use numbers 1-9!!")
                    continue
#0918 
def validate_entry(num):
    if num not in numset:
        return True
    else:
        return False
#0922
def invalid():
    os.system("cls")
    display_board(board)
    print("This is an Invalid Sudoku puzzle.")
    raise SystemExit   
#1104
def assign_rows():
    for r in range(9):
        for c in range(9):
            if r == 0:
                row1.append(board[r][c])
            elif r == 1:
                row2.append(board[r][c])
            elif r == 2:
                row3.append(board[r][c])
            elif r == 3:
                row4.append(board[r][c])
            elif r == 4:
                row5.append(board[r][c])
            elif r == 5:
                row6.append(board[r][c])
            elif r == 6:
                row7.append(board[r][c])
            elif r == 7:
                row8.append(board[r][c])
            elif r == 8:
                row9.append(board[r][c])
#0707            
def assign_columns():
    for r in range(9):
        for c in range(9):
            if c == 0:
                col1.append(board[r][c])
            if c == 1:
                col2.append(board[r][c])
            if c == 2:
                col3.append(board[r][c])
            if c == 3:
                col4.append(board[r][c])
            if c == 4:
                col5.append(board[r][c])
            if c == 5:
                col6.append(board[r][c])
            if c == 6:
                col7.append(board[r][c])
            if c == 7:
                col8.append(board[r][c])
            if c == 8:
                col9.append(board[r][c])
#1216            
def assign_squares():
    for r in range(9):
        for c in range(9):
            if r < 3 and c < 3:
                sq1.append(board[r][c])
            elif 2 < r < 6 and c < 3:
                sq2.append(board[r][c])
            elif r > 5 and c < 3:
                sq3.append(board[r][c])
            elif r < 3 and 2 < c < 6:
                sq4.append(board[r][c])
            elif 2 < r < 6 and 2 < c < 6:
                sq5.append(board[r][c])
            elif r > 5 and 2 < c < 6:
                sq6.append(board[r][c])
            elif r < 3 and c > 5:
                sq7.append(board[r][c])
            elif 2 < r < 6 and c > 5:
                sq8.append(board[r][c])
            elif r > 5 and c > 5:
                sq9.append(board[r][c])
#0304
def clear_rcs():
    sq1.clear()
    sq2.clear()
    sq3.clear()
    sq4.clear()
    sq5.clear()
    sq6.clear()
    sq7.clear()
    sq8.clear()
    sq9.clear()
    row1.clear()
    row2.clear()
    row3.clear()
    row4.clear()
    row5.clear()
    row6.clear()
    row7.clear()
    row8.clear()
    row9.clear()
    col1.clear()
    col2.clear()
    col3.clear()
    col4.clear()
    col5.clear()
    col6.clear()
    col7.clear()
    col8.clear()
    col9.clear()
#0114
def validate_lists():
    clear_rcs()
    assign_rows()
    assign_columns()
    assign_squares()
    check_rows()
    check_columns()
    check_squares()
#2008
def check_rows():
    lists=row1
    check_list(lists)
    lists=row2
    check_list(lists)
    lists=row3
    check_list(lists)
    lists=row4
    check_list(lists)
    lists=row5
    check_list(lists)
    lists=row6
    check_list(lists)
    lists=row7
    check_list(lists)
    lists=row8
    check_list(lists)
    lists=row9
    check_list(lists)
#1002
def check_columns():
    lists=col1
    check_list(lists)
    lists=col2
    check_list(lists)
    lists=col3
    check_list(lists)
    lists=col4
    check_list(lists)
    lists=col5
    check_list(lists)
    lists=col6
    check_list(lists)
    lists=col7
    check_list(lists)
    lists=col8
    check_list(lists)
    lists=col9
    check_list(lists)
#0918
def check_squares():
    lists=sq1
    check_list(lists)
    lists=sq2
    check_list(lists)
    lists=sq3
    check_list(lists)
    lists=sq4
    check_list(lists)
    lists=sq5
    check_list(lists)
    lists=sq6
    check_list(lists)
    lists=sq7
    check_list(lists)
    lists=sq8
    check_list(lists)
    lists=sq9
    check_list(lists)
#0922  
def check_list(lists):
    for c in range(1,10,+1):
        m=str(c)
        if m not in lists:
            invalid()
#1104
def congrats():
    os.system("cls")
    display_board(board)
    print("THIS IS A VALID SUDOKU BOARD CONGRATS!!!!!")
    raise SystemExit
#0707

# Main Program
import os
board = [
    ["1","1","1","1","1","1","1","1","1"],
    ["2","2","2","2","2","2","2","2","2"],
    ["3","3","3","3","3","3","3","3","3"],
    ["4","4","4","4","4","4","4","4","4"],
    ["5","5","5","5","5","5","5","5","5"],
    ["6","6","6","6","6","6","6","6","6"],
    ["7","7","7","7","7","7","7","7","7"],
    ["8","8","8","8","8","8","8","8","8"],
    ["9","9","9","9","9","9","9","9","9"]
]
numset="123456789"
sq1=[]
sq2=[]
sq3=[]
sq4=[]
sq5=[]
sq6=[]
sq7=[]
sq8=[]
sq9=[]
row1=[]
row2=[]
row3=[]
row4=[]
row5=[]
row6=[]
row7=[]
row8=[]
row9=[]
col1=[]
col2=[]
col3=[]
col4=[]
col5=[]
col6=[]
col7=[]
col8=[]
col9=[]
os.system("cls")
display_board(board)
enterboard()
validate_lists()
congrats()
#1216
#End of Program.



