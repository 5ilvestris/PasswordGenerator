import random
import string
import os
import pyperclip as clip
from tkinter import messagebox
import tkinter
if os.name == "nt":
    os.system("cls")
elif os.name == "posix":
    os.system("clear")
print("-----------------------------------------")
print("     Silvestris Password Generator")
print("-----------------------------------------")
leng = int(input("How many digits is your password?\n=>"))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
x="".join(random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation, leng))
print(x)
clip.copy(x)
import ctypes # An included library with Python install. 
def Mbox(title, text, style): 
    return ctypes.windll.user32.MessageBoxW(0, text, title, style) 
Mbox("Successfull", "Password is copied\nYour password is:\n=> " + x, 1)
