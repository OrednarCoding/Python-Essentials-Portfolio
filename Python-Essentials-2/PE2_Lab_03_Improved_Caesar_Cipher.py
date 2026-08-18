#===================================================================
# Project: Improved Caesar Cipher
# Course: Cisco Python Essentials 2
# Lab: PE2 Lab 03
#
# Student: Randy Crawford
# Date Started: 08/05/2026
# Date Completed: 08/05/2026
#
# Encrypt a message using a variable Caesar cipher shift while
# preserving upper/lower case and leaving non-letter characters
# unchanged.
#===================================================================

def input_shift():
    while True:
        try:
            x=int(input("Please enter the shift for the cipher(+)/decipher(-) : "))
            return x
        except ValueError:
            print("Please try again with a number only ")
#1002
        

def input_message():
    y=input("Please enter your message to be coded or decoded : ")
    return y
#0918
def cipher_decipher(shift, message):
    code=[]
    for letter in message:
        
        if letter in alphabet:
            position = alphabet.index(letter)            
            new_position = (position + shift)%26            
            code.append(alphabet[new_position])
        elif letter in ALPHABET:
            position = ALPHABET.index(letter)            
            new_position = (position + shift)%26
            code.append(ALPHABET[new_position])
        else:
            code.append(letter)
    return code
#0922

def display_code(code):
    nm=""
    for i in range(len(code)):
        nm +=code[i]
    return nm
#1104

#main program
ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet="abcdefghijklmnopqrstuvwxyz"
shift=input_shift()
message=input_message()

code=cipher_decipher(shift, message)
new_message = display_code(code)
print(new_message)
#0707
#End Program
