import random
import string
import os
import ctypes
import pyperclip as clip
import tkinter

if os.name == "nt":
    os.system("cls")
elif os.name == "posix":
    os.system("clear") 
print("-----------------------------------------")
print("     Silvestris Password Generator")
print("-----------------------------------------")
flag1=0
while flag1==0:
    leng = int(input("How many digits is your password?\n=>"))
    flag1=1
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
x="".join(random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation, leng))
print("-----------------------------------------")
print("Your password is ", x)
print("Copy or save? (C=>Copy, S=>Save)")
flag2=0
while flag2==0:
    ans=input("=>")
    if ans=="C":
        clip.copy(x)
        flag2=1
    elif ans=="c":
        clip.copy(x)
        flag2=1
    elif ans=="S":
        print("Which app will you use this password in?")
        ans2=input("=>")
        file = open("Passwords.txt", "a")
        file.write(ans2 + " => " + x + "\n")
        print("Saved to passwords.txt in this folder")
        flag2=1
    elif ans=="s":
        print("Which app will you use this password in?")
        ans2=input("=>")
        file = open("Passwords.txt", "a")
        file.write(ans2 + " => " + x + "\n")
        print("Saved to passwords.txt in this folder")
        flag2=1
    else:
        print("Please input again")
print("Press a button for exit")
input("")
