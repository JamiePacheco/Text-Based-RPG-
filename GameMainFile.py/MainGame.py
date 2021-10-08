import room
import combat
import time
import random
import sys
import os

def string(x):
    i = 0
    while i < len(x):
        for char in x: 
            print(char, end="") 
            sys.stdout.flush() 
            time.sleep(0.02) 
            i += 1
    else:
        print("")

string("WELCOME TO JAMIE'S RPG GAME\n")
string("WHAT IS YOUR NAME?")
name = input(":")

string(f"\nWELL {name} THIS IS THE START OF YOUR JOURNEY")
time.sleep(1)
os.system("cls")


room.RoomCode()                     
