from tkinter import *

window = Tk()
window.title("Voting Machine")
window.geometry('300x250')

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

def vote(party):
    print(party)
    
 
Labour = Button(window, text="Labour", bg="red", command=callLabour)
Labour.pack()

Conservatives = Button(window, text="Conservatives", bg="blue", fg="white", command=callConservatives)
Conservatives.pack()

LibDems = Button(window, text="LibDems", bg="yellow", command=callLibDems)
LibDems.pack()

mainloop()
