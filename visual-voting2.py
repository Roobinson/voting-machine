from subprocess import call
import sys
from tkinter import *

master = Tk()

print("-------------------------------------------")
print("*******************************************")
print("*******************************************")
print("************* Election Machine ************")
print("*******************************************")
print("*******************************************")
print("-------------------------------------------")

def callLabour():
    print("\n-----Labour-----")

def callConservatives():
    print("\n-----Conservatives-----")

def callLibDems():
    print("\n-----LibDems-----")

Labour = Button(master, text="Labour", command=callLabour)
Labour.pack()

Conservatives = Button(master, text="Conservatives", command=callConservatives)
Conservatives.pack()

LibDems = Button(master, text="LibDems", command=callLibDems)
LibDems.pack()

mainloop()
