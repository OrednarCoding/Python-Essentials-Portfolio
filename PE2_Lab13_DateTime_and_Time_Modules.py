#===================================================================
# Project: The datetime and time Modules
# Course: Cisco Python Essentials 2
# Lab: PE2 Lab 13
#
# Student: Randy Crawford
# Date Started: 08/13/2026
# Date Completed:
#
# Original Lab Requirements:
# Use the datetime and time modules to create and format date and
# time information using the required output format.
#
# Program Design:
# Create datetime objects and use strftime() formatting codes to
# display date and time values in the exact format required by the
# lab.
#
# Verification:
# Compare the program output against the required lab output and
# verify each date/time line matches the specified format.
#
#1002,0918,0922,1104,0707,1216,0304,0410,0114,2008
#=================================================================
import os
os.system("cls")
from datetime import datetime
current = datetime(2020, 11, 4, 14, 53, 0)
print(current)
print(current.strftime("%Y-%m-%d"))
print(current.strftime("%H:%M:%S"))
print(current.strftime("%Y/%m/%d %H:%M:%S"))
print(current.strftime("%A"))
print(current.strftime("%B"))
print(current.strftime("%A, %B %d, %Y"))
print(current.strftime("%y/%B/%d %H:%M:%S %p"))
print(current.strftime("%a, %Y %b %d"))
print(current.strftime("%A, %Y %B %d"))
print(current.strftime("Weekday: %w"))
print(current.strftime("Day of the year: %j"))
print(current.strftime("Week number of the year: %W"))
