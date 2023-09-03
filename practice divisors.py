#!usr/bin/env python3
# Tyler Kirkwood

import sys

def age():
    age = int(input("enter your age: ")) 
    if age < 19:
        print("you may not purchase alcohol.")
    elif age < 25:
        print("You may be asked to show you ID.")
    else: 
        print("your are old.")

age()