from tkinter import *

def View():
    timesList.delete(0,END)
    num = int(numEntry.get())
    for i in range(1,13):
        result = i*num
        timesList.insert(END,(i,"x",num,"=",result))

def Clear():
    timesList.delete(0,END)
    numEntry.delete(0,END)

window = Tk()
window.geometry("335x270")
window.title("Times Table")

numLabel = Label(text = "Enter a number:")
numLabel.place(x =10 , y= 25 ,height = 25)

numEntry =Entry(relief="flat",)
numEntry.place(x =100 ,y = 25,width = 100,height=25)
numEntry.focus()

timesList= Listbox(relief="flat")
timesList.place(x=100,y=60,width=100,height=200)

viewBtn = Button(text="View Times Table",relief="groove",command=View)
viewBtn.place(x=210 ,y=25,width=100,height=25)

clearBtn = Button(text="Clear",relief="groove",command=Clear)
clearBtn.place(x=210 ,y=60,width=100,height=25)

window.mainloop()