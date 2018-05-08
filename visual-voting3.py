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

def vote(party):
    print(party)
    labourTally = 0
    consTally = 0
    libdemTally = 0
    if party == "Labour": labourTally = labourTally + 1
    elif party == "Conservatives": consTally = consTally + 1
    elif party == "LibDems": libdemTally = libdemTally + 1
    #file.write(labourTally,consTally,libdemTally)

lbl = Label(window, text="Press to vote. You may only vote once.")
lbl.grid(column=0, row=0)

Labour = Button(window, text="Labour", bg="red", command=vote("Labour"))
Labour.grid(column=0, row=2)

Conservatives = Button(window, text="Conservatives", bg="blue", fg="white", command=vote("Conservative"))
Conservatives.grid(column=0, row=3)

LibDems = Button(window, text="LibDems", bg="yellow", command=vote("LibDem"))
LibDems.grid(column=0, row=4)

window.mainloop()
