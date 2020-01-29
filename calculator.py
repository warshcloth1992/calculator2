"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

input_string = ""

while input_string != "q":
    input_string = input("enter tokens here: ")
    TokensList = input_string.split(" ")

    if TokensList[0] == "+":

        print(add(int(TokensList[1]), int(TokensList[2])))