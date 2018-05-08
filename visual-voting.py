from tkinter import *

boxWindow = Tk()
boxWindow.title("Voting Machine")
boxWindow.geometry('300x250')

print("-------------------------------------------")
print("*******************************************")
print("*******************************************")
print("************* Election Machine ************")
print("******************Results******************")
print("*******************************************")
print("-------------------------------------------")

def callLabour():
    print("\n-----Labour-----")

def callConservatives():
    print("\n-----Conservatives-----")

def callLibDems():
    print("\n-----LibDems-----")
    
 
Labour = Button(boxWindow, text="Labour", bg="red", command=callLabour)
Labour.pack()

Conservatives = Button(boxWindow, text="Conservatives", bg="blue", fg="white", command=callConservatives)
Conservatives.pack()

LibDems = Button(boxWindow, text="LibDems", bg="yellow", command=callLibDems)
LibDems.pack()

mainloop()
