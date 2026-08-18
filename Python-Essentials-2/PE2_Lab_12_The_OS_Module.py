#===================================================================
# Project: The OS Module
# Course: Cisco Python Essentials 2
# Lab: PE2 Lab 12
#
# Student: Randy Crawford
# Date Started: 08/13/2026
# Date Completed:
#
# Original Lab Requirements:
# Write a program that searches a directory tree for directories
# with a specified name.
#
# The program must begin searching from a supplied starting path
# and examine that directory and all directories contained beneath
# it.
#
# Each time a directory matching the requested name is found, the
# program must display the absolute path to that directory.
#
# Program Design:
# Create a find(path, dir) function. The function receives the
# starting search path and the directory name to search for.
#
# The search must work through directory structures of different
# depths. Recursion will be used so the function can continue
# searching inside subdirectories.
#
# Verification:
# Test the program using a directory tree containing multiple
# directories with the same requested name at different levels.
# Every matching directory should be displayed with its full
# absolute path.
#
#1002,0918,0922,1104,0707,1216,0304,0410,0114,2008
#===================================================================
import os
os.system("cls")
def find(path, dir):
    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        if os.path.isdir(full_path):
            if item == dir:
                print(os.path.abspath(full_path))

            find(full_path, dir)
    

find(r"C:\Users\radcr\Downloads", "python")




    
