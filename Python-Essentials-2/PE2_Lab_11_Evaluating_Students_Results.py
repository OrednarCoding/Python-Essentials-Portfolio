#===================================================================
# Project: Evaluating Students' Results
# Course: Cisco Python Essentials 2
# Lab: PE2 Lab 11
#
# Student: Randy Crawford
# Date Started: 08/12/2026
# Date Completed: 08/12/2026
#
# Original Lab Requirements:
# Read a user-selected text file containing student first names,
# last names, and points earned. Calculate the total points earned
# by each student and display a sorted report of the results.
#
# Each student may appear multiple times in the source file. The
# program must combine those entries and calculate the student's
# total points.
#
# The program must be protected against possible file and data
# failures, including a missing file, an empty file, and invalid
# input data. Custom exceptions must be used for invalid lines
# and empty source files.
#
# Program Design:
# Use a dictionary to store student results. Each student's first
# and last name will be combined into a tuple and used as the
# dictionary key. The dictionary value will contain the student's
# accumulated point total.
#
# Verification:
# Repeated entries for the same student must be combined correctly,
# and the final report must be sorted and display each student's
# total points.
#
#1002,0918,0922,1104,0707,1216,0304,0410,0114,2008
#===================================================================
def enterfile():
    try:
        os.chdir(r"C:\\Users\\radcr\\Downloads")
        filename=input("Enter the name of the file: ")
        f = open(filename, "r")
        lines = f.readlines()
        if len(lines) == 0:
            raise FileEmpty
        for line in lines:
            text=line.split()
            if len(text) !=3:
                raise BadLine
            students_add(text)         
        f.close()
    except FileNotFoundError:
        print("There is no file with this name. This is an error.")
        raise SystemExit

    except FileEmpty:
        print("The file is empty. This is an error.")
        raise SystemExit

    except BadLine:
        print("There is a bad line in this file. This is an error.")
        raise SystemExit

    except ValueError:
        value_error()
    return 
#1002
def students_add(text):
    first_name = text[0]
    last_name = text[1]
    points = float(text[2])
    student=(first_name, last_name)
    if student in students:
        students[student] +=points
    else:
        students[student] = points
#0918
def display_results(sd):
    for student, points in sd.items():
        print(f"{student[0]} {student[1]} - {points}")
#0922
def student_order(students):
    sorted_dic  = sorted(students.items(), key=lambda item: item[0])
    sorted_dict = dict(sorted_dic)
    return sorted_dict
#1104        
def value_error():
    print("There is a bad Value in this file this is an error")
    raise SystemExit
#0114 


#Main Program
import os
class StudentsDataExceptions(Exception):
    pass
class BadLine(StudentsDataExceptions):
    pass
class FileEmpty(StudentsDataExceptions):
    pass
os.system("cls")
students={}
first_name = ()
last_name = ()
points = ()
enterfile()
sd = student_order(students)
display_results(sd)
#2008
#End of Program





    
